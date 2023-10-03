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

from models.dispensary import Dispensary
from models.user import User
from models.exceptions import exception_403


class DispensaryService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_dispensaryes_by_medcard_num(self, user: User, medcard_num: int) -> list[Dispensary]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM dispensaryes WHERE medcard_num = {medcard_num} ORDER BY start_date"""
            selected_dispensaryes = execute_read_query_all(self.connection, query)
            dispensaryes = []
            for dispensary in selected_dispensaryes:
                dispensaryes.append(SerializationService.serialization_dispensary(dispensary))
            return dispensaryes
        raise exception_403 from None
    
    def get_dispensary_by_pk(self, user: User, dispensary_data: dict) -> Dispensary:
        if check_user_access(user=user, medcard_num=dispensary_data["medcard_num"]):
            query = f"""SELECT * FROM dispensaryes WHERE medcard_num = '{dispensary_data["medcard_num"]}' AND
                                                            start_date = '{dispensary_data["start_date"]}'"""
            dispensary = execute_read_query_first(self.connection, query)

            return SerializationService.serialization_dispensary(dispensary)
        raise exception_403 from None

    def add_new_dispensary(self, user: User, dispensary: dict):
        if check_user_access(user=user, medcard_num=dispensary["medcard_num"]):
            if not dispensary["end_date"]:
                dispensary["end_date"] = None

            query = f"""INSERT INTO dispensaryes (medcard_num, start_date, end_date, diagnosis, specialist, end_reason) 
                            VALUES (%(medcard_num)s, %(start_date)s, %(end_date)s, %(diagnosis)s, %(specialist)s, %(end_reason)s)"""
            execute_data_query(self.connection, query, dispensary)
        else:
            raise exception_403 from None
    
    def update_dispensary(self, user: User, dispensary: dict):
        if check_user_access(user=user, medcard_num=dispensary["medcard_num"]):
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
        else:
            raise exception_403 from None

    def delete_dispensary(self, user: User, dispensary: dict):
        if check_user_access(user=user, medcard_num=dispensary["medcard_num"]):
            query = f"""DELETE FROM dispensaryes WHERE  medcard_num = %(medcard_num)s AND
                                                            start_date = %(start_date)s"""
            execute_data_query(self.connection, query, dispensary)
        else:
            raise exception_403 from None
