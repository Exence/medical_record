from decimal import Decimal
from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class ScreeningPK(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)


class ScreeningBase(ScreeningPK):
    age: int | None
    questionnaire_test: str = Field(...)
    height: Decimal = Field(...)
    weight: Decimal = Field(...)
    physical_development: str | None
    blood_pressures: str | None
    carriage: str | None
    foot_condition: str | None
    sight_od: Decimal | None
    sight_os: Decimal | None
    visual_acuity: str | None
    malinovsky_test: str | None
    binocular_vision: str | None
    hearing_acuteness: str | None
    dynammetry_left: Decimal | None
    dynammetry_right: Decimal | None
    physical_fitness: str | None
    protein_in_urine: str | None
    glucose_in_urine: str | None
    biological_age: str | None
    speech_defects: bool | None
    kern_test: int | None
    neurotic_disorders: bool | None
    thinking_and_speech_disorders: bool | None
    motor_development_disorders: bool | None
    attention_and_memory_disorders: bool | None
    social_contacts_disorders: bool | None
    diseases_for_year: int | None


class Screening(ScreeningBase):
    class Config:
        orm_mode = True


class ScreeningCreate(ScreeningBase):
    @validator("questionnaire_test")
    def validate_questionnaire_test(cls, value):
        if not (value is None or value in ['Норма', 'Отклонение']):
            raise HTTPException(
                status_code=422, detail="Questionnaire test should be in ['Норма', 'Отклонение']"
            )
        return value

    @validator("physical_development")
    def validate_physical_development(cls, value):
        if not (value is None or value in ['Нормальное', 'Низкий рост', 'Дефицит массы', 'Избыток массы']):
            raise HTTPException(
                status_code=422, detail="Physical development test should be in ['Нормальное', 'Низкий рост', 'Дефицит массы', 'Избыток массы']"
            )
        return value

    @validator("carriage")
    def validate_carriage(cls, value):
        if not (value is None or value in ['Нормальная', 'Незначительные отклонения', 'Значительные нарушения']):
            raise HTTPException(
                status_code=422, detail="Carriage should be in ['Нормальная', 'Незначительные отклонения', 'Значительные нарушения']"
            )
        return value

    @validator("foot_condition")
    def validate_foot_condition(cls, value):
        if not (value is None or value in ['Нормальная', 'Уплощена', 'Плоская']):
            raise HTTPException(
                status_code=422, detail="Foot condition should be in ['Нормальная', 'Уплощена', 'Плоская']"
            )
        return value

    @validator("visual_acuity")
    def validate_visual_acuity(cls, value):
        if not (value is None or value in ['Нормальная', 'Снижена']):
            raise HTTPException(
                status_code=422, detail="Visual acuity should be in ['Нормальная', 'Снижена']"
            )
        return value

    @validator("malinovsky_test")
    def validate_malinovsky_test(cls, value):
        if not (value is None or value in ['Нормальная', 'Предмиопия']):
            raise HTTPException(
                status_code=422, detail="Malinovsky test should be in ['Нормальная', 'Предмиопия']"
            )
        return value

    @validator("binocular_vision")
    def validate_binocular_vision(cls, value):
        if not (value is None or value in ['Норма', 'Нарушение']):
            raise HTTPException(
                status_code=422, detail="Binocular vision should be in ['Норма', 'Нарушение']"
            )
        return value

    @validator("hearing_acuteness")
    def validate_hearing_acuteness(cls, value):
        if not (value is None or value in ['Норма', 'Снижена']):
            raise HTTPException(
                status_code=422, detail="Hearing acuteness should be in ['Норма', 'Снижена']"
            )
        return value

    @validator("physical_fitness")
    def validate_physical_fitness(cls, value):
        if not (value is None or value in ['Норма', 'Снижена', 'Повышена']):
            raise HTTPException(
                status_code=422, detail="Physical fitness should be in ['Норма', 'Снижена', 'Повышена']"
            )
        return value

    @validator("protein_in_urine")
    def validate_protein_in_urine(cls, value):
        if not (value is None or value in ['Норма', 'Следы белка', 'Белок в моче']):
            raise HTTPException(
                status_code=422, detail="Protein in urine should be in ['Норма', 'Следы белка', 'Белок в моче']"
            )
        return value

    @validator("glucose_in_urine")
    def validate_glucose_in_urine(cls, value):
        if not (value is None or value in ['Норма', 'Глюкоза в моче']):
            raise HTTPException(
                status_code=422, detail="Glucose in urine should be in ['Норма', 'Глюкоза в моче']"
            )
        return value

    @validator("biological_age")
    def validate_biological_age(cls, value):
        if not (value is None or value in ['Соответствует', 'Опережает', 'Отстает']):
            raise HTTPException(
                status_code=422, detail="Biological age should be in ['Соответствует', 'Опережает', 'Отстает']"
            )
        return value


class ScreeningUpdate(ScreeningBase):
    prev_examination_date: date = Field(...)
