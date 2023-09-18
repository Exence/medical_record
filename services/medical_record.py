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
from models.gg_injection import GammaGlobulinInjection
from models.hospitalization import Hospitalization
from models.kindergarten import KindergartenWithChildrens
from models.mantoux_test import MantouxTest
from models.medical_certificate import MedicalCertificate
from models.medical_examination import MedicalExamination
from models.ongoing_medical_supervision import OngoingMedicalSupervision
from models.oral_sanation import OralSanation
from models.parent import ParentCreate
from models.past_illness import PastIllness
from models.screening import Screening
from models.spa_treatment import SpaTreatment
from models.tub_vac import TuberculosisVaccination
from models.vaccination import Vaccination
from models.visit_specialist_control import VisitSpecialistControl

from services.auth import AuthService
from services.kindergarten import (
    get_kindergarten_num_by_name,
    get_kindergarten_name_by_num,
)
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


    def get_prevaccination_checkups_by_medcard_num(self, medcard_num: int) -> list[OralSanation]:
            query = f"""SELECT  * FROM prevaccination_checkups_view WHERE medcard_num = {medcard_num}"""
            selected_prevaccination_checkups = execute_read_query_all(self.connection, query)
            prevaccination_checkups = []
            for prevaccination_checkup in selected_prevaccination_checkups:
                prevaccination_checkups.append(SerializationService.serialization_prevaccination_checkup(prevaccination_checkup))
            return prevaccination_checkups
    
    def get_prevaccination_checkup_by_pk(self, prevaccination_checkup_data: dict) -> OralSanation:
        query = f"""SELECT * FROM prevaccination_checkups_view WHERE medcard_num = '{prevaccination_checkup_data["medcard_num"]}' AND
                                                                     examination_date = '{prevaccination_checkup_data["examination_date"]}'"""
        prevaccination_checkup = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_prevaccination_checkup(prevaccination_checkup)

    def add_new_prevaccination_checkup(self, prevaccination_checkup: dict):
        if not prevaccination_checkup["no_vac_date"]:
            prevaccination_checkup["no_vac_date"] = None

        query = f"""INSERT INTO prevaccination_checkups (medcard_num, examination_date, diagnosis, report, vac_name_id, no_vac_date, doctor) 
                         VALUES (%(medcard_num)s, %(examination_date)s, %(diagnosis)s, %(report)s, %(vac_name_id)s, %(no_vac_date)s, %(doctor)s)"""
        execute_data_query(self.connection, query, prevaccination_checkup)
        return self.get_prevaccination_checkup_by_pk(prevaccination_checkup)
    
    def update_prevaccination_checkup(self, prevaccination_checkup: dict):
        if not prevaccination_checkup["no_vac_date"]:
            prevaccination_checkup["no_vac_date"] = None

        query = f"""UPDATE  prevaccination_checkups SET examination_date = %(examination_date)s, 
                                               diagnosis = %(diagnosis)s,
                                               report = %(report)s,
                                               vac_name_id = %(vac_name_id)s,
                                               no_vac_date = %(no_vac_date)s,
                                               doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            examination_date = %(old_examination_date)s"""
        execute_data_query(self.connection, query, prevaccination_checkup)
        return self.get_prevaccination_checkup_by_pk(prevaccination_checkup)

    def delete_prevaccination_checkup(self, prevaccination_checkup: dict):
        query = f"""DELETE FROM prevaccination_checkups WHERE  medcard_num = %(medcard_num)s AND
                                                  examination_date = %(examination_date)s"""
        execute_data_query(self.connection, query, prevaccination_checkup)


    def get_prof_vaccinations_by_medcard_num(self, medcard_num: int) -> list[Vaccination]:
            query = f"""SELECT  * FROM prof_vaccinations WHERE medcard_num = {medcard_num}"""
            selected_prof_vaccinations = execute_read_query_all(self.connection, query)
            prof_vaccinations = []
            for prof_vaccination in selected_prof_vaccinations:
                prof_vaccinations.append(SerializationService.serialization_vaccination(prof_vaccination))
            return prof_vaccinations
    
    def get_prof_vaccination_by_pk(self, prof_vaccination_data: dict) -> Vaccination:
        query = f"""SELECT * FROM prof_vaccinations WHERE medcard_num = '{prof_vaccination_data["medcard_num"]}' AND
                                                          vac_name_id = '{prof_vaccination_data["vac_name_id"]}' AND
                                                          vac_type = '{prof_vaccination_data["vac_type"]}'"""
        prof_vaccination = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_vaccination(prof_vaccination)

    def add_new_vaccination(self, vaccination: dict):
        query = f"""INSERT INTO vaccinations (medcard_num, vac_name_id, vac_type, vac_date, serial, dose, introduction_method, reaction, doctor) 
                         VALUES (%(medcard_num)s, %(vac_name_id)s, %(vac_type)s, %(vac_date)s, %(serial)s, %(dose)s, %(introduction_method)s, %(reaction)s, %(doctor)s)"""
        execute_data_query(self.connection, query, vaccination)
    
    def update_vaccination(self, vaccination: dict):
        query = f"""UPDATE vaccinations SET vac_name_id = %(vac_name_id)s, 
                                            vac_type = %(vac_type)s,
                                            vac_date = %(vac_date)s,
                                            serial = %(serial)s, 
                                            dose = %(dose)s,
                                            introduction_method = %(introduction_method)s,
                                            reaction = %(reaction)s, 
                                            doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            vac_name_id = %(old_vac_name_id)s AND
                            vac_type = %(old_vac_type)s"""
        execute_data_query(self.connection, query, vaccination)

    def delete_vaccination(self, vaccination: dict):
        query = f"""DELETE FROM vaccinations WHERE  medcard_num = %(medcard_num)s AND
                                                    vac_name_id = %(vac_name_id)s AND
                                                    vac_type = %(vac_type)s"""
        execute_data_query(self.connection, query, vaccination)


    def get_epid_vaccinations_by_medcard_num(self, medcard_num: int) -> list[Vaccination]:
            query = f"""SELECT  * FROM epid_vaccinations WHERE medcard_num = {medcard_num}"""
            selected_epid_vaccinations = execute_read_query_all(self.connection, query)
            epid_vaccinations = []
            for epid_vaccination in selected_epid_vaccinations:
                epid_vaccinations.append(SerializationService.serialization_vaccination(epid_vaccination))
            return epid_vaccinations
    
    def get_epid_vaccination_by_pk(self, epid_vaccination_data: dict) -> Vaccination:
        query = f"""SELECT * FROM epid_vaccinations WHERE medcard_num = '{epid_vaccination_data["medcard_num"]}' AND
                                                          vac_name_id = '{epid_vaccination_data["vac_name_id"]}' AND
                                                          vac_type = '{epid_vaccination_data["vac_type"]}'"""
        epid_vaccination = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_vaccination(epid_vaccination)


    def get_gg_injections_by_medcard_num(self, medcard_num: int) -> list[GammaGlobulinInjection]:
            query = f"""SELECT  * FROM gamma_globulin_injections WHERE medcard_num = {medcard_num}  ORDER BY vac_date"""
            selected_gg_injections = execute_read_query_all(self.connection, query)
            gg_injections = []
            for gg_injection in selected_gg_injections:
                gg_injections.append(SerializationService.serialization_gg_injection(gg_injection))
            return gg_injections
    
    def get_gg_injection_by_pk(self, gg_injection_data: dict) -> GammaGlobulinInjection:
        query = f"""SELECT * FROM gamma_globulin_injections WHERE medcard_num = '{gg_injection_data["medcard_num"]}' AND
                                                                  vac_date = '{gg_injection_data["vac_date"]}'"""
        gg_injection = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_gg_injection(gg_injection)

    def add_new_gg_injection(self, gg_injection: dict):
        query = f"""INSERT INTO gamma_globulin_injections (medcard_num, vac_date, reason, serial, dose, reaction, doctor) 
                         VALUES (%(medcard_num)s, %(vac_date)s, %(reason)s, %(serial)s, %(dose)s, %(reaction)s, %(doctor)s)"""
        execute_data_query(self.connection, query, gg_injection)
    
    def update_gg_injection(self, gg_injection: dict):
        query = f"""UPDATE gamma_globulin_injections SET vac_date = %(vac_date)s,
                                            reason = %(reason)s,
                                            serial = %(serial)s, 
                                            dose = %(dose)s,
                                            reaction = %(reaction)s, 
                                            doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                        vac_date = %(old_vac_date)s"""
        execute_data_query(self.connection, query, gg_injection)

    def delete_gg_injection(self, gg_injection: dict):
        query = f"""DELETE FROM gamma_globulin_injections WHERE  medcard_num = %(medcard_num)s AND
                                                     vac_date = %(vac_date)s"""
        execute_data_query(self.connection, query, gg_injection)

    
    def get_mantoux_tests_by_medcard_num(self, medcard_num: int) -> list[MantouxTest]:
            query = f"""SELECT  * FROM mantoux_tests WHERE medcard_num = {medcard_num}  ORDER BY check_date"""
            selected_mantoux_tests = execute_read_query_all(self.connection, query)
            mantoux_tests = []
            for mantoux_test in selected_mantoux_tests:
                mantoux_tests.append(SerializationService.serialization_mantoux_test(mantoux_test))
            return mantoux_tests
    
    def get_mantoux_test_by_pk(self, mantoux_test_data: dict) -> MantouxTest:
        query = f"""SELECT * FROM mantoux_tests WHERE medcard_num = '{mantoux_test_data["medcard_num"]}' AND
                                                      check_date = '{mantoux_test_data["check_date"]}'"""
        mantoux_test = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_mantoux_test(mantoux_test)

    def add_new_mantoux_test(self, mantoux_test: dict):
        query = f"""INSERT INTO mantoux_tests (medcard_num, check_date, result) 
                         VALUES (%(medcard_num)s, %(check_date)s, %(result)s)"""
        execute_data_query(self.connection, query, mantoux_test)
    
    def update_mantoux_test(self, mantoux_test: dict):
        query = f"""UPDATE mantoux_tests SET check_date = %(check_date)s,
                                                         result = %(result)s
                    WHERE medcard_num = %(medcard_num)s AND
                          check_date = %(old_check_date)s"""
        execute_data_query(self.connection, query, mantoux_test)

    def delete_mantoux_test(self, mantoux_test: dict):
        query = f"""DELETE FROM mantoux_tests WHERE  medcard_num = %(medcard_num)s AND
                                                     check_date = %(check_date)s"""
        execute_data_query(self.connection, query, mantoux_test)

    def get_tub_vacs_by_medcard_num(self, medcard_num: int) -> list[TuberculosisVaccination]:
            query = f"""SELECT  * FROM tuberculosis_vaccinations WHERE medcard_num = {medcard_num} ORDER BY vac_date"""
            selected_tub_vacs = execute_read_query_all(self.connection, query)
            tub_vacs = []
            for tub_vac in selected_tub_vacs:
                tub_vacs.append(SerializationService.serialization_tub_vac(tub_vac))
            return tub_vacs
    
    def get_tub_vac_by_pk(self, tub_vac_data: dict) -> TuberculosisVaccination:
        query = f"""SELECT * FROM tuberculosis_vaccinations WHERE medcard_num = '{tub_vac_data["medcard_num"]}' AND
                                                                  vac_date = '{tub_vac_data["vac_date"]}'"""
        tub_vac = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_tub_vac(tub_vac)

    def add_new_tub_vac(self, tub_vac: dict):
        query = f"""INSERT INTO tuberculosis_vaccinations (medcard_num, vac_date, serial, dose, doctor) 
                         VALUES (%(medcard_num)s, %(vac_date)s, %(serial)s, %(dose)s, %(doctor)s)"""
        execute_data_query(self.connection, query, tub_vac)
    
    def update_tub_vac(self, tub_vac: dict):
        query = f"""UPDATE tuberculosis_vaccinations SET vac_date = %(vac_date)s,
                                            serial = %(serial)s, 
                                            dose = %(dose)s,
                                            doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            vac_date = %(old_vac_date)s"""
        execute_data_query(self.connection, query, tub_vac)

    def delete_tub_vac(self, tub_vac: dict):
        query = f"""DELETE FROM tuberculosis_vaccinations WHERE  medcard_num = %(medcard_num)s AND
                                                     vac_date = %(vac_date)s"""
        execute_data_query(self.connection, query, tub_vac)

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


    def get_screenings_by_medcard_num(self, medcard_num: int) -> list[Screening]:
            query = f"""SELECT  * FROM screenings WHERE medcard_num = {medcard_num} ORDER BY age"""
            selected_screenings = execute_read_query_all(self.connection, query)
            screenings = []
            for screening in selected_screenings:
                screenings.append(SerializationService.serialization_screening(screening))
            return screenings
    
    def get_screening_by_pk(self, screening_data: dict) -> Screening:
        query = f"""SELECT * FROM screenings WHERE medcard_num = '{screening_data["medcard_num"]}' AND
                                                                  age = '{screening_data["age"]}'"""
        screening = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_screening(screening)

    def add_new_screening(self, screening: dict):
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
    
    def update_screening(self, screening: dict):
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

    def delete_screening(self, screening: dict):
        query = f"""DELETE FROM screenings WHERE medcard_num = %(medcard_num)s AND
                                                age = %(age)s"""
        execute_data_query(self.connection, query, screening)

