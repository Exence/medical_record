from pydantic import (
    BaseModel,
    Field,
)
from typing import List
from models.child import ChildToShow


class KindergartenBase(BaseModel):
    number: int = Field(..., gt=-1, lt=1000)
    name: str = Field(...,max_length=150)

class Kindergarten(KindergartenBase):
    class Config:
        orm_mode = True

class KindergartenCreate(KindergartenBase):
    pass


class KindergartenWithChildrens(KindergartenBase):
    groups: list = [[], [], [], [], [], []]
