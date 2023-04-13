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
from models.child import (
    CreateChildForm,
    Child,
)
from models.deworming import Deworming
from models.dispensary import Dispensary
from models.extra_classes import ExtraClass
from models.hospitalization import Hospitalization
from models.kindergarten import KindergartenWithChildrens
from models.medical_certificate import MedicalCertificate
from models.oral_sanation import OralSanation
from models.parent import ParentCreate
from models.past_illness import PastIllness
from models.spa_treatment import SpaTreatment
from models.visit_specialist_control import VisitSpecialistControl

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


    def get_hospitalizations_by_medcard_num(self, medcard_num: int) -> list[Hospitalization]:
        query = f"""SELECT  * FROM hospitalizations WHERE medcard_num = {medcard_num} ORDER BY start_date"""
        selected_hospitalizations = execute_read_query_all(self.connection, query)
        hospitalizations = []
        for hospitalization in selected_hospitalizations:
            hospitalizations.append(SerializationService.serialization_hospitalization(hospitalization))
        return hospitalizations
    
    def get_hospitalization_by_pk(self, hospitalization_data: dict) -> Hospitalization:
        query = f"""SELECT * FROM hospitalizations WHERE medcard_num = '{hospitalization_data["medcard_num"]}' AND
                                                         start_date = '{hospitalization_data["start_date"]}'"""
        hospitalization = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_hospitalization(hospitalization)

    def add_new_hospitalization(self, hospitalization: dict):
        if not hospitalization["end_date"]:
            hospitalization["end_date"] = None

        query = f"""INSERT INTO hospitalizations (medcard_num, start_date, end_date, diagnosis, founding) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(founding)s)"""
        execute_data_query(self.connection, query, hospitalization)
    
    def update_hospitalization(self, hospitalization: dict):
        if not hospitalization["end_date"]:
            hospitalization["end_date"] = None

        query = f"""UPDATE  hospitalizations SET start_date = %(start_date)s, 
                                                 end_date = %(end_date)s, 
                                                 diagnosis = %(diagnosis)s,
                                                 founding = %(founding)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s"""
        execute_data_query(self.connection, query, hospitalization)

    def delete_hospitalization(self, hospitalization: dict):
        query = f"""DELETE FROM hospitalizations WHERE  medcard_num = %(medcard_num)s AND
                                                        start_date = %(start_date)s"""
        execute_data_query(self.connection, query, hospitalization)


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


    def get_dispensaryes_by_medcard_num(self, medcard_num: int) -> list[Dispensary]:
            query = f"""SELECT  * FROM dispensaryes WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_dispensaryes = execute_read_query_all(self.connection, query)
            dispensaryes = []
            for dispensary in selected_dispensaryes:
                dispensaryes.append(SerializationService.serialization_dispensary(dispensary))
            return dispensaryes
    
    def get_dispensary_by_pk(self, dispensary_data: dict) -> Dispensary:
        query = f"""SELECT * FROM dispensaryes WHERE medcard_num = '{dispensary_data["medcard_num"]}' AND
                                                         start_date = '{dispensary_data["start_date"]}'"""
        dispensary = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_dispensary(dispensary)

    def add_new_dispensary(self, dispensary: dict):
        if not dispensary["end_date"]:
            dispensary["end_date"] = None

        query = f"""INSERT INTO dispensaryes (medcard_num, start_date, end_date, diagnosis, specialist, end_reason) 
                         VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(specialist)s, %(end_reason)s)"""
        execute_data_query(self.connection, query, dispensary)
    
    def update_dispensary(self, dispensary: dict):
        if not dispensary["end_date"]:
            dispensary["end_date"] = None

        query = f"""UPDATE  dispensaryes SET start_date = %(start_date)s, 
                                                 end_date = %(end_date)s, 
                                                 diagnosis = %(diagnosis)s,
                                                 specialist = %(specialist)s,
                                                 end_reason = %(end_reason)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_date = %(old_start_date)s"""
        execute_data_query(self.connection, query, dispensary)

    def delete_dispensary(self, dispensary: dict):
        query = f"""DELETE FROM dispensaryes WHERE  medcard_num = %(medcard_num)s AND
                                                        start_date = %(start_date)s"""
        execute_data_query(self.connection, query, dispensary)


    def get_visit_specialist_controls_by_dispensary(self, visit_specialist_control_data: dict) -> list[VisitSpecialistControl]:
            query = f"""SELECT  * FROM visit_specialist_controls WHERE medcard_num = '{visit_specialist_control_data["medcard_num"]}' AND
                                                                       start_dispanser_date =  '{visit_specialist_control_data["start_dispanser_date"]}'
                        ORDER BY assigned_date"""
            selected_visit_specialist_controls = execute_read_query_all(self.connection, query)
            visit_specialist_controls = []
            for visit_specialist_control in selected_visit_specialist_controls:
                visit_specialist_controls.append(SerializationService.serialization_visit_specialist_control(visit_specialist_control))
            return visit_specialist_controls
    
    def get_visit_specialist_control_by_pk(self, visit_specialist_control_data: dict) -> VisitSpecialistControl:
        query = f"""SELECT  * FROM visit_specialist_controls WHERE medcard_num = '{visit_specialist_control_data["medcard_num"]}' AND
                                                                   start_dispanser_date =  '{visit_specialist_control_data["start_dispanser_date"]}' AND
                                                                   assigned_date = '{visit_specialist_control_data["assigned_date"]}'"""
        visit_specialist_control = execute_read_query_first(self.connection, query)

        return SerializationService.serialization_visit_specialist_control(visit_specialist_control)

    def add_new_visit_specialist_control(self, visit_specialist_control: dict):
        if not visit_specialist_control["fact_date"]:
            visit_specialist_control["fact_date"] = None

        query = f"""INSERT INTO visit_specialist_controls (medcard_num, start_dispanser_date, assigned_date, fact_date) 
                         VALUES (%(medcard_num)s, %(start_dispanser_date)s, %(assigned_date)s, %(fact_date)s)"""
        execute_data_query(self.connection, query, visit_specialist_control)
    
    def update_visit_specialist_control(self, visit_specialist_control: dict):
        if not visit_specialist_control["fact_date"]:
            visit_specialist_control["fact_date"] = None

        query = f"""UPDATE  visit_specialist_controls SET assigned_date = %(assigned_date)s, 
                                                 fact_date = %(fact_date)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            start_dispanser_date = %(start_dispanser_date)s AND
                            assigned_date = %(old_assigned_date)s"""
        execute_data_query(self.connection, query, visit_specialist_control)

    def delete_visit_specialist_control(self, visit_specialist_control: dict):
        query = f"""DELETE FROM visit_specialist_controls WHERE  medcard_num = %(medcard_num)s AND
                                                                 start_dispanser_date = %(start_dispanser_date)s AND
                                                                 assigned_date = %(assigned_date)s"""
        execute_data_query(self.connection, query, visit_specialist_control)


    def get_dewormings_by_medcard_num(self, medcard_num: int) -> list[Deworming]:
            query = f"""SELECT  * FROM dewormings WHERE medcard_num = {medcard_num} ORDER BY deworming_date"""
            selected_dewormings = execute_read_query_all(self.connection, query)
            dewormings = []
            for deworming in selected_dewormings:
                dewormings.append(SerializationService.serialization_deworming(deworming))
            return dewormings
    
    def get_deworming_by_pk(self, deworming_data: dict) -> Deworming:
        query = f"""SELECT * FROM dewormings WHERE medcard_num = '{deworming_data["medcard_num"]}' AND
                                                         deworming_date = '{deworming_data["deworming_date"]}'"""
        deworming = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_deworming(deworming)

    def add_new_deworming(self, deworming: dict):
        query = f"""INSERT INTO dewormings (medcard_num, deworming_date, result) 
                         VALUES (%(medcard_num)s, %(deworming_date)s, %(result)s)"""
        execute_data_query(self.connection, query, deworming)
    
    def update_deworming(self, deworming: dict):
        query = f"""UPDATE  dewormings SET deworming_date = %(deworming_date)s, 
                                           result = %(result)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            deworming_date = %(old_deworming_date)s"""
        execute_data_query(self.connection, query, deworming)

    def delete_deworming(self, deworming: dict):
        query = f"""DELETE FROM dewormings WHERE  medcard_num = %(medcard_num)s AND
                                                  deworming_date = %(deworming_date)s"""
        execute_data_query(self.connection, query, deworming)


    def get_oral_sanations_by_medcard_num(self, medcard_num: int) -> list[OralSanation]:
            query = f"""SELECT  * FROM oral_sanations WHERE medcard_num = {medcard_num} ORDER BY sanation_date"""
            selected_oral_sanations = execute_read_query_all(self.connection, query)
            oral_sanations = []
            for oral_sanation in selected_oral_sanations:
                oral_sanations.append(SerializationService.serialization_oral_sanation(oral_sanation))
            return oral_sanations
    
    def get_oral_sanation_by_pk(self, oral_sanation_data: dict) -> OralSanation:
        query = f"""SELECT * FROM oral_sanations WHERE medcard_num = '{oral_sanation_data["medcard_num"]}' AND
                                                       sanation_date = '{oral_sanation_data["sanation_date"]}'"""
        oral_sanation = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_oral_sanation(oral_sanation)

    def add_new_oral_sanation(self, oral_sanation: dict):
        query = f"""INSERT INTO oral_sanations (medcard_num, sanation_date, dental_result, sanation_result) 
                         VALUES (%(medcard_num)s, %(sanation_date)s, %(dental_result)s, %(sanation_result)s)"""
        execute_data_query(self.connection, query, oral_sanation)
    
    def update_oral_sanation(self, oral_sanation: dict):
        query = f"""UPDATE  oral_sanations SET sanation_date = %(sanation_date)s, 
                                               dental_result = %(dental_result)s,
                                               sanation_result = %(sanation_result)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            sanation_date = %(old_sanation_date)s"""
        execute_data_query(self.connection, query, oral_sanation)

    def delete_oral_sanation(self, oral_sanation: dict):
        query = f"""DELETE FROM oral_sanations WHERE  medcard_num = %(medcard_num)s AND
                                                  sanation_date = %(sanation_date)s"""
        execute_data_query(self.connection, query, oral_sanation)
