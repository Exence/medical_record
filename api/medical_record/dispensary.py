from fastapi import (
    APIRouter,
    Depends,  
)
from models.dispensary import Dispensary, DispensaryPK, DispensaryCreate, DispensaryUpdate
from models.user import User
from services.medical_record.dispensary import DispensaryService
from services.auth import get_current_user


router = APIRouter(
    prefix='/dispensary',
    tags=['Dispensary']
)

@router.get('/get_all', response_model=list[Dispensary])
async def get_dispensaryes_by_medcard_num(medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: DispensaryService = Depends()):
    return service.get_dispensaryes_by_medcard_num(user=user, medcard_num=medcard_num)

@router.post('/get_one', response_model=Dispensary)
async def get_dispensary_by_pk(dispensary_pk: DispensaryPK, 
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    return service.get_dispensary_by_pk(user=user, dispensary_pk=dispensary_pk)

@router.post('/add', response_model=Dispensary)
async def add_dispensary(dispensary_data: DispensaryCreate, 
                      user: User = Depends(get_current_user),
                      service: DispensaryService = Depends()):
    return service.add_new_dispensary(user=user, dispensary_data=dispensary_data)

@router.post('/update', response_model=Dispensary)
async def update_dispensary(dispensary_data: DispensaryUpdate, 
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    return service.update_dispensary(user=user, dispensary_data=dispensary_data)

@router.post('/delete')
async def delete_dispensary(dispensary_pk: DispensaryPK, 
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    service.delete_dispensary(user=user, dispensary_pk=dispensary_pk)
