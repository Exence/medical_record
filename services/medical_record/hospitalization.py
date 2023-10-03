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

from models.hospitalization import Hospitalization
from models.user import User
from models.exceptions import exception_403


class HospitalizationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_hospitalizations_by_medcard_num(self, user: User, medcard_num: int) -> list[Hospitalization]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM hospitalizations WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_hospitalizations = execute_read_query_all(self.connection, query)
            hospitalizations = []
            for hospitalization in selected_hospitalizations:
                hospitalizations.append(SerializationService.serialization_hospitalization(hospitalization))
            return hospitalizations
        raise exception_403 from None
    
    def get_hospitalization_by_pk(self, user: User, hospitalization_data: dict) -> Hospitalization:
        if check_user_access(user=user, medcard_num=hospitalization_data["medcard_num"]):
            query = f"""SELECT * FROM hospitalizations WHERE medcard_num = '{hospitalization_data["medcard_num"]}' AND
                                                            start_date = '{hospitalization_data["start_date"]}'"""
            hospitalization = execute_read_query_first(self.connection, query)

            return SerializationService.serialization_hospitalization(hospitalization)
        raise exception_403 from None

    def add_new_hospitalization(self, user: User, hospitalization: dict):
        if check_user_access(user=user, medcard_num=hospitalization["medcard_num"]):
            if not hospitalization["end_date"]:
                hospitalization["end_date"] = None

            query = f"""INSERT INTO hospitalizations (medcard_num, start_date, end_date, diagnosis, founding) 
                            VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(founding)s)"""
            execute_data_query(self.connection, query, hospitalization)
        raise exception_403 from None
    
    def update_hospitalization(self, user: User, hospitalization: dict):
        if check_user_access(user=user, medcard_num=hospitalization["medcard_num"]):
            if not hospitalization["end_date"]:
                hospitalization["end_date"] = None

            query = f"""UPDATE  hospitalizations SET start_date = %(start_date)s, 
                                                    end_date = %(end_date)s, 
                                                    diagnosis = %(diagnosis)s,
                                                    founding = %(founding)s
                        WHERE   medcard_num = %(medcard_num)s AND
                                start_date = %(old_start_date)s"""
            execute_data_query(self.connection, query, hospitalization)
        else:
            raise exception_403 from None

    def delete_hospitalization(self, user: User, hospitalization: dict):
        if check_user_access(user=user, medcard_num=hospitalization["medcard_num"]):
            query = f"""DELETE FROM hospitalizations WHERE  medcard_num = %(medcard_num)s AND
                                                            start_date = %(start_date)s"""
            execute_data_query(self.connection, query, hospitalization)
        else:
            raise exception_403 from None
