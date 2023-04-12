from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class PastIllnessBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date = Field(...)
    diagnosis: str = Field(...)

class PastIllness(PastIllnessBase):
    class Config:
        orm_mode = True

class PastIllnessCreate(PastIllnessBase):
    pass