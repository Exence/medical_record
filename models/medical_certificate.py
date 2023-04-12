from datetime import date
from fastapi import (
    HTTPException,
)
from pydantic import (
    BaseModel,
    Field,
    validator,
)
import re


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")

class MedicalCertificateBase(BaseModel):
    medcard_num: int = Field(...)
    disease: str = Field(..., max_length=250)
    cert_date: date = Field(...)
    start_date: date  = Field(...)
    end_date: date = Field(...)
    infection_contact: bool = Field(...)
    sport_exemption_date: date | None
    vac_exemption_date: date | None
    doctor: str = Field(..., max_length=200)

class MedicalCertificate(MedicalCertificateBase):
    class Config:
        orm_mode = True

class MedicalCertificateCreate(MedicalCertificateBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value