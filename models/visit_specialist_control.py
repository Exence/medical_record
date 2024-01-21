from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class VisitSpecialistControlMain(BaseModel):
    medcard_num: int = Field(...)
    start_dispanser_date: date = Field(...)


class VisitSpecialistControlPK(VisitSpecialistControlMain):
    assigned_date: date = Field(...)


class VisitSpecialistControlBase(VisitSpecialistControlPK):
    fact_date: date | None


class VisitSpecialistControl(VisitSpecialistControlBase):
    class Config:
        orm_mode = True


class VisitSpecialistControlCreate(VisitSpecialistControlBase):
    pass


class VisitSpecialistControlUpdate(VisitSpecialistControlCreate):
    prev_assigned_date: date = Field(...)
