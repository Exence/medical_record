import psycopg2

from pprint import pprint

from fastapi import (
    Depends,
    HTTPException,
)
from typing import (
    Any,
    List,
    )

from models.allergyes import Allergy
from models.child import (
    CreateChildForm,
    Child,
)
from models.kindergarten import KindergartenWithChildrens
from models.parent import ParentCreate

from services.auth import AuthService
from services.kindergarten import get_kindergarten_num_by_name
from services.parent import select_parent_id
from services.serialization import (    
    serialization_allergy,
    serialization_allergy_to_create,
    serialization_child,
    serialization_child_to_create,
    serialization_child_to_show,
    serialization_parent_to_create,
    )

from settings import settings
from database import (
    get_connection,
    execute_data_query,
    execute_read_query_first,
    execute_read_query_all,
)


def create_medcard_tranzaction(connection: Any, father: ParentCreate, mother: ParentCreate, form_data:CreateChildForm) -> bool:
    try:
        cursor = connection.cursor()
        father_id = None
        mother_id = None

        query = f"""INSERT INTO parents (surname, name, patronymic, birthday_year, education, phone_num) VALUES %s"""

        if father and mother:  
            query += ", %s"      
            cursor.execute(query, [father.to_tuple(), mother.to_tuple()])
            father_id = select_parent_id(cursor, father)
            mother_id = select_parent_id(cursor, mother)
        elif father:
            cursor.execute(query, [father.to_tuple()])
            father_id = select_parent_id(cursor, father)
        else:
            cursor.execute(query, [mother.to_tuple()])
            mother_id = select_parent_id(cursor, mother)

        kindergarten_num = get_kindergarten_num_by_name(cursor, form_data.kindergarten_name)

        cursor.close()

        child = serialization_child_to_create(form_data, father_id, mother_id, kindergarten_num)

        query = f"""INSERT INTO childrens (surname, name, patronymic, kindergarten_num, birthday, sex, group_num, address, clinic, edu_type, entering_date, father_id, mother_id, family_characteristics, family_microclimate, rest_and_class_opportunities, case_history) VALUES %s"""

        execute_data_query(connection, query, child)   
        
        return True     
        
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
        connection.rollback()
        return False
    

class MedicalRecordService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def create_new_medcard(self, form_data: CreateChildForm, access_token: str):
        current_user = AuthService.validate_token(access_token)
        father = None
        mother = None

        if (form_data.father):
            father = serialization_parent_to_create(form_data.father.split())
        
        if (form_data.mother):
            mother = serialization_parent_to_create(form_data.mother.split())

        return create_medcard_tranzaction(self.connection, father, mother, form_data)    

    def get_all_childrens(self) -> list:
        query = f"""SELECT  * FROM all_childrens"""
        selected_childrens = execute_read_query_all(self.connection, query)

        query = f"""SELECT * FROM kindergartens
                    WHERE number <> 0"""
        selected_kindergartens = execute_read_query_all(self.connection, query)

        kindergartens = []
        for kindergarten in selected_kindergartens:
            kindergartens.append(KindergartenWithChildrens(number = kindergarten[0], name=kindergarten[1]))
        
        for child in selected_childrens:
            child = serialization_child_to_show(child)
            for kindergarten in kindergartens:
                if child.kindergarten_name == kindergarten.name:
                    kindergarten.groups[child.group_num - 1].append(child)

        return kindergartens          

    def get_child_by_medcard_num(self, medcard_num: int) -> Child:
        query = f"""SELECT  * FROM childrens WHERE medcard_num = {medcard_num}"""
        selected_child = execute_read_query_first(self.connection, query)

        return serialization_child(selected_child)
    
    def get_allergyes_by_medcard_num(self, medcard_num: int) -> list[Allergy]:
        query = f"""SELECT  * FROM allergyes WHERE medcard_num = {medcard_num} ORDER BY start_age"""
        selected_allergyes = execute_read_query_all(self.connection, query)
        allergyes = []
        for allergy in selected_allergyes:
            allergyes.append(serialization_allergy(allergy))
        
        return allergyes

    def add_new_allergy(self, medcard_num: int, allergy: dict):
        query = f"INSERT INTO allergyes (medcard_num, allergen, allergy_type, start_age, reaction_type, diagnosis_date, note) VALUES %s"
        allergy_data = serialization_allergy_to_create(medcard_num, allergy)
        execute_data_query(self.connection, query, allergy_data)
        print(allergy_data)

    def update_allergy(self, allergy: dict):
        query = f"""UPDATE allergyes SET    allergen = %(allergen)s, 
                                            allergy_type = %(allergy_type)s, 
                                            start_age = %(start_age)s, 
                                            reaction_type = %(reaction_type)s, 
                                            diagnosis_date = %(diagnosis_date)s, 
                                            note = %(note)s
                    WHERE medcard_num = %(medcard_num)s AND allergen = %(prev_allergen)s"""
        execute_data_query(self.connection, query, allergy)

    def delete_allergy(self, allergy: dict):
        query = f"DELETE FROM allergyes WHERE medcard_num = %(medcard_num)s AND allergen = %(allergen)s"
        execute_data_query(self.connection, query, allergy)


