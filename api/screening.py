from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.screening import ScreeningService


router = APIRouter(
    prefix='/screening',
    tags=['Screening']
)

@router.post('/get')
async def get_screening(screening_data: JsonForm,  service: ScreeningService = Depends()):
    screening = screening_data.json_data
    screening = service.get_screening_by_pk(screening)
    return  screening

@router.post('/add')
async def add_extra_class(screening_data: JsonForm,  service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.add_new_screening(screening)

@router.post('/update')
async def update_screening(screening_data: JsonForm,  service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.update_screening(screening)

@router.post('/delete')
async def delete_screening(screening_data: JsonForm,  service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.delete_screening(screening)
