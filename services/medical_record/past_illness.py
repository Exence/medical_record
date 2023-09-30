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

from models.past_illness import PastIllness


class PastIllnessService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_past_illnesses_by_medcard_num(self, medcard_num: int) -> list[PastIllness]:
        query = f"""SELECT  * FROM past_illnesses WHERE medcard_num = {medcard_num} ORDER BY diagnosis"""
        selected_past_illnesses = execute_read_query_all(self.connection, query)
        past_illnesses = []
        for past_illness in selected_past_illnesses:
            past_illnesses.append(SerializationService.serialization_past_illness(past_illness))
        
        return past_illnesses
    
    def get_past_illness_by_pk(self, past_illness_data: dict) -> PastIllness:
        query = f"""SELECT * FROM past_illnesses WHERE  medcard_num = '{past_illness_data["medcard_num"]}' AND
                                                        diagnosis = '{past_illness_data["diagnosis"]}' AND
                                                        start_date = '{past_illness_data["start_date"]}'"""
        past_illness = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_past_illness(past_illness)

    def add_new_past_illness(self, past_illness: dict):
        query = f"""INSERT INTO past_illnesses (medcard_num, start_date, end_date, diagnosis) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s)"""
        execute_data_query(self.connection, query, past_illness)
    
    def update_past_illness(self, past_illness: dict):
        query = f"""UPDATE  past_illnesses SET  start_date = %(start_date)s, 
                                                end_date = %(end_date)s, 
                                                diagnosis = %(diagnosis)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s AND
                            diagnosis = %(old_diagnosis)s"""
        execute_data_query(self.connection, query, past_illness)

    def delete_past_illness(self, past_illness: dict):
        query = f"""DELETE FROM past_illnesses WHERE  medcard_num = %(medcard_num)s AND
                                                    start_date = %(start_date)s AND
                                                    diagnosis = %(diagnosis)s"""
        execute_data_query(self.connection, query, past_illness)
