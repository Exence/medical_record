import psycopg2

from fastapi import (
    Depends,
    HTTPException,
)
from typing import Any

from models.child import (
    CreateChildForm,
)
from models.parent import ParentCreate

from services.auth import AuthService
from services.kindergarten import get_kindergarten_num_by_name
from services.parent import select_parent_id
from services.serialization import (
    serialization_parent_to_create,
    serialization_child_to_create,
    )

from settings import settings
from database import (
    get_connection,
    execute_insert_query,
    execute_read_query_first,
    execute_read_query_all,
)


def create_medcard_tranzaction(connection: Any, father: ParentCreate, mother: ParentCreate, form_data:CreateChildForm) -> bool:
    try:
        connection.autocommit=False
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

        child = [serialization_child_to_create(form_data, father_id, mother_id, kindergarten_num)]

        query = f"""INSERT INTO childrens (surname, name, patronymic, kindergarten_num, birthday, sex, group_num, address, clinic, edu_type, entering_date, father_id, mother_id, family_characteristics, family_microclimate, rest_and_class_opportunities, case_history) VALUES %s"""

        execute_insert_query(connection, query, child)   
        
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
        father_data = form_data.father.split()
        mother_data = form_data.mother.split()

        if (father_data):
            father = serialization_parent_to_create(father_data)
        
        if (mother_data):
            mother = serialization_parent_to_create(mother_data)

        return create_medcard_tranzaction(self.connection, father, mother, form_data)                
