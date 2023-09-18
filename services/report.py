from datetime import date
from fastapi import Depends
from typing import Any

from database import (
    get_connection,
    execute_read_query_all,
)

from models.child import ChildToShow
from models.tub_diagnostic import TubDiagnostic
from models.vaccination import VacReport

from services.serialization import SerializationService


class ReportService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_childrens_by_mantoux_test_result(self, mantoux_test_result: str, start_date: date, end_date:date) -> list[ChildToShow]:
        query = f"""SELECT DISTINCT * FROM all_childrens AS ac
                      JOIN mantoux_tests AS mt
                        ON ac.medcard_num = mt.medcard_num
                     WHERE mt.result = '{mantoux_test_result}' AND
                           mt.check_date BETWEEN '{start_date}' AND '{end_date}'"""
        selected_childrens = execute_read_query_all(self.connection, query)
        childrens = []
        for child in selected_childrens:
            childrens.append(SerializationService.serialization_child_to_show(child))
        return childrens


    def get_childrens_by_vaccine(self, vac: VacReport) -> list[ChildToShow]:
        query = f"""SELECT DISTINCT * FROM all_childrens AS ac
                      JOIN vaccinations AS v
                        ON ac.medcard_num = v.medcard_num
                     WHERE v.vac_name_id = '{vac.vac_name_id}' AND
                           v.vac_type = '{vac.vac_type}'"""
        selected_childrens = execute_read_query_all(self.connection, query)
        childrens = []
        for child in selected_childrens:
            childrens.append(SerializationService.serialization_child_to_show(child))
        return childrens
    