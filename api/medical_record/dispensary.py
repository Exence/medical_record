from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record.dispensary import DispensaryService


router = APIRouter(
    prefix='/dispensary',
    tags=['Dispensary']
)

@router.post('/dispensary/get')
async def get_dispensary(dispensary_data: JsonForm,  service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    dispensary = service.get_dispensary_by_pk(dispensary)
    return {"dispensary": dispensary}

@router.post('/dispensary/add')
async def add_new_dispensary(dispensary_data: JsonForm,  service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.add_new_dispensary(dispensary)

@router.post('/dispensary/update')
async def update_dispensary(dispensary_data: JsonForm,  service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.update_dispensary(dispensary)

@router.post('/dispensary/delete')
async def delete_dispensary(dispensary_data: JsonForm,  service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.delete_dispensary(dispensary)