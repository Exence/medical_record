from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class HospitalizationPK(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)


class HospitalizationBase(HospitalizationPK):
    end_date: date | None
    diagnosis: str = Field(...)
    founding: str = Field(..., max_length=200)


class Hospitalization(HospitalizationBase):
    class Config:
        orm_mode = True


class HospitalizationCreate(HospitalizationBase):
    pass


class HospitalizationUpdate(HospitalizationCreate):
    prev_start_date: date = Field(...)
