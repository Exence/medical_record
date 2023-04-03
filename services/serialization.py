from typing import Any

from database import (
      execute_read_query_first,
      )

from models.child import (
    CreateChildForm,
    ChildCreate,
    )
from models.user import (
    User,
)
from models.parent import (
        ParentCreate,
)

from services.kindergarten import get_kindergarten_name_by_num


def serialization_user(connection: Any, user_data: tuple) -> User:
            cursor = connection.cursor()
            kindergarten_name = get_kindergarten_name_by_num(cursor, user_data[6])
            cursor.close()

            return User (
                login = user_data[0],
                surname = user_data[1],
                name = user_data[2],
                patronymic = user_data[3],
                password_hash = user_data[4],
                access_level = user_data[5],
                kindergarten_num = user_data[6],
                kindergarten_name = kindergarten_name
            )

def serialization_parent_to_create(parent_data: tuple) -> ParentCreate:
        return ParentCreate(
                surname=parent_data[0],
                name=parent_data[1],
                patronymic=parent_data[2],
                birthday_year=parent_data[3],
                education=parent_data[4],
                phone_num=parent_data[5])
                

def serialization_child_to_create(form_data: CreateChildForm, father_id: int, mother_id: int, kindergarten_num: int) -> ChildCreate:
        return (form_data.surname,
                form_data.name,
                form_data.patronymic,
                kindergarten_num,
                form_data.birthday,
                form_data.sex[0],
                form_data.group_num,
                form_data.address,
                form_data.clinic,
                'ДДУ',
                form_data.entering_date,
                father_id,
                mother_id,
                form_data.family_characteristics,
                form_data.family_microclimate,
                form_data.rest_and_class_opportunities,
                form_data.case_history,
        )
