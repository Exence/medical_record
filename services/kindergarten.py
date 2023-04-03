from typing import Any


def get_kindergarten_num_by_name(cursor: Any, kindergarten_name: str) -> int:
    query = f"""SELECT number FROM kindergartens WHERE name = '{kindergarten_name}'"""
    cursor.execute(query)
    return cursor.fetchone()[0]

def get_kindergarten_name_by_num(cursor: Any, kindergarten_num: int) -> str:
    query = f"""SELECT name FROM kindergartens WHERE number = '{kindergarten_num}'"""
    cursor.execute(query)
    return cursor.fetchone()[0]