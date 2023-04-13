from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class VisitSpecialistControlBase(BaseModel):
    medcard_num: int = Field(...)
    start_dispanser_date: date = Field(...)
    assigned_date: date = Field(...)
    fact_date: date | None

class VisitSpecialistControl(VisitSpecialistControlBase):
    class Config:
        orm_mode = True

class VisitSpecialistControlCreate(VisitSpecialistControlBase):
    pass
