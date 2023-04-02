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

class UserBase(BaseModel):
    login: str
    surname: str
    name: str
    patronymic: str
    access_level: str
    kindergarten_num: int


class UserCreate(UserBase):
    password: str

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
    
    @validator("access_level")
    def validate_access_level(cls, value):
        if value not in ['db_admin', 'admin', 'user']:
            raise HTTPException(
                status_code=422, detail="access_level is not valid"
            )
        return value


class User(UserBase):
    password_hash: str
    kindergarten_name: str
    
    class Config:
        orm_mode = True


class CreateUserForm(BaseModel):
    surname: str 
    name: str
    patronymic: str
    login: str
    access_level: str
    kindergarten_name: str
    password: str

    @classmethod
    def as_form(
        cls,
        surname: str = Form(...),
        name: str = Form(...),
        patronymic: str = Form(...),
        login: str = Form(...),
        access_level: str = Form(...),
        kindergarten_name: str = Form(...),
        password: str = Form(...),
    ):
        return cls(surname = surname,
                    name = name,
                    patronymic = patronymic,
                    login = login,
                    access_level = access_level,
                    kindergarten_name = kindergarten_name,
                    password = password
                    )

