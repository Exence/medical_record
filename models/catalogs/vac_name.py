from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)


class VacNamePK(BaseModel):
    id: int = Field(...)


class VacNameBase(BaseModel):
    name: str = Field(...)
    vac_type: str = Field(...)


class VacName(VacNamePK, VacNameBase):
    class Config:
        orm_mode = True


class VacNameTypeDict(BaseModel):
    prof: dict[int, str]
    epid: dict[int, str]

    class Config:
        schema_extra = {
            "example": {
                        "prof": {
                            1: "Прививка 1",
                            2: "Прививка 2",
                            3: "Прививка 3"
                        },
                        "epid": {
                            4: "Прививка 4",
                            5: "Прививка 5",
                            6: "Прививка 6"
                        }
                    }
        }


class VacNameCreate(VacNameBase):
    @validator("vac_type")
    def validate_vac_type(cls, value):
        if not value in ['Профилактическая', 'По показаниям']:
            raise HTTPException(
                status_code=422, detail="Vac type should be in ['Профилактическая', 'По показаниям']"
            )
        return value


class VacNameUpdate(VacNamePK, VacNameCreate):
    pass
