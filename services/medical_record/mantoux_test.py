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
from services.user import check_user_access

from models.mantoux_test import MantouxTest
from models.user import User
from models.exceptions import exception_403


class MantouxTestService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_mantoux_tests_by_medcard_num(self, user: User, medcard_num: int) -> list[MantouxTest]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM mantoux_tests WHERE medcard_num = {medcard_num}  ORDER BY check_date"""
            selected_mantoux_tests = execute_read_query_all(self.connection, query)
            mantoux_tests = []
            for mantoux_test in selected_mantoux_tests:
                mantoux_tests.append(SerializationService.serialization_mantoux_test(mantoux_test))
            return mantoux_tests
        raise exception_403 from None
    
    def get_mantoux_test_by_pk(self, user: User, mantoux_test_data: dict) -> MantouxTest:
        if check_user_access(user=user, medcard_num=mantoux_test_data["medcard_num"]):
            query = f"""SELECT * FROM mantoux_tests WHERE medcard_num = '{mantoux_test_data["medcard_num"]}' AND
                                                        check_date = '{mantoux_test_data["check_date"]}'"""
            mantoux_test = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_mantoux_test(mantoux_test)
        raise exception_403 from None

    def add_new_mantoux_test(self, user: User, mantoux_test: dict):
        if check_user_access(user=user, medcard_num=mantoux_test["medcard_num"]):
            query = f"""INSERT INTO mantoux_tests (medcard_num, check_date, result) 
                            VALUES (%(medcard_num)s, %(check_date)s, %(result)s)"""
            execute_data_query(self.connection, query, mantoux_test)
        raise exception_403 from None
    
    def update_mantoux_test(self, user: User, mantoux_test: dict):
        if check_user_access(user=user, medcard_num=mantoux_test["medcard_num"]):
            query = f"""UPDATE mantoux_tests SET check_date = %(check_date)s,
                                                            result = %(result)s
                        WHERE medcard_num = %(medcard_num)s AND
                            check_date = %(old_check_date)s"""
            execute_data_query(self.connection, query, mantoux_test)
        raise exception_403 from None

    def delete_mantoux_test(self, user: User, mantoux_test: dict):
        if check_user_access(user=user, medcard_num=mantoux_test["medcard_num"]):
            query = f"""DELETE FROM mantoux_tests WHERE  medcard_num = %(medcard_num)s AND
                                                        check_date = %(check_date)s"""
            execute_data_query(self.connection, query, mantoux_test)
        raise exception_403 from None
