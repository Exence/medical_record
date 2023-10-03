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

from models.vaccination import Vaccination
from models.user import User
from models.exceptions import exception_403


class VaccinationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def add_new_vaccination(self, user: User, vaccination: dict):
        if check_user_access(user=user, medcard_num=vaccination["medcard_num"]):
            query = f"""INSERT INTO vaccinations (medcard_num, vac_name_id, vac_type, vac_date, serial, dose, introduction_method, reaction, doctor) 
                            VALUES (%(medcard_num)s, %(vac_name_id)s, %(vac_type)s, %(vac_date)s, %(serial)s, %(dose)s, %(introduction_method)s, %(reaction)s, %(doctor)s)"""
            execute_data_query(self.connection, query, vaccination)
        else:
            raise exception_403 from None
    
    def update_vaccination(self, user: User, vaccination: dict):
        if check_user_access(user=user, medcard_num=vaccination["medcard_num"]):
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
        else:
            raise exception_403 from None

    def delete_vaccination(self, user: User, vaccination: dict):
        if check_user_access(user=user, medcard_num=vaccination["medcard_num"]):
            query = f"""DELETE FROM vaccinations WHERE  medcard_num = %(medcard_num)s AND
                                                        vac_name_id = %(vac_name_id)s AND
                                                        vac_type = %(vac_type)s"""
            execute_data_query(self.connection, query, vaccination)
        else:
            raise exception_403 from None

    
    def get_prof_vaccinations_by_medcard_num(self, user: User, medcard_num: int) -> list[Vaccination]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM prof_vaccinations WHERE medcard_num = {medcard_num}"""
            selected_prof_vaccinations = execute_read_query_all(self.connection, query)
            prof_vaccinations = []
            for prof_vaccination in selected_prof_vaccinations:
                prof_vaccinations.append(SerializationService.serialization_vaccination(prof_vaccination))
            return prof_vaccinations
        raise exception_403 from None
    
    def get_prof_vaccination_by_pk(self, user: User, prof_vaccination_data: dict) -> Vaccination:
        if check_user_access(user=user, medcard_num=prof_vaccination_data["medcard_num"]):
            query = f"""SELECT * FROM prof_vaccinations WHERE medcard_num = '{prof_vaccination_data["medcard_num"]}' AND
                                                              vac_name_id = '{prof_vaccination_data["vac_name_id"]}' AND
                                                              vac_type = '{prof_vaccination_data["vac_type"]}'"""
            prof_vaccination = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_vaccination(prof_vaccination)
        raise exception_403 from None
    

    def get_epid_vaccinations_by_medcard_num(self, user: User, medcard_num: int) -> list[Vaccination]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM epid_vaccinations WHERE medcard_num = {medcard_num}"""
            selected_epid_vaccinations = execute_read_query_all(self.connection, query)
            epid_vaccinations = []
            for epid_vaccination in selected_epid_vaccinations:
                epid_vaccinations.append(SerializationService.serialization_vaccination(epid_vaccination))
            return epid_vaccinations
        raise exception_403 from None
    
    def get_epid_vaccination_by_pk(self, user: User, epid_vaccination_data: dict) -> Vaccination:
        if check_user_access(user=user, medcard_num=epid_vaccination_data["medcard_num"]):
            query = f"""SELECT * FROM epid_vaccinations WHERE medcard_num = '{epid_vaccination_data["medcard_num"]}' AND
                                                              vac_name_id = '{epid_vaccination_data["vac_name_id"]}' AND
                                                              vac_type = '{epid_vaccination_data["vac_type"]}'"""
            epid_vaccination = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_vaccination(epid_vaccination)
        raise exception_403 from None
