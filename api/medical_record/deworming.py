from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.deworming import (
    DewormingPK,
    Deworming,
    DewormingCreate,
    DewormingUpdate,
)
from models.user import User
from services.medical_record.deworming import DewormingService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/dewormings',
    tags=['Deworming']
)


@router.get('/', response_model=list[Deworming])
async def get_dewormings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: DewormingService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_dewormings_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Deworming)
async def get_deworming_by_pk(deworming_pk: DewormingPK,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: DewormingService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_deworming_by_pk(deworming_pk=deworming_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Deworming)
async def add_deworming(deworming_data: DewormingCreate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: DewormingService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_deworming(deworming_data=deworming_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Deworming)
async def update_deworming(deworming_data: DewormingUpdate,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_deworming(deworming_data=deworming_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_deworming(deworming_pk: DewormingPK,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_deworming(deworming_pk=deworming_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
