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

from models.screening import Screening
from models.user import User
from models.exceptions import exception_403


class ScreeningService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_screenings_by_medcard_num(self, user: User, medcard_num: int) -> list[Screening]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM screenings WHERE medcard_num = {medcard_num} ORDER BY age"""
            selected_screenings = execute_read_query_all(self.connection, query)
            screenings = []
            for screening in selected_screenings:
                screenings.append(SerializationService.serialization_screening(screening))
            return screenings
        raise exception_403 from None
    
    def get_screening_by_pk(self, user: User, screening_data: dict) -> Screening:
        if check_user_access(user=user, medcard_num=screening_data["medcard_num"]):
            query = f"""SELECT * FROM screenings WHERE medcard_num = '{screening_data["medcard_num"]}' AND
                                                                    age = '{screening_data["age"]}'"""
            screening = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_screening(screening)
        raise exception_403 from None

    def add_new_screening(self, user: User, screening: dict):
        if check_user_access(user=user, medcard_num=screening["medcard_num"]):
            for key in ["physical_development", "blood_pressures", "carriage", "foot_condition", "sight_od", "sight_os", "visual_acuity","malinovsky_test", "binocular_vision", "hearing_acuteness", "dynammetry_left", "dynammetry_right", "physical_fitness", "protein_in_urine", "glucose_in_urine", "biological_age", "kern_test"]:
                if not screening[key]:
                    screening[key] = None
                
            query = f"""INSERT INTO screenings 
                            VALUES (%(medcard_num)s, 
                                    %(age)s,
                                    %(questionnaire_test)s,
                                    %(height)s,
                                    %(weight)s,
                                    %(physical_development)s, 
                                    %(blood_pressures)s,
                                    %(carriage)s,
                                    %(foot_condition)s,
                                    %(sight_od)s,
                                    %(sight_os)s, 
                                    %(visual_acuity)s,
                                    %(malinovsky_test)s,
                                    %(binocular_vision)s,
                                    %(hearing_acuteness)s,
                                    %(dynammetry_left)s, 
                                    %(dynammetry_right)s,
                                    %(physical_fitness)s,
                                    %(protein_in_urine)s,
                                    %(glucose_in_urine)s,
                                    %(biological_age)s, 
                                    %(speech_defects)s,
                                    %(kern_test)s,
                                    %(neurotic_disorders)s,
                                    %(thinking_and_speech_disorders)s,
                                    %(motor_development_disorders)s, 
                                    %(attention_and_memory_disorders)s,
                                    %(social_contacts_disorders)s,
                                    NULL)"""
            execute_data_query(self.connection, query, screening)
        else:
            raise exception_403 from None
    
    def update_screening(self, user: User, screening: dict):
        if check_user_access(user=user, medcard_num=screening["medcard_num"]):
            for key in ["physical_development", "blood_pressures", "carriage", "foot_condition", "sight_od", "sight_os", "visual_acuity","malinovsky_test", "binocular_vision", "hearing_acuteness", "dynammetry_left", "dynammetry_right", "physical_fitness", "protein_in_urine", "glucose_in_urine", "biological_age", "kern_test"]:
                if not screening[key]:
                    screening[key] = None

            query = f"""UPDATE screenings SET    age = %(age)s,
                                                questionnaire_test = %(questionnaire_test)s,
                                                height = %(height)s,
                                                weight = %(weight)s,
                                                physical_development = %(physical_development)s, 
                                                blood_pressures = %(blood_pressures)s,
                                                carriage = %(carriage)s,
                                                foot_condition = %(foot_condition)s,
                                                sight_od = %(sight_od)s,
                                                sight_os = %(sight_os)s, 
                                                visual_acuity = %(visual_acuity)s,
                                                malinovsky_test = %(malinovsky_test)s,
                                                binocular_vision = %(binocular_vision)s,
                                                hearing_acuteness = %(hearing_acuteness)s,
                                                dynammetry_left = %(dynammetry_left)s, 
                                                dynammetry_right = %(dynammetry_right)s,
                                                physical_fitness = %(physical_fitness)s,
                                                protein_in_urine = %(protein_in_urine)s,
                                                glucose_in_urine = %(glucose_in_urine)s,
                                                biological_age = %(biological_age)s, 
                                                speech_defects = %(speech_defects)s,
                                                kern_test = %(kern_test)s,
                                                neurotic_disorders = %(neurotic_disorders)s,
                                                thinking_and_speech_disorders = %(thinking_and_speech_disorders)s,
                                                motor_development_disorders = %(motor_development_disorders)s, 
                                                attention_and_memory_disorders = %(attention_and_memory_disorders)s,
                                                social_contacts_disorders = %(social_contacts_disorders)s
                        WHERE   medcard_num = %(medcard_num)s AND
                                age = %(old_age)s"""
            execute_data_query(self.connection, query, screening)
        else:
            raise exception_403 from None

    def delete_screening(self, user: User, screening: dict):
        if check_user_access(user=user, medcard_num=screening["medcard_num"]):
            query = f"""DELETE FROM screenings WHERE medcard_num = %(medcard_num)s AND
                                                    age = %(age)s"""
            execute_data_query(self.connection, query, screening)
        else:
            raise exception_403 from None
