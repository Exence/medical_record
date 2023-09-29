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

from models.oral_sanation import OralSanation


class OralSanationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_oral_sanations_by_medcard_num(self, medcard_num: int) -> list[OralSanation]:
            query = f"""SELECT  * FROM oral_sanations WHERE medcard_num = {medcard_num} ORDER BY sanation_date"""
            selected_oral_sanations = execute_read_query_all(self.connection, query)
            oral_sanations = []
            for oral_sanation in selected_oral_sanations:
                oral_sanations.append(SerializationService.serialization_oral_sanation(oral_sanation))
            return oral_sanations
    
    def get_oral_sanation_by_pk(self, oral_sanation_data: dict) -> OralSanation:
        query = f"""SELECT * FROM oral_sanations WHERE medcard_num = '{oral_sanation_data["medcard_num"]}' AND
                                                       sanation_date = '{oral_sanation_data["sanation_date"]}'"""
        oral_sanation = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_oral_sanation(oral_sanation)

    def add_new_oral_sanation(self, oral_sanation: dict):
        query = f"""INSERT INTO oral_sanations (medcard_num, sanation_date, dental_result, sanation_result) 
                         VALUES (%(medcard_num)s, %(sanation_date)s, %(dental_result)s, %(sanation_result)s)"""
        execute_data_query(self.connection, query, oral_sanation)
    
    def update_oral_sanation(self, oral_sanation: dict):
        query = f"""UPDATE  oral_sanations SET sanation_date = %(sanation_date)s, 
                                               dental_result = %(dental_result)s,
                                               sanation_result = %(sanation_result)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            sanation_date = %(old_sanation_date)s"""
        execute_data_query(self.connection, query, oral_sanation)

    def delete_oral_sanation(self, oral_sanation: dict):
        query = f"""DELETE FROM oral_sanations WHERE  medcard_num = %(medcard_num)s AND
                                                  sanation_date = %(sanation_date)s"""
        execute_data_query(self.connection, query, oral_sanation)
