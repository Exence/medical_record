from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
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
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/screenings',
    tags=['Screening']
)


@router.get('/', response_model=list[Screening])
async def get_screenings_by_medcard_num(medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: ScreeningService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_screenings_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Screening)
async def get_screening_by_pk(screening_pk: ScreeningPK,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: ScreeningService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_screening_by_pk(screening_pk=screening_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Screening)
async def add_screening(screening_data: ScreeningCreate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ScreeningService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_screening(screening_data=screening_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Screening)
async def update_screening(screening_data: ScreeningUpdate,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_screening(screening_data=screening_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_screening(screening_pk: ScreeningPK,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: ScreeningService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_screening(screening_pk=screening_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
