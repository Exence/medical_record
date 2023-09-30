import psycopg2

from fastapi import (
    Depends,
)
from typing import (
    Any,
    )

from database import (
    get_connection,
    execute_data_query,
    execute_read_query_first,
    execute_read_query_all,
)
from services.serialization import SerializationService

from models.mantoux_test import MantouxTest


class MantouxTestService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_mantoux_tests_by_medcard_num(self, medcard_num: int) -> list[MantouxTest]:
            query = f"""SELECT  * FROM mantoux_tests WHERE medcard_num = {medcard_num}  ORDER BY check_date"""
            selected_mantoux_tests = execute_read_query_all(self.connection, query)
            mantoux_tests = []
            for mantoux_test in selected_mantoux_tests:
                mantoux_tests.append(SerializationService.serialization_mantoux_test(mantoux_test))
            return mantoux_tests
    
    def get_mantoux_test_by_pk(self, mantoux_test_data: dict) -> MantouxTest:
        query = f"""SELECT * FROM mantoux_tests WHERE medcard_num = '{mantoux_test_data["medcard_num"]}' AND
                                                      check_date = '{mantoux_test_data["check_date"]}'"""
        mantoux_test = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_mantoux_test(mantoux_test)

    def add_new_mantoux_test(self, mantoux_test: dict):
        query = f"""INSERT INTO mantoux_tests (medcard_num, check_date, result) 
                         VALUES (%(medcard_num)s, %(check_date)s, %(result)s)"""
        execute_data_query(self.connection, query, mantoux_test)
    
    def update_mantoux_test(self, mantoux_test: dict):
        query = f"""UPDATE mantoux_tests SET check_date = %(check_date)s,
                                                         result = %(result)s
                    WHERE medcard_num = %(medcard_num)s AND
                          check_date = %(old_check_date)s"""
        execute_data_query(self.connection, query, mantoux_test)

    def delete_mantoux_test(self, mantoux_test: dict):
        query = f"""DELETE FROM mantoux_tests WHERE  medcard_num = %(medcard_num)s AND
                                                     check_date = %(check_date)s"""
        execute_data_query(self.connection, query, mantoux_test)
