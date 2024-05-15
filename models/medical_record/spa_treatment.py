from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class SpaTreatmentPK(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)


class SpaTreatmentBase(SpaTreatmentPK):
    end_date: date | None
    diagnosis: str = Field(...)
    founding_specialization: str = Field(..., max_length=200)
    climatic_zone: str = Field(..., max_length=200)


class SpaTreatment(SpaTreatmentBase):
    class Config:
        orm_mode = True


class SpaTreatmentCreate(SpaTreatmentBase):
    pass


class SpaTreatmentUpdate(SpaTreatmentCreate):
    prev_start_date: date = Field(...)
