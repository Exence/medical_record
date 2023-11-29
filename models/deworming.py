from datetime import date
from enum import Enum
from pydantic import (
    BaseModel,
    Field,
)


class dewormingResultKind(str, Enum):
    POSITIVELY = 'Положительно'
    NEGATIVE = 'Отрицательно'


class DewormingPK(BaseModel):
    medcard_num: int = Field(...)
    deworming_date: date = Field(...)
class DewormingBase(DewormingPK):    
    result: dewormingResultKind = Field(...)

class Deworming(DewormingBase):
    class Config:
        orm_mode = True

class DewormingCreate(DewormingBase):
    pass

class DewormingUpdate(DewormingCreate):
    prev_deworming_date: date = Field(...)
