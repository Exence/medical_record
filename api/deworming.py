from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.deworming import DewormingService


router = APIRouter(
    prefix='/deworming',
    tags=['Deworming']
)

@router.post('/get')
async def get_deworming(deworming_data: JsonForm,  service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    deworming = service.get_deworming_by_pk(deworming)
    return {"deworming": deworming}

@router.post('/add')
async def add_extra_class(deworming_data: JsonForm,  service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.add_new_deworming(deworming)

@router.post('/update')
async def update_deworming(deworming_data: JsonForm,  service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.update_deworming(deworming)

@router.post('/delete')
async def delete_deworming(deworming_data: JsonForm,  service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.delete_deworming(deworming)