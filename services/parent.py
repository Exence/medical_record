from typing import Any

from models.parent import ParentCreate


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
