from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.screening import ScreeningService
from services.auth import get_current_user


router = APIRouter(
    prefix='/screening',
    tags=['Screening']
)

@router.post('/get')
async def get_screening(screening_data: JsonForm,
                        user: User = Depends(get_current_user),
                        service: ScreeningService = Depends()):
    screening = screening_data.json_data
    screening = service.get_screening_by_pk(user=user, screening_data=screening)
    return  screening

@router.post('/add')
async def add_extra_class(screening_data: JsonForm,
                          user: User = Depends(get_current_user),
                          service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.add_new_screening(user=user, screening=screening)

@router.post('/update')
async def update_screening(screening_data: JsonForm,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.update_screening(user=user, screening=screening)

@router.post('/delete')
async def delete_screening(screening_data: JsonForm,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    screening = screening_data.json_data
    service.delete_screening(user=user, screening=screening)
