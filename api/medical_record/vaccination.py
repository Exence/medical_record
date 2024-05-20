from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.vaccination import (
    VaccinationPK,
    Vaccination,
    VaccinationCreate,
    VaccinationUpdate,
)
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/vaccinations',
    tags=['Vaccination']
)


@router.get('/', response_model=list[Vaccination])
async def get_vaccinations_by_medcard_num(medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_vaccinations_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Vaccination)
async def get_vaccination_by_pk(vaccination_pk: VaccinationPK,
                                medcard_num: int,
                                user: User = Depends(get_current_user),
                                service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_vaccination_by_pk(vaccination_pk=vaccination_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Vaccination)
async def add_vaccination(vaccination_data: VaccinationCreate,
                          medcard_num: int,
                          user: User = Depends(get_current_user),
                          service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_vaccination(vaccination_data=vaccination_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Vaccination)
async def update_vaccination(vaccination_data: VaccinationUpdate,
                             medcard_num: int,
                             user: User = Depends(get_current_user),
                             service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_vaccination(vaccination_data=vaccination_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_vaccination(vaccination_pk: VaccinationPK,
                             medcard_num: int,
                             user: User = Depends(get_current_user),
                             service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_vaccination(vaccination_pk=vaccination_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
