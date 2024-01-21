from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class DispensaryPK(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)


class DispensaryBase(DispensaryPK):
    diagnosis: str = Field(...)
    specialist: str = Field(...)
    end_date: date | None
    end_reason: str | None


class Dispensary(DispensaryBase):
    class Config:
        orm_mode = True


class DispensaryCreate(DispensaryBase):
    pass


class DispensaryUpdate(DispensaryCreate):
    prev_start_date: date = Field(...)
