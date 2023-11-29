import re

from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")

class PrevaccinationCheckupPK(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)

class PrevaccinationCheckupBase(PrevaccinationCheckupPK):
    age: int | None
    diagnosis: str = Field(...)
    report: str = Field(...)
    no_vac_date: date | None
    doctor: str = Field(..., max_length=200)

class PrevaccinationCheckup(PrevaccinationCheckupBase):
    vac_name_id: int = Field(...)
    
    class Config:
        orm_mode = True

class PrevaccinationCheckupCreate(PrevaccinationCheckupBase):
    vac_name_id: int = Field(...)

    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value
    
class PrevaccinationCheckupUpdate(PrevaccinationCheckupCreate):
    prev_examination_date: date = Field(...)
    
class PrevaccinationCheckupView(PrevaccinationCheckupBase):
    vac_name: str

    class Config:
        orm_mode = True
