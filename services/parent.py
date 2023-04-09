from typing import Any

from database import execute_read_query_first
from models.parent import (
    Parent,
    ParentCreate,)


def select_parent_id(cursor: Any, parent: ParentCreate) -> int:
    query = f"""SELECT id FROM parents 
            WHERE   surname = '{parent.surname}' AND 
                    name = '{parent.name}' AND 
                    patronymic = '{parent.patronymic}' AND 
                    birthday_year = {parent.birthday_year} AND 
                    education = '{parent.education}' AND 
                    phone_num = {parent.phone_num}
            """
    cursor.execute(query)
    return cursor.fetchone()[0]

def get_parent_by_id(connection: Any, parent_id: int) -> Parent:
    query = f"""SELECT * FROM parents WHERE id = {parent_id}"""
    parent = execute_read_query_first(connection, query)
    return Parent(
        id=parent[0],
        surname=parent[1],
        name=parent[2],
        patronymic=parent[3],
        birthday_year=parent[4],
        education=parent[5],
        phone_num=parent[6]
    )
