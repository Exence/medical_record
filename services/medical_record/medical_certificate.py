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

from models.medical_certificate import MedicalCertificate
from models.user import User
from models.exceptions import exception_403


class MedicalCertificateService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_medical_certificates_by_medcard_num(self, user: User, medcard_num: int) -> list[MedicalCertificate]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT * FROM medical_certificates WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_medical_certificates = execute_read_query_all(self.connection, query)
            medical_certificates = []
            for medical_certificate in selected_medical_certificates:
                medical_certificates.append(SerializationService.serialization_medical_certificate(medical_certificate))
            
            return medical_certificates
        raise exception_403 from None
    
    def get_medical_certificate_by_pk(self, user: User, medical_certificate_data: dict) -> MedicalCertificate:
        if check_user_access(user=user, medcard_num=medical_certificate_data["medcard_num"]):
            query = f"""SELECT * FROM medical_certificates WHERE    medcard_num = '{medical_certificate_data["medcard_num"]}' AND
                                                                    disease = '{medical_certificate_data["disease"]}' AND
                                                                    cert_date = '{medical_certificate_data["cert_date"]}'"""
            medical_certificate = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_medical_certificate(medical_certificate)
        raise exception_403 from None
    
    def add_new_medical_certificate(self, user: User, medical_certificate: dict):
        if check_user_access(user=user, medcard_num=medical_certificate["medcard_num"]):
            if not medical_certificate["sport_exemption_date"]:
                medical_certificate["sport_exemption_date"] = None
            if not medical_certificate["vac_exemption_date"]:
                medical_certificate["vac_exemption_date"] = None

            query = f"""INSERT INTO medical_certificates (medcard_num, disease, cert_date, start_date, end_date, infection_contact, sport_exemption_date, vac_exemption_date, doctor) 
                    VALUES (%(medcard_num)s, %(disease)s, %(cert_date)s, %(start_date)s, %(end_date)s, %(infection_contact)s, %(sport_exemption_date)s, %(vac_exemption_date)s, %(doctor)s)"""
            execute_data_query(self.connection, query, medical_certificate)
        else:
            raise exception_403 from None

    def update_medical_certificate(self, user: User, medical_certificate: dict):
        if check_user_access(user=user, medcard_num=medical_certificate["medcard_num"]):
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
        else:
            raise exception_403 from None

    def delete_medical_certificate(self, user: User, medical_certificate: dict):
        if check_user_access(user=user, medcard_num=medical_certificate["medcard_num"]):
            query = f"""DELETE FROM medical_certificates WHERE  medcard_num = %(medcard_num)s AND
                                                                disease = %(disease)s AND
                                                                cert_date = %(cert_date)s"""
            execute_data_query(self.connection, query, medical_certificate)
        else:
            raise exception_403 from None
