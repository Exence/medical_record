from fastapi import (
    APIRouter,
    Depends,
)
from models.dispensary import Dispensary, DispensaryPK, DispensaryCreate, DispensaryUpdate
from models.user import User
from services.medical_record.dispensary import DispensaryService
from services.auth import get_current_user


router = APIRouter(
    prefix='/dispensaryes',
    tags=['Dispensary']
)


@router.get('/', response_model=list[Dispensary])
async def get_dispensaryes_by_medcard_num(medcard_num: int,
                                          user: User = Depends(
                                              get_current_user),
                                          service: DispensaryService = Depends()):
    return service.get_dispensaryes_by_medcard_num(medcard_num=medcard_num)


@router.post('/one', response_model=Dispensary)
async def get_dispensary_by_id(dispensary_pk: DispensaryPK,
                               user: User = Depends(get_current_user),
                               service: DispensaryService = Depends()):
    return service.get_dispensary_by_id(id=dispensary_pk.id)


@router.post('/', response_model=Dispensary)
async def add_dispensary(dispensary_data: DispensaryCreate,
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    return service.add_new_dispensary(dispensary_data=dispensary_data)


@router.put('/', response_model=Dispensary)
async def update_dispensary(dispensary_data: DispensaryUpdate,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    return service.update_dispensary(dispensary_data=dispensary_data)


@router.delete('/')
async def delete_dispensary(dispensary_pk: DispensaryPK,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    service.delete_dispensary(id=dispensary_pk.id)
