from fastapi import (
    APIRouter,
    Depends,
)
from pprint import pprint

from models.screening import (
    ScreeningPK,
    Screening,
    ScreeningCreate,
    ScreeningUpdate,
)
from models.user import User
from services.medical_record.screening import ScreeningService
from services.auth import get_current_user


router = APIRouter(
    prefix='/screening',
    tags=['Screening']
)


@router.get('/get_all', response_model=list[Screening])
async def get_screenings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: ScreeningService = Depends()):
    return service.get_screenings_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=Screening)
async def get_screening_by_pk(screening_pk: ScreeningPK,
                              user: User = Depends(get_current_user),
                              service: ScreeningService = Depends()):
    return service.get_screening_by_pk(user=user, screening_pk=screening_pk)


@router.post('/add', response_model=Screening)
async def add_screening(screening_data: ScreeningCreate,
                        user: User = Depends(get_current_user),
                        service: ScreeningService = Depends()):
    return service.add_new_screening(user=user, screening_data=screening_data)


@router.post('/update', response_model=Screening)
async def update_screening(screening_data: ScreeningUpdate,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    return service.update_screening(user=user, screening_data=screening_data)


@router.post('/delete')
async def delete_screening(screening_pk: ScreeningPK,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    service.delete_screening(user=user, screening_pk=screening_pk)
