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

from models.gg_injection import GammaGlobulinInjection
from models.user import User
from models.exceptions import exception_403


class GammaGlobulinInjectionService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_gg_injections_by_medcard_num(self, user: User, medcard_num: int) -> list[GammaGlobulinInjection]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM gamma_globulin_injections WHERE medcard_num = {medcard_num}  ORDER BY vac_date"""
            selected_gg_injections = execute_read_query_all(self.connection, query)
            gg_injections = []
            for gg_injection in selected_gg_injections:
                gg_injections.append(SerializationService.serialization_gg_injection(gg_injection))
            return gg_injections
        raise exception_403 from None
    
    def get_gg_injection_by_pk(self, user: User, gg_injection_data: dict) -> GammaGlobulinInjection:
        if check_user_access(user=user, medcard_num=gg_injection_data["medcard_num"]):
            query = f"""SELECT * FROM gamma_globulin_injections WHERE medcard_num = '{gg_injection_data["medcard_num"]}' AND
                                                                    vac_date = '{gg_injection_data["vac_date"]}'"""
            gg_injection = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_gg_injection(gg_injection)
        raise exception_403 from None

    def add_new_gg_injection(self, user: User, gg_injection: dict):
        if check_user_access(user=user, medcard_num=gg_injection["medcard_num"]):
            query = f"""INSERT INTO gamma_globulin_injections (medcard_num, vac_date, reason, serial, dose, reaction, doctor) 
                            VALUES (%(medcard_num)s, %(vac_date)s, %(reason)s, %(serial)s, %(dose)s, %(reaction)s, %(doctor)s)"""
            execute_data_query(self.connection, query, gg_injection)
        raise exception_403 from None
    
    def update_gg_injection(self, user: User, gg_injection: dict):
        if check_user_access(user=user, medcard_num=gg_injection["medcard_num"]):
            query = f"""UPDATE gamma_globulin_injections SET vac_date = %(vac_date)s,
                                                reason = %(reason)s,
                                                serial = %(serial)s, 
                                                dose = %(dose)s,
                                                reaction = %(reaction)s, 
                                                doctor = %(doctor)s
                        WHERE   medcard_num = %(medcard_num)s AND
                            vac_date = %(old_vac_date)s"""
            execute_data_query(self.connection, query, gg_injection)

    def delete_gg_injection(self, user: User, gg_injection: dict):
        if check_user_access(user=user, medcard_num=gg_injection["medcard_num"]):
            query = f"""DELETE FROM gamma_globulin_injections WHERE  medcard_num = %(medcard_num)s AND
                                                        vac_date = %(vac_date)s"""
            execute_data_query(self.connection, query, gg_injection)
        raise exception_403 from None
