from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class VacNameBase(BaseModel):
    name: str = Field(...)
    vac_type: str = Field(...)

class VacName(VacNameBase):
    id: int = Field(...)
    
    class Config:
        orm_mode = True

class VacNameCreate(VacNameBase):
    @validator("vac_type")
    def validate_vac_type(cls, value):
        if not value in ['Профилактическая', 'По показаниям']:
            raise HTTPException(
                status_code=422, detail="Vac type should be in ['Профилактическая', 'По показаниям']"
            )
        return value
