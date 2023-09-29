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

from models.extra_classes import ExtraClass


class ExtraClassService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

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