import re
from datetime import date
from decimal import Decimal
from enum import Enum
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class MedicalExaminationPeriodKind(str, Enum):
    FIRST = 'Перед поступлением в ясли-сад, детский сад'
    SECOND = 'За 1 год до школы'
    THIRD = 'Перед школой'
    
class HealthGroupKind(str, Enum):
    FIRST = 'I'
    SECOND = 'II'
    THIRD = 'III'
    FOURTH = 'IV'

class SportGroupKind(str, Enum):
    BASIC = 'Основная'
    EXERCISE_THERAPY = 'Лечебная'
class MedicalExaminationPK(BaseModel):
    medcard_num: int = Field(...)
    period: MedicalExaminationPeriodKind = Field(...)
class MedicalExaminationBase(MedicalExaminationPK):
    examination_date: date = Field(...)
    age: int | None
    height: Decimal = Field(...)
    weight: Decimal = Field(...)
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
    health_group: HealthGroupKind = Field(...)
    sport_group: SportGroupKind = Field(...)
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
    
class MedicalExaminationUpdate(MedicalExaminationCreate):
    prev_period: str = Field(...)
