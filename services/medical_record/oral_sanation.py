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

from models.oral_sanation import OralSanation
from models.user import User
from models.exceptions import exception_403


class OralSanationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_oral_sanations_by_medcard_num(self, user: User, medcard_num: int) -> list[OralSanation]:
        if check_user_access(user=user, medcard_num=medcard_num):
            query = f"""SELECT  * FROM oral_sanations WHERE medcard_num = {medcard_num} ORDER BY sanation_date"""
            selected_oral_sanations = execute_read_query_all(self.connection, query)
            oral_sanations = []
            for oral_sanation in selected_oral_sanations:
                oral_sanations.append(SerializationService.serialization_oral_sanation(oral_sanation))
            return oral_sanations
        raise exception_403 from None
    
    def get_oral_sanation_by_pk(self, user: User, oral_sanation_data: dict) -> OralSanation:
        if check_user_access(user=user, medcard_num=oral_sanation_data["medcard_num"]):
            query = f"""SELECT * FROM oral_sanations WHERE medcard_num = '{oral_sanation_data["medcard_num"]}' AND
                                                        sanation_date = '{oral_sanation_data["sanation_date"]}'"""
            oral_sanation = execute_read_query_first(self.connection, query)
            return SerializationService.serialization_oral_sanation(oral_sanation)
        raise exception_403 from None

    def add_new_oral_sanation(self, user: User, oral_sanation: dict):
        if check_user_access(user=user, medcard_num=oral_sanation["medcard_num"]):
            query = f"""INSERT INTO oral_sanations (medcard_num, sanation_date, dental_result, sanation_result) 
                            VALUES (%(medcard_num)s, %(sanation_date)s, %(dental_result)s, %(sanation_result)s)"""
            execute_data_query(self.connection, query, oral_sanation)
        else:
            raise exception_403 from None
    
    def update_oral_sanation(self, user: User, oral_sanation: dict):
        if check_user_access(user=user, medcard_num=oral_sanation["medcard_num"]):
            query = f"""UPDATE  oral_sanations SET sanation_date = %(sanation_date)s, 
                                                dental_result = %(dental_result)s,
                                                sanation_result = %(sanation_result)s
                        WHERE   medcard_num = %(medcard_num)s AND
                                sanation_date = %(old_sanation_date)s"""
            execute_data_query(self.connection, query, oral_sanation)
        else:
            raise exception_403 from None

    def delete_oral_sanation(self, user: User, oral_sanation: dict):
        if check_user_access(user=user, medcard_num=oral_sanation["medcard_num"]):
            query = f"""DELETE FROM oral_sanations WHERE  medcard_num = %(medcard_num)s AND
                                                    sanation_date = %(sanation_date)s"""
            execute_data_query(self.connection, query, oral_sanation)
        else:
            raise exception_403 from None
