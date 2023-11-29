from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class OralSanationPK(BaseModel):
    medcard_num: int = Field(...)
    sanation_date: date = Field(...)

class OralSanationBase(OralSanationPK):
    dental_result: str = Field(...)
    sanation_result: str = Field(...)

class OralSanation(OralSanationBase):
    class Config:
        orm_mode = True

class OralSanationCreate(OralSanationBase):
    pass

class OralSanationUpdate(OralSanationCreate):
    prev_sanation_date: date = Field(...)
