from fastapi import Depends
from typing import Any

from database import (
    get_connection,
    execute_read_query_all,
    execute_read_query_first,
)

from models.vac_name import VacName

from services.serialization import SerializationService


def get_vac_names_by_type(connection: Any, vac_type: str) -> list[VacName]:
    query = f"""SELECT * FROM vac_names WHERE vac_type='{vac_type}'"""
    selected_vac_names = execute_read_query_all(connection, query)
    vac_names = []
    for vac_name in selected_vac_names:
        vac_names.append(SerializationService.serialization_vac_name(vac_name))
    return vac_names


class VacNameSevice():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def get_all_vac_names(self):
        query = f"""SELECT * FROM vac_names ORDER BY vac_type DESC, name"""
        selected_vac_names = execute_read_query_all(self.connection, query)
        vac_names = []
        for vac_name in selected_vac_names:
            vac_names.append(SerializationService.serialization_vac_name(vac_name))
        return vac_names
    
    def get_vac_name_by_id(self, id: int) -> VacName:
        query = f"""SELECT * FROM vac_names WHERE id = {id}"""
        vac_name = execute_read_query_first(self.connection, query)
        return SerializationService.serialization_vac_name(vac_name)
