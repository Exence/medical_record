import re
from fastapi import (
    Form,
    HTTPException,
)
from pydantic import (
    BaseModel,
    Field,
    validator,
)
from datetime import date

from models.parent import Parent


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")
LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")




class ChildPK(BaseModel):
    medcard_num: int = Field(...)

class ParentsIds(BaseModel):
    father_id: int | None
    mother_id: int | None



class ChildBase(BaseModel):
    kindergarten_num: int = Field(..., gt=-1, lt=1000)
    surname: str = Field(..., max_length=150)
    name: str = Field(..., max_length=150)
    patronymic: str = Field(..., max_length=150)
    birthday: date = Field(...)
    sex: str = Field(..., max_length=1)
    group_num: int = Field(..., gt=0, lt=7)
    address: str = Field(..., max_length=250)
    clinic: str = Field(..., max_length=200)
    edu_type: str = Field(default='ДДУ', max_length=25)
    entering_date: date = Field(...)
    family_characteristics: str = Field(...)
    family_microclimate: str = Field(...)
    rest_and_class_opportunities: str = Field(...)
    case_history: str | None


class ChildWithParentsView(ChildPK, ChildBase):
    father_surname: str | None = Field(max_length=150)
    father_name: str | None = Field(max_length=150)
    father_patronymic: str | None = Field(max_length=150)
    father_birthday_year: int | None = Field(gt=1900)
    father_education: str | None = Field()
    father_phone_num: int | None = Field(gt=80000000000, lt=90000000000)
    mother_surname: str | None = Field(max_length=150)
    mother_name: str | None = Field(max_length=150)
    mother_patronymic: str | None = Field(..., max_length=150)
    mother_birthday_year: int | None = Field(..., gt=1900)
    mother_education: str | None = Field()
    mother_phone_num: int | None = Field(gt=80000000000, lt=90000000000)


class ChildEdit(ChildPK, ChildBase):
    kindergarten_num: str | None

    class Config:
        orm_mode = True


class Child(ChildPK, ChildBase, ParentsIds):
    father: Parent
    mother: Parent
    
    class Config:
        orm_mode = True


class ChildCreate(ChildBase):
    kindergarten_num: int = Field(..., gt=-1, lt=1000)

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Surname should contains only letters"
            )
        return value

    @validator("patronymic")
    def validate_patronymic(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Patronymic should contains only letters"
            )
        return value

    @validator("sex")
    def validate_sex(cls, value):
        if not value in ['М', 'Ж']:
            raise HTTPException(
                status_code=422, detail="Education should be in ['М', 'Ж']. Only one letter"
            )
        return value

    @validator("family_characteristics")
    def validate_family_characteristics(cls, value):
        if not value in ['Полная', 'Неполная']:
            raise HTTPException(
                status_code=422, detail="Family characteristics should be in ['Полная', 'Неполная']"
            )
        return value

    @validator("family_microclimate")
    def validate_family_microclimate(cls, value):
        if not value in ['Благоприятный', 'Неблагоприятный']:
            raise HTTPException(
                status_code=422, detail="Family microclimate should be in ['Благоприятный', 'Неблагоприятный']"
            )
        return value

    @validator("rest_and_class_opportunities")
    def validate_rest_and_class_opportunities(cls, value):
        if not value in ['Комната', 'Индивидуальный стол', 'Нет']:
            raise HTTPException(
                status_code=422, detail="Rest and class opportunities should be in ['Комната', 'Индивидуальный стол', 'Нет']"
            )
        return value


class CreateChildForm(BaseModel):
    surname: str
    name: str
    patronymic: str
    kindergarten_name: str
    birthday: date
    sex: str
    group_num: int
    address: str
    clinic: str
    entering_date: str
    father: str
    mother: str
    family_characteristics: str
    family_microclimate: str
    rest_and_class_opportunities: str
    case_history: str

    @classmethod
    def as_form(
        cls,
        surname: str = Form(...),
        name: str = Form(...),
        patronymic: str = Form(...),
        kindergarten_name: str = Form(...),
        birthday: date = Form(...),
        sex: str = Form(...),
        group_num: int = Form(...),
        address: str = Form(...),
        clinic: str = Form(...),
        entering_date: str = Form(...),
        father: str = Form(default=""),
        mother: str = Form(default=""),
        family_characteristics: str = Form(...),
        family_microclimate: str = Form(...),
        rest_and_class_opportunities: str = Form(...),
        case_history: str = Form(default="")
    ):
        return cls(surname=surname,
                   name=name,
                   patronymic=patronymic,
                   kindergarten_name=kindergarten_name,
                   birthday=birthday,
                   sex=sex,
                   group_num=group_num,
                   address=address,
                   clinic=clinic,
                   entering_date=entering_date,
                   father=father,
                   mother=mother,
                   family_characteristics=family_characteristics,
                   family_microclimate=family_microclimate,
                   rest_and_class_opportunities=rest_and_class_opportunities,
                   case_history=case_history
                   )


class ChildToShow(BaseModel):
    medcard_num: int
    surname: str
    name: str
    patronymic: str
    kindergarten_name: str
    birthday: date
    group_num: int
    father_surname: str | None
    father_name: str | None
    father_patronymic: str | None
    father_phone_num: int | None
    mother_surname: str | None
    mother_name: str | None
    mother_patronymic: str | None
    mother_phone_num: int | None
