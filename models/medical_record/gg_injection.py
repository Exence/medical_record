import re

from datetime import date
from decimal import Decimal
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")
REACTION_MATCH_PATTERN = re.compile(r"^(Не|За)медленная$")


class GammaGlobulinInjectionPK(BaseModel):
    medcard_num: int = Field(...)
    vac_date: date = Field(...)


class GammaGlobulinInjectionBase(GammaGlobulinInjectionPK):
    reason: str = Field(...)
    serial: str = Field(..., max_length=90)
    dose: Decimal = Field(...)
    reaction: str = Field(...)
    doctor: str = Field(..., max_length=200)


class GammaGlobulinInjection(GammaGlobulinInjectionBase):
    class Config:
        orm_mode = True


class GammaGlobulinInjectionCreate(GammaGlobulinInjectionBase):
    @validator("reaction")
    def validate_vac_type(cls, value):
        if not REACTION_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Reaction should be 'Немедленная' or 'Замедленная'"
            )
        return value

    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class GammaGlobulinInjectionUpdate(GammaGlobulinInjectionCreate):
    prev_vac_date: date = Field(...)
