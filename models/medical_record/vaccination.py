import re

from datetime import date
from fastapi import (
    Form,
    HTTPException,
)
from pydantic import (
    BaseModel,
    Field,
    validator,
)

from models.catalogs.vac_name import VacName


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")
REACTION_MATCH_PATTERN = re.compile(r"^(Не|За)медленная$")


class VaccinationPK(BaseModel):
    medcard_num: int = Field(...)
    vac_name_id: int = Field(...)
    vac_type: str = Field(..., max_length=16)


class VaccinationBase(VaccinationPK):
    vac_date: date = Field(...)
    serial: str = Field(..., max_length=90)
    dose: float = Field(...)
    introduction_method: str = Field(..., max_length=90)
    reaction: str = Field(...)
    doctor: str = Field(..., max_length=200)


class Vaccination(VaccinationBase):
    vac_name: VacName

    class Config:
        orm_mode = True


class VaccinationCreate(VaccinationBase):
    @validator("vac_type")
    def validate_vac_type(cls, value):
        if not re.compile(r"(^Вакцинация ?I{1,3}$)|(^Ревакцинация ?I{1,3}?V{0,1}$)").match(value):
            raise HTTPException(
                status_code=422, detail="Vaccination type should be in 'Вакцинация I-III' or 'Ревакцинация I-IV'"
            )
        return value

    @validator("reaction")
    def validate_reaction(cls, value):
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


class VaccinationUpdate(VaccinationCreate):
    prev_vac_name_id: int = Field(...)
    prev_vac_type: str = Field(...)


class VaccinationView(VaccinationBase):
    vac_name: str


class VacReport(BaseModel):
    vac_name_id: int
    vac_type: str = Field(..., max_length=16)

    @classmethod
    def as_form(cls,
                vac_name_id=Form(...),
                vac_type=Form(...)):
        return cls(
            vac_name_id=vac_name_id,
            vac_type=vac_type
        )
