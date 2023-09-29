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

from models.dispensary import Dispensary


class DispensaryService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_dispensaryes_by_medcard_num(self, medcard_num: int) -> list[Dispensary]:
            query = f"""SELECT  * FROM dispensaryes WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_dispensaryes = execute_read_query_all(self.connection, query)
            dispensaryes = []
            for dispensary in selected_dispensaryes:
                dispensaryes.append(SerializationService.serialization_dispensary(dispensary))
            return dispensaryes
    
    def get_dispensary_by_pk(self, dispensary_data: dict) -> Dispensary:
        query = f"""SELECT * FROM dispensaryes WHERE medcard_num = '{dispensary_data["medcard_num"]}' AND
                                                         start_date = '{dispensary_data["start_date"]}'"""
        dispensary = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_dispensary(dispensary)

    def add_new_dispensary(self, dispensary: dict):
        if not dispensary["end_date"]:
            dispensary["end_date"] = None

        query = f"""INSERT INTO dispensaryes (medcard_num, start_date, end_date, diagnosis, specialist, end_reason) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(specialist)s, %(end_reason)s)"""
        execute_data_query(self.connection, query, dispensary)
    
    def update_dispensary(self, dispensary: dict):
        if not dispensary["end_date"]:
            dispensary["end_date"] = None

        query = f"""UPDATE  dispensaryes SET start_date = %(start_date)s, 
                                                 end_date = %(end_date)s, 
                                                 diagnosis = %(diagnosis)s,
                                                 specialist = %(specialist)s,
                                                 end_reason = %(end_reason)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s"""
        execute_data_query(self.connection, query, dispensary)

    def delete_dispensary(self, dispensary: dict):
        query = f"""DELETE FROM dispensaryes WHERE  medcard_num = %(medcard_num)s AND
                                                        start_date = %(start_date)s"""
        execute_data_query(self.connection, query, dispensary)
