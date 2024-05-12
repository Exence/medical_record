from pydantic import (
    BaseModel,
    Field,
)
from models.child import ChildWithParentsView
from typing import TypedDict


class KindergartenBase(BaseModel):
    number: int = Field(..., gt=-1, lt=1000)
    name: str = Field(..., max_length=150)


class Kindergarten(KindergartenBase):
    class Config:
        orm_mode = True


class KindergartenCreate(KindergartenBase):
    pass


class KindergartenUpdate(KindergartenBase):
    prev_number: int = Field(..., gt=-1, lt=1000)


class KindergartenWithchildren(TypedDict):
    groups: dict[list[ChildWithParentsView]]
