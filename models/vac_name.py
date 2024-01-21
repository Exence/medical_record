from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)
from typing import TypedDict


class VacNamePK(BaseModel):
    id: int = Field(...)


class VacNameBase(BaseModel):
    name: str = Field(...)
    vac_type: str = Field(...)


class VacName(VacNamePK, VacNameBase):
    class Config:
        orm_mode = True


class VacNameDict(TypedDict):
    name: str
    vac_type: str


class VacNameCreate(VacNameBase):
    @validator("vac_type")
    def validate_vac_type(cls, value):
        if not value in ['Профилактическая', 'По показаниям']:
            raise HTTPException(
                status_code=422, detail="Vac type should be in ['Профилактическая', 'По показаниям']"
            )
        return value


class VacNameUpdate(VacNamePK, VacNameCreate):
    pass
