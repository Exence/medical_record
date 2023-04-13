from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class SpaTreatmentBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date | None
    diagnosis: str = Field(...)
    founding_specialization: str = Field(..., max_length=200)
    climatic_zone: str = Field(..., max_length=200)

class SpaTreatment(SpaTreatmentBase):
    class Config:
        orm_mode = True

class SpaTreatmentCreate(SpaTreatmentBase):
    pass