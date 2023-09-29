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

from models.ongoing_medical_supervision import OngoingMedicalSupervision


class OngoingMedicalSupervisionService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_ongoing_medical_supervisions_by_medcard_num(self, medcard_num: int) -> list[OngoingMedicalSupervision]:
            query = f"""SELECT  * FROM ongoing_medical_supervisions WHERE medcard_num = {medcard_num} ORDER BY examination_date"""
            selected_ongoing_medical_supervisions = execute_read_query_all(self.connection, query)
            ongoing_medical_supervisions = []
            for ongoing_medical_supervision in selected_ongoing_medical_supervisions:
                ongoing_medical_supervisions.append(SerializationService.serialization_ongoing_medical_supervision(ongoing_medical_supervision))
            return ongoing_medical_supervisions
    
    def get_ongoing_medical_supervision_by_pk(self, ongoing_medical_supervision_data: dict) -> OngoingMedicalSupervision:
        query = f"""SELECT * FROM ongoing_medical_supervisions WHERE medcard_num = '{ongoing_medical_supervision_data["medcard_num"]}' AND
                                                                  examination_date = '{ongoing_medical_supervision_data["examination_date"]}'"""
        ongoing_medical_supervision = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_ongoing_medical_supervision(ongoing_medical_supervision)

    def add_new_ongoing_medical_supervision(self, ongoing_medical_supervision: dict):
        query = f"""INSERT INTO ongoing_medical_supervisions (medcard_num, examination_date, examination_data, diagnosis, prescription, doctor) 
                         VALUES (%(medcard_num)s, %(examination_date)s, %(examination_data)s, %(diagnosis)s, %(prescription)s, %(doctor)s)"""
        execute_data_query(self.connection, query, ongoing_medical_supervision)
    
    def update_ongoing_medical_supervision(self, ongoing_medical_supervision: dict):
        query = f"""UPDATE ongoing_medical_supervisions SET examination_date = %(examination_date)s,
                                            examination_data = %(examination_data)s, 
                                            diagnosis = %(diagnosis)s,
                                            prescription = %(prescription)s,
                                            doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            examination_date = %(old_examination_date)s"""
        execute_data_query(self.connection, query, ongoing_medical_supervision)

    def delete_ongoing_medical_supervision(self, ongoing_medical_supervision: dict):
        query = f"""DELETE FROM ongoing_medical_supervisions WHERE  medcard_num = %(medcard_num)s AND
                                                     examination_date = %(examination_date)s"""
        execute_data_query(self.connection, query, ongoing_medical_supervision)