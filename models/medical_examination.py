import re
from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class MedicalExaminationBase(BaseModel):
    medcard_num: int = Field(...)
    period: str = Field(...)
    examination_date: date = Field(...)
    age: int = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    complaints: str | None
    pediatrician: str | None
    orthopaedist: str | None
    ophthalmologist: str | None
    otolaryngologist: str | None
    dermatologist: str | None
    neurologist: str | None
    speech_therapist: str | None
    denta_surgeon: str | None
    psychologist: str | None
    other_doctors: str | None
    blood_test: str | None
    urine_analysis: str | None
    feces_analysis: str | None
    general_diagnosis: str | None
    physical_development: str | None
    mental_development: str | None
    health_group: str | None
    sport_group: str | None
    med_and_ped_conclusion: str | None
    recommendations: str | None

class MedicalExamination(MedicalExaminationBase):
    class Config:
        orm_mode = True

class MedicalExaminationCreate(MedicalExaminationBase):
    @validator("period")
    def validate_period(cls, value):
        if not value in ['Перед поступлением в ясли-сад, детский сад', 'За 1 год до школы', 'Перед школой']:
            raise HTTPException(
                status_code=422, detail="Period type should be in ['Перед поступлением в ясли-сад, детский сад', 'За 1 год до школы', 'Перед школой']"
            )
        return value
    
    @validator("health_group")
    def validate_health_group(cls, value):
        if not re.compile(r"^(I{1,3})$|^(IV)$").match(value):
            raise HTTPException(
                status_code=422, detail="Health group should be I-IV"
            )
        return value
