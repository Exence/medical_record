from fastapi import (
    APIRouter,
    Depends,
)

from models.medical_record.screening import (
    ScreeningPK,
    Screening,
    ScreeningCreate,
    ScreeningUpdate,
)
from models.user import User
from services.medical_record.screening import ScreeningService
from services.auth import get_current_user


router = APIRouter(
    prefix='/screenings',
    tags=['Screening']
)


@router.get('/', response_model=list[Screening])
async def get_screenings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: ScreeningService = Depends()):
    return service.get_screenings_by_medcard_num(medcard_num=medcard_num)


@router.post('/one', response_model=Screening)
async def get_screening_by_pk(screening_pk: ScreeningPK,
                              user: User = Depends(get_current_user),
                              service: ScreeningService = Depends()):
    return service.get_screening_by_pk(screening_pk=screening_pk)


@router.post('/', response_model=Screening)
async def add_screening(screening_data: ScreeningCreate,
                        user: User = Depends(get_current_user),
                        service: ScreeningService = Depends()):
    return service.add_new_screening(screening_data=screening_data)


@router.put('/', response_model=Screening)
async def update_screening(screening_data: ScreeningUpdate,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    return service.update_screening(screening_data=screening_data)


@router.delete('/')
async def delete_screening(screening_pk: ScreeningPK,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    service.delete_screening(screening_pk=screening_pk)
