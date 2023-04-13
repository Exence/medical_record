from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class OralSanationBase(BaseModel):
    medcard_num: int = Field(...)
    sanation_date: date = Field(...)
    dental_result: str = Field(...)
    sanation_result: str = Field(...)

class OralSanation(OralSanationBase):
    class Config:
        orm_mode = True

class OralSanationCreate(OralSanationBase):
    pass
