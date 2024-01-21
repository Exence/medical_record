from fastapi import (
    APIRouter,
    Depends,
)
from models.oral_sanation import (
    OralSanationPK,
    OralSanation,
    OralSanationCreate,
    OralSanationUpdate,
)
from models.user import User
from services.medical_record.oral_sanation import OralSanationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/oral_sanation',
    tags=['OralSanation']
)


@router.get('/get_all', response_model=list[OralSanation])
async def get_oral_sanations_by_medcard_num(medcard_num: int,
                                            user: User = Depends(
                                                get_current_user),
                                            service: OralSanationService = Depends()):
    return service.get_oral_sanations_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=OralSanation)
async def get_oral_sanation_by_pk(oral_sanation_pk: OralSanationPK,
                                  user: User = Depends(get_current_user),
                                  service: OralSanationService = Depends()):
    return service.get_oral_sanation_by_pk(user=user, oral_sanation_pk=oral_sanation_pk)


@router.post('/add', response_model=OralSanation)
async def add_oral_sanation(oral_sanation_data: OralSanationCreate,
                            user: User = Depends(get_current_user),
                            service: OralSanationService = Depends()):
    return service.add_new_oral_sanation(user=user, oral_sanation_data=oral_sanation_data)


@router.post('/update', response_model=OralSanation)
async def update_oral_sanation(oral_sanation_data: OralSanationUpdate,
                               user: User = Depends(get_current_user),
                               service: OralSanationService = Depends()):
    return service.update_oral_sanation(user=user, oral_sanation_data=oral_sanation_data)


@router.post('/delete')
async def delete_oral_sanation(oral_sanation_pk: OralSanationPK,
                               user: User = Depends(get_current_user),
                               service: OralSanationService = Depends()):
    service.delete_oral_sanation(user=user, oral_sanation_pk=oral_sanation_pk)
