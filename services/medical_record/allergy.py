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

from models.allergyes import Allergy
from models.user import User
from models.exceptions import exception_403
 

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

    def add_new_allergy(self, user: User, medcard_num: int, allergy: dict):
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"INSERT INTO allergyes (medcard_num, allergen, allergy_type, start_age, reaction_type, diagnosis_date, note) VALUES %s"
            allergy_data = SerializationService.serialization_allergy_to_create(medcard_num, allergy)
            execute_data_query(self.connection, query, allergy_data)
        else:
            raise exception_403 from None

    def update_allergy(self, user: User, allergy: dict):
        if check_user_access(user=user, medcard_num=allergy["medcard_num"]):
            query = f"""UPDATE allergyes SET    allergen = %(allergen)s, 
                                                allergy_type = %(allergy_type)s, 
                                                start_age = %(start_age)s, 
                                                reaction_type = %(reaction_type)s, 
                                                diagnosis_date = %(diagnosis_date)s, 
                                                note = %(note)s
                        WHERE medcard_num = %(medcard_num)s AND allergen = %(prev_allergen)s"""
            execute_data_query(self.connection, query, allergy)
        else:
            raise exception_403 from None

    def delete_allergy(self, user: User, allergy: dict):
        if check_user_access(user=user, medcard_num=allergy["medcard_num"]):
            query = f"DELETE FROM allergyes WHERE medcard_num = %(medcard_num)s AND allergen = %(allergen)s"
            execute_data_query(self.connection, query, allergy)
        else:
            raise exception_403 from None
