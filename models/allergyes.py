from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class AllergyPK(BaseModel):
    medcard_num: int = Field(...)
    allergen: str = Field(...)


class AllergyBase(AllergyPK):
    allergy_type: str = Field(...)
    start_age: int = Field(...)
    reaction_type: str = Field(...)
    diagnosis_date: date = Field(...)
    note: str | None

class AllergyUpdate(AllergyBase):
    prev_allergen: str = Field(...)
    class Config:
        orm_mode = True

class AllergyCreate(AllergyBase):
    pass

class Allergy(AllergyBase):
    pass 

class AllergyCreate(AllergyBase):
    @validator("allergy_type")
    def validate_allergy_type(cls, value):
        if not value in ['Вакцинальная',  'Лекарственная',  'Аллергические заболевания']:
            raise HTTPException(
                status_code=422, detail="Allergy type should be in ['Вакцинальная',  'Лекарственная',  'Аллергические заболевания']"
            )
        return value
