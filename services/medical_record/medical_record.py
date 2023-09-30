import psycopg2

from fastapi import (
    Depends,
    HTTPException,
)
from typing import (
    Any,
    )

from models.kindergarten import KindergartenWithChildrens
from models.child import (
    CreateChildForm,
    Child,
)

from services.auth import AuthService
from services.kindergarten import (
    get_kindergarten_num_by_name,
    get_kindergarten_name_by_num,
)
from services.medical_record.parent import select_parent_id
from services.serialization import SerializationService

from settings import settings
from database import (
    get_connection,
    execute_data_query,
    execute_read_query_first,
    execute_read_query_all,
)

from models.parent import (
    Parent,
    ParentCreate,)


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

        child = SerializationService.serialization_child_to_create(form_data, father_id, mother_id, kindergarten_num)

        query = f"""INSERT INTO childrens (surname, name, patronymic, kindergarten_num, birthday, sex, group_num, address, clinic, edu_type, entering_date, father_id, mother_id, family_characteristics, family_microclimate, rest_and_class_opportunities, case_history) VALUES %s"""

        execute_data_query(connection, query, child)   
        
        return True     
        
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
    

class MedicalRecordService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def create_new_medcard(self, form_data: CreateChildForm, access_token: str):
        current_user = AuthService.validate_token(access_token)
        father = None
        mother = None

        if (form_data.father):
            father = SerializationService.serialization_parent_to_create(form_data.father.split())
        
        if (form_data.mother):
            mother = SerializationService.serialization_parent_to_create(form_data.mother.split())

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
            child = SerializationService.serialization_child_to_show(child)
            for kindergarten in kindergartens:
                if child.kindergarten_name == kindergarten.name:
                    kindergarten.groups[child.group_num - 1].append(child)

        return kindergartens          

    def get_child_by_medcard_num(self, medcard_num: int) -> Child:
        query = f"""SELECT  * FROM childrens WHERE medcard_num = {medcard_num}"""
        selected_child = execute_read_query_first(self.connection, query)
        child = SerializationService.serialization_child(selected_child)
        cursor = self.connection.cursor()
        kindergarten_name = get_kindergarten_name_by_num(cursor, child.kindergarten_num)
        cursor.close()
        child.kindergarten_name = kindergarten_name
        return child

    
    def update_child(self, child: dict):
        cursor = self.connection.cursor()
        kindergarten_num = get_kindergarten_num_by_name(cursor, child["kindergarten_name"])
        cursor.close()
        query = f"""UPDATE childrens SET surname = %(surname)s,
                                         name = %(name)s,
                                         patronymic = %(patronymic)s,
                                         kindergarten_num = {kindergarten_num},
                                         birthday = %(birthday)s,
                                         sex = %(sex)s,
                                         group_num = %(group_num)s,
                                         address = %(address)s,
                                         clinic = %(clinic)s,
                                         entering_date = %(entering_date)s,
                                         family_characteristics = %(family_characteristics)s,
                                         family_microclimate = %(family_microclimate)s,
                                         rest_and_class_opportunities = %(rest_and_class_opportunities)s,
                                         case_history = %(case_history)s
                    WHERE medcard_num = %(medcard_num)s"""
        execute_data_query(self.connection, query, child)
