import re
from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")

class TuberculosisVaccinationPK(BaseModel):
    medcard_num: int = Field(...)
    vac_date: date = Field(...)

class TuberculosisVaccinationBase(TuberculosisVaccinationPK):
    serial: str = Field(..., max_length=90)
    dose: float = Field(...)
    doctor: str = Field(..., max_length=200)

class TuberculosisVaccination(TuberculosisVaccinationBase):
    class Config:
        orm_mode = True

class TuberculosisVaccinationCreate(TuberculosisVaccinationBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value

class TuberculosisVaccinationUpdate(TuberculosisVaccinationCreate):
    prev_vac_date: date = Field(...)
