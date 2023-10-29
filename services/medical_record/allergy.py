from fastapi import (
    Depends,
)
from typing import (
    Any,
    )

from database import (
    get_connection,
    execute_data_query,
    execute_read_query_all,
)
from services.serialization import SerializationService
from services.user import check_user_access

from models.allergyes import Allergy, AllergyUpdate, AllergyCreate, AllergyPK
from models.user import User
from models.exceptions import exception_403


def json_to_allergy_update(allergy_data: dict) -> AllergyUpdate:
    return AllergyUpdate(**allergy_data)
 
def json_to_allergy_create(allergy_data: dict) -> AllergyCreate:
    return AllergyCreate(**allergy_data)

def json_to_allergy_pk(allergy_data: dict) -> AllergyPK:
    return AllergyPK(**allergy_data)

class AllergyService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_allergyes_by_medcard_num(self, user: User, medcard_num: int) -> list[Allergy]:
        allergyes = []
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM allergyes WHERE medcard_num = {medcard_num} ORDER BY start_age"""
            selected_allergyes = execute_read_query_all(self.connection, query)
        
            for allergy in selected_allergyes:
                allergyes.append(SerializationService.serialization_allergy(allergy))
        
        return allergyes

    def add_new_allergy(self, user: User, allergy: AllergyCreate):
        if check_user_access(user=user, medcard_num=allergy.medcard_num):
            query = f"""INSERT INTO allergyes (medcard_num, allergen, allergy_type, start_age, reaction_type, diagnosis_date, note)
            VALUES ('{allergy.medcard_num}', '{allergy.allergen}', '{allergy.allergy_type}', '{allergy.start_age}', '{allergy.reaction_type}', '{allergy.diagnosis_date}', '{allergy.note}')"""
            execute_data_query(self.connection, query, allergy)
        else:
            raise exception_403 from None

    def update_allergy(self, user: User, allergy: AllergyUpdate):
        if check_user_access(user=user, medcard_num=allergy.medcard_num):
            query = f"""UPDATE allergyes SET    allergen = '{allergy.allergen}', 
                                                allergy_type = '{allergy.allergy_type}', 
                                                start_age = '{allergy.start_age}', 
                                                reaction_type = '{allergy.reaction_type}', 
                                                diagnosis_date = '{allergy.diagnosis_date}', 
                                                note = '{allergy.note}'
                        WHERE medcard_num = '{allergy.medcard_num}' AND allergen = '{allergy.prev_allergen}'"""
            execute_data_query(self.connection, query, allergy)
        else:
            raise exception_403 from None

    def delete_allergy(self, user: User, allergy: AllergyPK):
        if check_user_access(user=user, medcard_num=allergy.medcard_num):
            query = f"DELETE FROM allergyes WHERE medcard_num = '{allergy.medcard_num}' AND allergen = '{allergy.allergen}'"
            execute_data_query(self.connection, query, allergy)
        else:
            raise exception_403 from None
