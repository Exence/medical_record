from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class HospitalizationBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date | None
    diagnosis: str = Field(...)
    founding: str = Field(..., max_length=200)

class Hospitalization(HospitalizationBase):
    class Config:
        orm_mode = True

class HospitalizationCreate(HospitalizationBase):
    pass