from datetime import date
from pydantic import (
    BaseModel,
    Field,
)


class DewormingBase(BaseModel):
    medcard_num: int = Field(...)
    deworming_date: date = Field(...)
    result: str = Field(...)

class Deworming(DewormingBase):
    class Config:
        orm_mode = True

class DewormingCreate(DewormingBase):
    pass
