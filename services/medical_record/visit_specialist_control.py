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

from models.visit_specialist_control import VisitSpecialistControl


class VisitSpecialistControlService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

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
