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

from models.medical_examination import MedicalExamination


class MedicalExaminationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_medical_examinations_by_medcard_num(self, medcard_num: int) -> list[MedicalExamination]:
            query = f"""SELECT  * FROM medical_examinations WHERE medcard_num = {medcard_num} ORDER BY examination_date"""
            selected_medical_examinations = execute_read_query_all(self.connection, query)
            medical_examinations = []
            for medical_examination in selected_medical_examinations:
                medical_examinations.append(SerializationService.serialization_medical_examination(medical_examination))
            return medical_examinations
    
    def get_medical_examination_by_pk(self, medical_examination_data: dict) -> MedicalExamination:
        query = f"""SELECT * FROM medical_examinations WHERE medcard_num = '{medical_examination_data["medcard_num"]}' AND
                                                             period = '{medical_examination_data["period"]}'"""
        medical_examination = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_medical_examination(medical_examination)

    def add_new_medical_examination(self, medical_examination: dict) -> int:
        query = f"""INSERT INTO medical_examinations 
                         VALUES (%(medcard_num)s,
                                 %(period)s,
                                 %(examination_date)s,
                                 NULL,
                                 %(height)s,
                                 %(weight)s,
                                 %(complaints)s,
                                 %(pediatrician)s,
                                 %(orthopaedist)s,
                                 %(ophthalmologist)s,
                                 %(otolaryngologist)s,
                                 %(dermatologist)s,
                                 %(neurologist)s,
                                 %(speech_therapist)s,
                                 %(denta_surgeon)s,
                                 %(psychologist)s,
                                 %(other_doctors)s,
                                 %(blood_test)s,
                                 %(urine_analysis)s,
                                 %(feces_analysis)s,
                                 %(general_diagnosis)s,
                                 %(physical_development)s,
                                 %(mental_development)s,
                                 %(health_group)s,
                                 %(sport_group)s,
                                 %(med_and_ped_conclusion)s,
                                 %(recommendations)s
                                 )"""
        execute_data_query(self.connection, query, medical_examination)
        return self.get_medical_examination_by_pk(medical_examination).age
    
    def update_medical_examination(self, medical_examination: dict) -> int:
        query = f"""UPDATE medical_examinations SET period = %(period)s,
                                                    examination_date = %(examination_date)s,
                                                    height = %(height)s,
                                                    weight = %(weight)s,
                                                    complaints = %(complaints)s,
                                                    pediatrician = %(pediatrician)s,
                                                    orthopaedist = %(orthopaedist)s,
                                                    ophthalmologist = %(ophthalmologist)s,
                                                    otolaryngologist = %(otolaryngologist)s,
                                                    dermatologist = %(dermatologist)s,
                                                    neurologist = %(neurologist)s,
                                                    speech_therapist = %(speech_therapist)s,
                                                    denta_surgeon = %(denta_surgeon)s,
                                                    psychologist = %(psychologist)s,
                                                    other_doctors = %(other_doctors)s,
                                                    blood_test = %(blood_test)s,
                                                    urine_analysis = %(urine_analysis)s,
                                                    feces_analysis = %(feces_analysis)s,
                                                    general_diagnosis = %(general_diagnosis)s,
                                                    physical_development = %(physical_development)s,
                                                    mental_development = %(mental_development)s,
                                                    health_group = %(health_group)s,
                                                    sport_group = %(sport_group)s,
                                                    med_and_ped_conclusion = %(med_and_ped_conclusion)s,
                                                    recommendations = %(recommendations)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            period = %(old_period)s"""
        execute_data_query(self.connection, query, medical_examination)
        return self.get_medical_examination_by_pk(medical_examination).age

    def delete_medical_examination(self, medical_examination: dict):
        query = f"""DELETE FROM medical_examinations WHERE  medcard_num = %(medcard_num)s AND
                                                     period = %(period)s"""
        execute_data_query(self.connection, query, medical_examination)
