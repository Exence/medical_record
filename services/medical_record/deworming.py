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

from models.deworming import Deworming
from models.user import User
from models.exceptions import exception_403


class DewormingService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_dewormings_by_medcard_num(self, user: User, medcard_num: int) -> list[Deworming]:
        dewormings = []
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM dewormings WHERE medcard_num = {medcard_num} ORDER BY deworming_date"""
            selected_dewormings = execute_read_query_all(self.connection, query)
            for deworming in selected_dewormings:
                dewormings.append(SerializationService.serialization_deworming(deworming))         
            return dewormings
        raise exception_403 from None
    
    def get_deworming_by_pk(self, user: User, deworming_data: dict) -> Deworming:
        if check_user_access(user=user, medcard_num=deworming_data["medcard_num"]):
            query = f"""SELECT * FROM dewormings WHERE medcard_num = '{deworming_data["medcard_num"]}' AND
                                                            deworming_date = '{deworming_data["deworming_date"]}'"""
            deworming = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_deworming(deworming)        
        raise exception_403 from None

    def add_new_deworming(self, user: User, deworming: dict):
        if check_user_access(user=user, medcard_num=deworming["medcard_num"]):
            query = f"""INSERT INTO dewormings (medcard_num, deworming_date, result) 
                            VALUES (%(medcard_num)s, %(deworming_date)s, %(result)s)"""
            execute_data_query(self.connection, query, deworming)
        else:
            raise exception_403 from None
    
    def update_deworming(self, user: User, deworming: dict):
        if check_user_access(user=user, medcard_num=deworming["medcard_num"]):
            query = f"""UPDATE  dewormings SET deworming_date = %(deworming_date)s, 
                                            result = %(result)s
                        WHERE   medcard_num = %(medcard_num)s AND
                                deworming_date = %(old_deworming_date)s"""
            execute_data_query(self.connection, query, deworming)
        else:
            raise exception_403 from None

    def delete_deworming(self, user: User, deworming: dict):
        if check_user_access(user=user, medcard_num=deworming["medcard_num"]):
            query = f"""DELETE FROM dewormings WHERE  medcard_num = %(medcard_num)s AND
                                                    deworming_date = %(deworming_date)s"""
            execute_data_query(self.connection, query, deworming)
        else:
            raise exception_403 from None
