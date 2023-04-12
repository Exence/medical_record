import psycopg2

from pprint import pprint

from fastapi import (
    Depends,
    HTTPException,
)
from typing import (
    Any,
    )

from models.allergyes import Allergy
from models.extra_classes import ExtraClass
from models.child import (
    CreateChildForm,
    Child,
)
from models.kindergarten import KindergartenWithChildrens
from models.medical_certificate import MedicalCertificate
from models.parent import ParentCreate
from models.past_illness import PastIllness

from services.auth import AuthService
from services.kindergarten import get_kindergarten_num_by_name
from services.parent import select_parent_id
from services.serialization import SerializationService

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
    
def create_parent_tranzaction(connection: Any, parent: dict) -> bool:
    try:
        cursor = connection.cursor()
        query = f"""INSERT INTO parents (surname, name, patronymic, birthday_year, education, phone_num)
                    VALUES (%(surname)s, %(name)s, %(patronymic)s, %(birthday_year)s, %(education)s, %(phone_num)s)"""  
        cursor.execute(query, parent)
        query = f"""SELECT id FROM parents 
            WHERE   surname = '{parent["surname"]}' AND 
                    name = '{parent["name"]}' AND 
                    patronymic = '{parent["patronymic"]}' AND 
                    birthday_year = {parent["birthday_year"]} AND 
                    education = '{parent["education"]}' AND 
                    phone_num = {parent["phone_num"]}
            """
        cursor.execute(query)
        parent_id = cursor.fetchone()[0]
        query = f"""UPDATE childrens SET {parent["parent_type"]}_id = {parent_id} WHERE medcard_num = {parent["medcard_num"]}"""
        cursor.execute(query)

        connection.commit()
        return parent_id
        
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
        connection.rollback()
        return None
    
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

        return SerializationService.serialization_child(selected_child)
    


    def get_allergyes_by_medcard_num(self, medcard_num: int) -> list[Allergy]:
        query = f"""SELECT  * FROM allergyes WHERE medcard_num = {medcard_num} ORDER BY start_age"""
        selected_allergyes = execute_read_query_all(self.connection, query)
        allergyes = []
        for allergy in selected_allergyes:
            allergyes.append(SerializationService.serialization_allergy(allergy))
        
        return allergyes

    def add_new_allergy(self, medcard_num: int, allergy: dict):
        query = f"INSERT INTO allergyes (medcard_num, allergen, allergy_type, start_age, reaction_type, diagnosis_date, note) VALUES %s"
        allergy_data = SerializationService.serialization_allergy_to_create(medcard_num, allergy)
        execute_data_query(self.connection, query, allergy_data)

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


    def add_parent(self, parent: dict):
        return create_parent_tranzaction(self.connection, parent)
    
    
    def update_parent(self, parent: dict):
        query = f"""UPDATE parents SET  surname = %(surname)s,
                                        name = %(name)s,
                                        patronymic = %(patronymic)s,
                                        birthday_year = %(birthday_year)s,
                                        education = %(education)s,
                                        phone_num = %(phone_num)s
                    WHERE id = %(id)s"""
        execute_data_query(self.connection, query, parent)

    def delete_parent(self, parent_data: dict):
        query = f"DELETE FROM parents WHERE id = %(id)s"
        execute_data_query(self.connection, query, parent_data)



    def get_extra_classes_by_medcard_num(self, medcard_num: int) -> list[ExtraClass]:
        query = f"""SELECT  * FROM extra_classes WHERE medcard_num = {medcard_num} ORDER BY age"""
        selected_estra_classes = execute_read_query_all(self.connection, query)
        extra_classes = []
        for extra_class in selected_estra_classes:
            extra_classes.append(SerializationService.serialization_extra_class(extra_class))
        
        return extra_classes


    def add_new_extra_class(self, extra_class: dict):
        query = f"INSERT INTO extra_classes (medcard_num, classes_type, age, hours_on_week) VALUES (%(medcard_num)s, %(classes_type)s, %(age)s, %(hours_on_week)s)"
        execute_data_query(self.connection, query, extra_class)

    def update_extra_class(self, extra_class: dict):
        query = f"""UPDATE extra_classes SET    classes_type = %(classes_type)s,
                                                age = %(age)s,
                                                hours_on_week = %(hours_on_week)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            classes_type = %(old_classes_type)s AND
                            age = %(old_age)s"""
        execute_data_query(self.connection, query, extra_class)

    def delete_extra_class(self, extra_class: dict):
        print(extra_class)
        query = f"""DELETE FROM extra_classes WHERE medcard_num = %(medcard_num)s AND
                                                    classes_type = %(classes_type)s AND
                                                    age = %(age)s"""
        execute_data_query(self.connection, query, extra_class)


    def get_past_illnesses_by_medcard_num(self, medcard_num: int) -> list[PastIllness]:
        query = f"""SELECT  * FROM past_illnesses WHERE medcard_num = {medcard_num} ORDER BY diagnosis"""
        selected_past_illnesses = execute_read_query_all(self.connection, query)
        past_illnesses = []
        for past_illness in selected_past_illnesses:
            past_illnesses.append(SerializationService.serialization_past_illness(past_illness))
        
        return past_illnesses
    
    def get_past_illness_by_pk(self, past_illness_data: dict) -> PastIllness:
        query = f"""SELECT * FROM past_illnesses WHERE  medcard_num = '{past_illness_data["medcard_num"]}' AND
                                                        diagnosis = '{past_illness_data["diagnosis"]}' AND
                                                        start_date = '{past_illness_data["start_date"]}'"""
        past_illness = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_past_illness(past_illness)

    def add_new_past_illness(self, past_illness: dict):
        query = f"""INSERT INTO past_illnesses (medcard_num, start_date, end_date, diagnosis) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s)"""
        execute_data_query(self.connection, query, past_illness)
    
    def update_past_illness(self, past_illness: dict):
        print(past_illness)
        query = f"""UPDATE  past_illnesses SET  start_date = %(start_date)s, 
                                                end_date = %(end_date)s, 
                                                diagnosis = %(diagnosis)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s AND
                            diagnosis = %(old_diagnosis)s"""
        execute_data_query(self.connection, query, past_illness)

    def delete_past_illness(self, past_illness: dict):
        query = f"""DELETE FROM past_illnesses WHERE  medcard_num = %(medcard_num)s AND
                                                    start_date = %(start_date)s AND
                                                    diagnosis = %(diagnosis)s"""
        execute_data_query(self.connection, query, past_illness)


    def get_medical_certificates_by_medcard_num(self, medcard_num: int) -> list[MedicalCertificate]:
        query = f"""SELECT * FROM medical_certificates WHERE medcard_num = {medcard_num} ORDER BY start_date"""
        selected_medical_certificates = execute_read_query_all(self.connection, query)
        medical_certificates = []
        for medical_certificate in selected_medical_certificates:
            medical_certificates.append(SerializationService.serialization_medical_certificate(medical_certificate))
        
        return medical_certificates
    
    def get_medical_certificate_by_pk(self, medical_certificate_data: dict) -> MedicalCertificate:
        query = f"""SELECT * FROM medical_certificates WHERE    medcard_num = '{medical_certificate_data["medcard_num"]}' AND
                                                                disease = '{medical_certificate_data["disease"]}' AND
                                                                cert_date = '{medical_certificate_data["cert_date"]}'"""
        medical_certificate = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_medical_certificate(medical_certificate)
    
    def add_new_medical_certificate(self, medical_certificate: dict):
        if not medical_certificate["sport_exemption_date"]:
            medical_certificate["sport_exemption_date"] = None
        if not medical_certificate["vac_exemption_date"]:
            medical_certificate["vac_exemption_date"] = None

        query = f"""INSERT INTO medical_certificates (medcard_num, disease, cert_date, start_date, end_date, infection_contact, sport_exemption_date, vac_exemption_date, doctor) 
                VALUES (%(medcard_num)s, %(disease)s, %(cert_date)s, %(start_date)s, %(end_date)s, %(infection_contact)s, %(sport_exemption_date)s, %(vac_exemption_date)s, %(doctor)s)"""
        execute_data_query(self.connection, query, medical_certificate)

    def update_medical_certificate(self, medical_certificate: dict):
        if not medical_certificate["sport_exemption_date"]:
            medical_certificate["sport_exemption_date"] = None
        if not medical_certificate["vac_exemption_date"]:
            medical_certificate["vac_exemption_date"] = None

        query = f"""UPDATE medical_certificates SET disease = %(disease)s,
                                                    cert_date = %(cert_date)s,
                                                    start_date = %(start_date)s,
                                                    end_date = %(end_date)s,
                                                    infection_contact = %(infection_contact)s,
                                                    sport_exemption_date = %(sport_exemption_date)s,
                                                    vac_exemption_date = %(vac_exemption_date)s,
                                                    doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            disease = %(old_disease)s AND
                            cert_date = %(old_cert_date)s"""
        execute_data_query(self.connection, query, medical_certificate)

    def delete_medical_certificate(self, medical_certificate: dict):
        query = f"""DELETE FROM medical_certificates WHERE  medcard_num = %(medcard_num)s AND
                                                            disease = %(disease)s AND
                                                            cert_date = %(cert_date)s"""
        execute_data_query(self.connection, query, medical_certificate)
