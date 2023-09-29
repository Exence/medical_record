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

from models.spa_treatment import SpaTreatment


class SpaTreatmentService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_spa_treatments_by_medcard_num(self, medcard_num: int) -> list[SpaTreatment]:
            query = f"""SELECT  * FROM spa_treatments WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_spa_treatments = execute_read_query_all(self.connection, query)
            spa_treatments = []
            for spa_treatment in selected_spa_treatments:
                spa_treatments.append(SerializationService.serialization_spa_treatment(spa_treatment))
            return spa_treatments
    
    def get_spa_treatment_by_pk(self, spa_treatment_data: dict) -> SpaTreatment:
        query = f"""SELECT * FROM spa_treatments WHERE medcard_num = '{spa_treatment_data["medcard_num"]}' AND
                                                         start_date = '{spa_treatment_data["start_date"]}'"""
        spa_treatment = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_spa_treatment(spa_treatment)

    def add_new_spa_treatment(self, spa_treatment: dict):
        if not spa_treatment["end_date"]:
            spa_treatment["end_date"] = None

        query = f"""INSERT INTO spa_treatments (medcard_num, start_date, end_date, diagnosis, founding_specialization, climatic_zone) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(founding_specialization)s, %(climatic_zone)s)"""
        execute_data_query(self.connection, query, spa_treatment)
    
    def update_spa_treatment(self, spa_treatment: dict):
        if not spa_treatment["end_date"]:
            spa_treatment["end_date"] = None

        query = f"""UPDATE  spa_treatments SET start_date = %(start_date)s, 
                                                 end_date = %(end_date)s, 
                                                 diagnosis = %(diagnosis)s,
                                                 founding_specialization = %(founding_specialization)s,
                                                 climatic_zone = %(climatic_zone)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s"""
        execute_data_query(self.connection, query, spa_treatment)

    def delete_spa_treatment(self, spa_treatment: dict):
        query = f"""DELETE FROM spa_treatments WHERE  medcard_num = %(medcard_num)s AND
                                                        start_date = %(start_date)s"""
        execute_data_query(self.connection, query, spa_treatment)
