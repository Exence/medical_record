from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.dispensary import Dispensary, DispensaryPK, DispensaryCreate, DispensaryUpdate
from models.user import User
from services.medical_record.dispensary import DispensaryService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/dispensaries',
    tags=['Dispensary']
)


@router.get('/', response_model=list[Dispensary])
async def get_dispensaries_by_medcard_num(medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: DispensaryService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_dispensaries_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Dispensary)
async def get_dispensary_by_pk(dispensary_pk: DispensaryPK,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: DispensaryService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_dispensary_by_pk(id=dispensary_pk.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Dispensary)
async def add_dispensary(dispensary_data: DispensaryCreate,
                         medcard_num: int,
                         user: User = Depends(get_current_user),
                         service: DispensaryService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_dispensary(dispensary_data=dispensary_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Dispensary)
async def update_dispensary(dispensary_data: DispensaryUpdate,
                            medcard_num: int,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_dispensary(dispensary_data=dispensary_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_dispensary(dispensary_pk: DispensaryPK,
                            medcard_num: int,
                            user: User = Depends(get_current_user),
                            service: DispensaryService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_dispensary(id=dispensary_pk.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )