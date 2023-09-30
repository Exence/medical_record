from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record.oral_sanation import OralSanationService


router = APIRouter(
    prefix='/oral_sanation',
    tags=['Oral sanation']
)

@router.post('/get')
async def get_oral_sanation(oral_sanation_data: JsonForm,  service: OralSanationService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    oral_sanation = service.get_oral_sanation_by_pk(oral_sanation)
    return {"oral_sanation": oral_sanation}

@router.post('/add')
async def add_extra_class(oral_sanation_data: JsonForm,  service: OralSanationService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.add_new_oral_sanation(oral_sanation)

@router.post('/update')
async def update_oral_sanation(oral_sanation_data: JsonForm,  service: OralSanationService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.update_oral_sanation(oral_sanation)

@router.post('/delete')
async def delete_oral_sanation(oral_sanation_data: JsonForm,  service: OralSanationService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.delete_oral_sanation(oral_sanation)