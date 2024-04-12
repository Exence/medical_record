from fastapi import (
    Form,
    HTTPException,
)
from pydantic import (
    BaseModel,
    validator,
)
import re


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class UserPK(BaseModel):
    kindergarten_num: int


class UserBase(UserPK):
    kindergarten_name: str
    surname: str
    name: str
    patronymic: str
    password_hash: str


class UserCreate(UserBase):
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


class UserUpdate(UserCreate):
    pass


class User(UserBase):

    class Config:
        orm_mode = True
