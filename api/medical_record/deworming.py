from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.deworming import DewormingService
from services.auth import get_current_user


router = APIRouter(
    prefix='/deworming',
    tags=['Deworming']
)

@router.post('/get')
async def get_deworming(deworming_data: JsonForm,
                        user: User = Depends(get_current_user),
                        service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    deworming = service.get_deworming_by_pk(user=user, deworming_data=deworming)
    return {"deworming": deworming}

@router.post('/add')
async def add_extra_class(deworming_data: JsonForm,
                          user: User = Depends(get_current_user),
                          service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.add_new_deworming(user=user, deworming=deworming)

@router.post('/update')
async def update_deworming(deworming_data: JsonForm,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.update_deworming(user=user, deworming=deworming)

@router.post('/delete')
async def delete_deworming(deworming_data: JsonForm,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    deworming = deworming_data.json_data
    service.delete_deworming(user=user, deworming=deworming)