from datetime import date
from enum import Enum
from pydantic import (
    BaseModel,
    Field,
)


class MantouxTestResultKind(str, Enum):
    NEGATIVE = 'Отрицательно'
    DOUBTFUL = 'Сомнительно'
    POSITIVELY = 'Положительно'


class MantouxTestPK(BaseModel):
    medcard_num: int = Field(...)
    check_date: date = Field(...)


class MantouxTestBase(MantouxTestPK):
    result: MantouxTestResultKind = Field(...)


class MantouxTest(MantouxTestBase):
    class Config:
        orm_mode = True


class MantouxTestCreate(MantouxTestBase):
    pass


class MantouxTestUpdate(MantouxTestCreate):
    prev_check_date: date = Field(...)
