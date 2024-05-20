from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.hospitalization import (
    HospitalizationPK,
    Hospitalization,
    HospitalizationCreate,
    HospitalizationUpdate,
)
from models.user import User
from services.medical_record.hospitalization import HospitalizationService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/hospitalizations',
    tags=['Hospitalization']
)


@router.get('/', response_model=list[Hospitalization])
async def get_hospitalizations_by_medcard_num(medcard_num: int,
                                              user: User = Depends(get_current_user),
                                              service: HospitalizationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_hospitalizations_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Hospitalization)
async def get_hospitalization_by_pk(hospitalization_pk: HospitalizationPK,
                                    medcard_num: int,
                                    user: User = Depends(get_current_user),
                                    service: HospitalizationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_hospitalization_by_pk(hospitalization_pk=hospitalization_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Hospitalization)
async def add_hospitalization(hospitalization_data: HospitalizationCreate,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: HospitalizationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_hospitalization(hospitalization_data=hospitalization_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Hospitalization)
async def update_hospitalization(hospitalization_data: HospitalizationUpdate,
                                 medcard_num: int,
                                 user: User = Depends(get_current_user),
                                 service: HospitalizationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_hospitalization(hospitalization_data=hospitalization_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_hospitalization(hospitalization_pk: HospitalizationPK,
                                 medcard_num: int,
                                 user: User = Depends(get_current_user),
                                 service: HospitalizationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_hospitalization(hospitalization_pk=hospitalization_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
