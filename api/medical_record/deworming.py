from fastapi import (
    APIRouter,
    Depends,
)
from models.deworming import (
    DewormingPK,
    Deworming,
    DewormingCreate,
    DewormingUpdate,
)
from models.user import User
from services.medical_record.deworming import DewormingService
from services.auth import get_current_user


router = APIRouter(
    prefix='/deworming',
    tags=['Deworming']
)


@router.get('/get_all', response_model=list[Deworming])
async def get_dewormings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: DewormingService = Depends()):
    return service.get_dewormings_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=Deworming)
async def get_deworming_by_pk(deworming_pk: DewormingPK,
                              user: User = Depends(get_current_user),
                              service: DewormingService = Depends()):
    return service.get_deworming_by_pk(user=user, deworming_pk=deworming_pk)


@router.post('/add', response_model=Deworming)
async def add_deworming(deworming_data: DewormingCreate,
                        user: User = Depends(get_current_user),
                        service: DewormingService = Depends()):
    return service.add_new_deworming(user=user, deworming_data=deworming_data)


@router.post('/update', response_model=Deworming)
async def update_deworming(deworming_data: DewormingUpdate,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    return service.update_deworming(user=user, deworming_data=deworming_data)


@router.post('/delete')
async def delete_deworming(deworming_pk: DewormingPK,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    service.delete_deworming(user=user, deworming_pk=deworming_pk)
