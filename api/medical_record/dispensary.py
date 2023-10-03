from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.dispensary import DispensaryService
from services.auth import get_current_user


router = APIRouter(
    prefix='/dispensary',
    tags=['Dispensary']
)

@router.post('/dispensary/get')
async def get_dispensary(dispensary_data: JsonForm,
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    dispensary = service.get_dispensary_by_pk(user=user, dispensary_data=dispensary)
    return {"dispensary": dispensary}

@router.post('/dispensary/add')
async def add_new_dispensary(dispensary_data: JsonForm,
                             user: User = Depends(get_current_user),
                             service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.add_new_dispensary(user=user, dispensary=dispensary)

@router.post('/dispensary/update')
async def update_dispensary(dispensary_data: JsonForm,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.update_dispensary(user=user, dispensary=dispensary)

@router.post('/dispensary/delete')
async def delete_dispensary(dispensary_data: JsonForm,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    dispensary = dispensary_data.json_data
    service.delete_dispensary(user=user, dispensary=dispensary)
