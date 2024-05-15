from pydantic import (
  BaseModel,
  Field,
)
from typing import TypedDict


class ClinicPK(BaseModel):
    id: int = Field(...)

class ClinicBase(BaseModel):
    name: str = Field(...)

class Clinic(ClinicPK, ClinicBase):
    class Config:
        orm_mode = True

class ClinicCreate(ClinicBase):
    pass

class ClinicUpdate(Clinic):
    pass

class ClinicDict(TypedDict):
    name: str

