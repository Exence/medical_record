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
    prefix='/dewormings',
    tags=['Deworming']
)


@router.get('/', response_model=list[Deworming])
async def get_dewormings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: DewormingService = Depends()):
    return service.get_dewormings_by_medcard_num(medcard_num=medcard_num)


@router.post('/one', response_model=Deworming)
async def get_deworming_by_pk(deworming_pk: DewormingPK,
                              user: User = Depends(get_current_user),
                              service: DewormingService = Depends()):
    return service.get_deworming_by_pk(deworming_pk=deworming_pk)


@router.post('/', response_model=Deworming)
async def add_deworming(deworming_data: DewormingCreate,
                        user: User = Depends(get_current_user),
                        service: DewormingService = Depends()):
    return service.add_new_deworming(deworming_data=deworming_data)


@router.put('/', response_model=Deworming)
async def update_deworming(deworming_data: DewormingUpdate,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    return service.update_deworming(deworming_data=deworming_data)


@router.delete('/')
async def delete_deworming(deworming_pk: DewormingPK,
                           user: User = Depends(get_current_user),
                           service: DewormingService = Depends()):
    service.delete_deworming(deworming_pk=deworming_pk)
