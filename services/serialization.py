from typing import Any

from database import (
      execute_read_query_first,
      )

from models.allergyes import Allergy
from models.child import (
    Child,
    CreateChildForm,
    ChildCreate,
    ChildShow
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
                
def serialization_child(child_data: tuple) -> Child:
        return Child(
                medcard_num=child_data[0],
                surname=child_data[1],
                name=child_data[2],
                patronymic=child_data[3],
                kindergarten_num=child_data[4],
                birthday=child_data[5],
                sex=child_data[6],
                group_num=child_data[7],
                address=child_data[8],
                clinic=child_data[9],
                edu_type=child_data[10],
                entering_date=child_data[11],
                father_id=child_data[12],
                mother_id=child_data[13],
                family_characteristics=child_data[14],
                family_microclimate=child_data[15],
                rest_and_class_opportunities=child_data[16],
                case_history=child_data[17]
        )

def serialization_child_to_create(form_data: CreateChildForm, father_id: int, mother_id: int, kindergarten_num: int) -> tuple:
        return [(form_data.surname,
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
        )]

def serialization_child_to_show(child_data: tuple) -> ChildShow:
        return ChildShow(
                medcard_num = child_data[0],
                surname = child_data[1],
                name = child_data[2],
                patronymic = child_data[3],
                kindergarten_name = child_data[4],
                birthday = child_data[5],
                group_num = child_data[6],
                father_surname = child_data[7],
                father_name = child_data[8],
                father_patronymic = child_data[9],
                father_phone_num = child_data[10],
                mother_surname = child_data[11],
                mother_name = child_data[12],
                mother_patronymic = child_data[13],
                mother_phone_num = child_data[14]) 

def serialization_allergy(allergy_data: tuple) -> Allergy:
        return Allergy (
                medcard_num=allergy_data[0],
                allergen=allergy_data[1],
                allergy_type=allergy_data[2],
                start_age=allergy_data[3],
                reaction_type=allergy_data[4],
                diagnosis_date=allergy_data[5],
                note=allergy_data[6]
        )

def serialization_allergy_to_create(medcard_num: int, allergy: dict):
        return [(
                medcard_num, 
                allergy["allergen"],
                allergy["allergy_type"],
                allergy["start_age"],
                allergy["reaction_type"],
                allergy["diagnosis_date"],
                allergy["note"],
                
        )]
