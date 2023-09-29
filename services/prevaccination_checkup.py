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

from models.prevaccination_checkup import PrevaccinationCheckup


class PrevaccinationCheckupService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_prevaccination_checkups_by_medcard_num(self, medcard_num: int) -> list[PrevaccinationCheckup]:
            query = f"""SELECT  * FROM prevaccination_checkups_view WHERE medcard_num = {medcard_num}"""
            selected_prevaccination_checkups = execute_read_query_all(self.connection, query)
            prevaccination_checkups = []
            for prevaccination_checkup in selected_prevaccination_checkups:
                prevaccination_checkups.append(SerializationService.serialization_prevaccination_checkup(prevaccination_checkup))
            return prevaccination_checkups
    
    def get_prevaccination_checkup_by_pk(self, prevaccination_checkup_data: dict) -> PrevaccinationCheckup:
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