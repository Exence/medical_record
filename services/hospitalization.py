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

from models.hospitalization import Hospitalization


class HospitalizationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_hospitalizations_by_medcard_num(self, medcard_num: int) -> list[Hospitalization]:
        query = f"""SELECT  * FROM hospitalizations WHERE medcard_num = {medcard_num} ORDER BY start_date"""
        selected_hospitalizations = execute_read_query_all(self.connection, query)
        hospitalizations = []
        for hospitalization in selected_hospitalizations:
            hospitalizations.append(SerializationService.serialization_hospitalization(hospitalization))
        return hospitalizations
    
    def get_hospitalization_by_pk(self, hospitalization_data: dict) -> Hospitalization:
        query = f"""SELECT * FROM hospitalizations WHERE medcard_num = '{hospitalization_data["medcard_num"]}' AND
                                                         start_date = '{hospitalization_data["start_date"]}'"""
        hospitalization = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_hospitalization(hospitalization)

    def add_new_hospitalization(self, hospitalization: dict):
        if not hospitalization["end_date"]:
            hospitalization["end_date"] = None

        query = f"""INSERT INTO hospitalizations (medcard_num, start_date, end_date, diagnosis, founding) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(founding)s)"""
        execute_data_query(self.connection, query, hospitalization)
    
    def update_hospitalization(self, hospitalization: dict):
        if not hospitalization["end_date"]:
            hospitalization["end_date"] = None

        query = f"""UPDATE  hospitalizations SET start_date = %(start_date)s, 
                                                 end_date = %(end_date)s, 
                                                 diagnosis = %(diagnosis)s,
                                                 founding = %(founding)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s"""
        execute_data_query(self.connection, query, hospitalization)

    def delete_hospitalization(self, hospitalization: dict):
        query = f"""DELETE FROM hospitalizations WHERE  medcard_num = %(medcard_num)s AND
                                                        start_date = %(start_date)s"""
        execute_data_query(self.connection, query, hospitalization)
