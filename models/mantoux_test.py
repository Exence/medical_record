from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class MantouxTestBase(BaseModel):
    medcard_num: int = Field(...)
    check_date: date = Field(...)
    result: str = Field(...)

class MantouxTest(MantouxTestBase):
    class Config:
        orm_mode = True

class MantouxTestCreate(MantouxTestBase):
    pass