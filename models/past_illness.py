from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class PastIllnessPK(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    diagnosis: str = Field(...)


class PastIllnessBase(PastIllnessPK):
    end_date: date = Field(...)


class PastIllness(PastIllnessBase):
    class Config:
        orm_mode = True


class PastIllnessCreate(PastIllnessBase):
    pass


class PastIllnessUpdate(PastIllnessCreate):
    prev_start_date: date = Field(...)
    prev_diagnosis: str = Field(...)
