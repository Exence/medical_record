from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class DispensaryPK(BaseModel):
    id: int = Field(...)


class DispensaryBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    diagnosis: str = Field(...)
    specialist: str = Field(...)
    end_date: date | None
    end_reason: str | None


class Dispensary(DispensaryPK, DispensaryBase):
    class Config:
        orm_mode = True


class DispensaryCreate(DispensaryBase):
    pass


class DispensaryUpdate(DispensaryPK, DispensaryCreate):
    pass
