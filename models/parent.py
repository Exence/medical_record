import re

from enum import Enum
from fastapi import (
    HTTPException,
)
from pydantic import (
    BaseModel,
    Field,
    validator,
)


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class ParentType(str, Enum):
    MOTHER = 'mother'
    FATHER = 'father'

class ParentTypeRequest(BaseModel):
    parent_type: ParentType

class ParentPK(BaseModel):
    id: int = Field(...)

class ParentBase(BaseModel):
    surname: str = Field(..., max_length=150)
    name: str = Field(..., max_length=150)
    patronymic: str = Field(..., max_length=150)
    birthday_year: int = Field(..., gt=1900)
    education: str = Field(...)
    phone_num: int = Field(..., gt=80000000000, lt=90000000000)


class Parent(ParentPK, ParentBase):
    class Config:
        orm_mode = True


class ParentCreate(ParentBase):
    parent_type: ParentType = Field(...)

class ParentUpdate(ParentPK, ParentCreate):
    pass

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

    @validator("education")
    def validate_education(cls, value):
        if not value in ['б/обр.', 'н/ср.', 'ср.', 'ср.-спец.', 'н/высш.', 'высш.']:
            raise HTTPException(
                status_code=422, detail="Education should be in ['б/обр.', 'н/ср.', 'ср.', 'ср.-спец.', 'н/высш.', 'высш.']"
            )
        return value

    def to_tuple(self):
        return (self.surname, self.name, self.patronymic, self.birthday_year, self.education, self.phone_num, )
