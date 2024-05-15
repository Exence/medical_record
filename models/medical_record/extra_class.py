from pydantic import (
    BaseModel,
    Field,
)


class ExtraClassPK(BaseModel):
    medcard_num: int = Field(...)
    classes_type: str = Field(...)
    age: int = Field(..., gt=0, lt=8)


class ExtraClassBase(ExtraClassPK):
    hours_on_week: int = Field(..., gt=0, lt=40)


class ExtraClass(ExtraClassBase):
    class Config:
        orm_mode = True


class ExtraClassCreate(ExtraClassBase):
    pass


class ExtraClassUpdate(ExtraClassCreate):
    prev_classes_type: str = Field(...)
    prev_age: int = Field(..., gt=0, lt=8)
