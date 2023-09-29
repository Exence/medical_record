from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.hospitalization import HospitalizationService


router = APIRouter(
    prefix='/hospitalization',
    tags=['Hospitalization']
)

@router.post('/get')
async def get_hospitalization(hospitalization_data: JsonForm,  service: HospitalizationService = Depends()):
    hospitalization = hospitalization_data.json_data
    hospitalization = service.get_hospitalization_by_pk(hospitalization)
    return {"hospitalization": hospitalization}

@router.post('/add')
async def add_extra_class(hospitalization_data: JsonForm,  service: HospitalizationService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.add_new_hospitalization(hospitalization)

@router.post('/update')
async def update_hospitalization(hospitalization_data: JsonForm,  service: HospitalizationService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.update_hospitalization(hospitalization)

@router.post('/delete')
async def delete_hospitalization(hospitalization_data: JsonForm,  service: HospitalizationService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.delete_hospitalization(hospitalization)