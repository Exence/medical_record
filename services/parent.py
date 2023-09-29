import psycopg2

from fastapi import (
    Depends,
)
from typing import Any

from database import (
    get_connection,
    execute_data_query,
    execute_read_query_first,
    execute_read_query_all,
)

from models.parent import (
    Parent,
    ParentCreate,)


def create_parent_tranzaction(connection: Any, parent: dict) -> bool:
    try:
        cursor = connection.cursor()
        query = f"""INSERT INTO parents (surname, name, patronymic, birthday_year, education, phone_num)
                    VALUES (%(surname)s, %(name)s, %(patronymic)s, %(birthday_year)s, %(education)s, %(phone_num)s)"""  
        cursor.execute(query, parent)
        query = f"""SELECT id FROM parents 
            WHERE   surname = '{parent["surname"]}' AND 
                    name = '{parent["name"]}' AND 
                    patronymic = '{parent["patronymic"]}' AND 
                    birthday_year = {parent["birthday_year"]} AND 
                    education = '{parent["education"]}' AND 
                    phone_num = {parent["phone_num"]}
            """
        cursor.execute(query)
        parent_id = cursor.fetchone()[0]
        query = f"""UPDATE childrens SET {parent["parent_type"]}_id = {parent_id} WHERE medcard_num = {parent["medcard_num"]}"""
        cursor.execute(query)

        connection.commit()
        return parent_id
        
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
        connection.rollback()
        return None
    
    finally:
        if cursor:
            cursor.close()

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
    if not parent_id:
        return None
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

class ParentService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection
        
    def add_parent(self, parent: dict):
        return create_parent_tranzaction(self.connection, parent)
    
    
    def update_parent(self, parent: dict):
        query = f"""UPDATE parents SET  surname = %(surname)s,
                                        name = %(name)s,
                                        patronymic = %(patronymic)s,
                                        birthday_year = %(birthday_year)s,
                                        education = %(education)s,
                                        phone_num = %(phone_num)s
                    WHERE id = %(id)s"""
        execute_data_query(self.connection, query, parent)

    def delete_parent(self, parent_data: dict):
        query = f"DELETE FROM parents WHERE id = %(id)s"
        execute_data_query(self.connection, query, parent_data)
