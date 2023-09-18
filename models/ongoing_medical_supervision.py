import re
from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")

class OngoingMedicalSupervisionBase(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)
    examination_data: str = Field(...)
    diagnosis: str = Field(...)
    prescription: str | None
    doctor: str = Field(..., max_length=200)

class OngoingMedicalSupervision(OngoingMedicalSupervisionBase):
    class Config:
        orm_mode = True

class OngoingMedicalSupervisionCreate(OngoingMedicalSupervisionBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value