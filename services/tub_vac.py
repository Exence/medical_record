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

from models.tub_vac import TuberculosisVaccination


class TuberculosisVaccinationService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_tub_vacs_by_medcard_num(self, medcard_num: int) -> list[TuberculosisVaccination]:
            query = f"""SELECT  * FROM tuberculosis_vaccinations WHERE medcard_num = {medcard_num} ORDER BY vac_date"""
            selected_tub_vacs = execute_read_query_all(self.connection, query)
            tub_vacs = []
            for tub_vac in selected_tub_vacs:
                tub_vacs.append(SerializationService.serialization_tub_vac(tub_vac))
            return tub_vacs
    
    def get_tub_vac_by_pk(self, tub_vac_data: dict) -> TuberculosisVaccination:
        query = f"""SELECT * FROM tuberculosis_vaccinations WHERE medcard_num = '{tub_vac_data["medcard_num"]}' AND
                                                                  vac_date = '{tub_vac_data["vac_date"]}'"""
        tub_vac = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_tub_vac(tub_vac)

    def add_new_tub_vac(self, tub_vac: dict):
        query = f"""INSERT INTO tuberculosis_vaccinations (medcard_num, vac_date, serial, dose, doctor) 
                         VALUES (%(medcard_num)s, %(vac_date)s, %(serial)s, %(dose)s, %(doctor)s)"""
        execute_data_query(self.connection, query, tub_vac)
    
    def update_tub_vac(self, tub_vac: dict):
        query = f"""UPDATE tuberculosis_vaccinations SET vac_date = %(vac_date)s,
                                            serial = %(serial)s, 
                                            dose = %(dose)s,
                                            doctor = %(doctor)s
                    WHERE   medcard_num = %(medcard_num)s AND
                            vac_date = %(old_vac_date)s"""
        execute_data_query(self.connection, query, tub_vac)

    def delete_tub_vac(self, tub_vac: dict):
        query = f"""DELETE FROM tuberculosis_vaccinations WHERE  medcard_num = %(medcard_num)s AND
                                                     vac_date = %(vac_date)s"""
        execute_data_query(self.connection, query, tub_vac)