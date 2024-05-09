from fastapi import (
    APIRouter,
    Depends,
)
from models.vaccination import (
    VaccinationPK,
    Vaccination,
    VaccinationCreate,
    VaccinationUpdate,
)
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/vaccinations',
    tags=['Vaccination']
)


@router.get('/', response_model=list[Vaccination])
async def get_vaccinations_by_medcard_num(medcard_num: int,
                                          user: User = Depends(
                                              get_current_user),
                                          service: VaccinationService = Depends()):
    return service.get_vaccinations_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/one', response_model=Vaccination)
async def get_vaccination_by_pk(vaccination_pk: VaccinationPK,
                                user: User = Depends(get_current_user),
                                service: VaccinationService = Depends()):
    return service.get_vaccination_by_pk(user=user, vaccination_pk=vaccination_pk)


@router.post('/', response_model=Vaccination)
async def add_vaccination(vaccination_data: VaccinationCreate,
                          user: User = Depends(get_current_user),
                          service: VaccinationService = Depends()):
    return service.add_new_vaccination(user=user, vaccination_data=vaccination_data)


@router.put('/', response_model=Vaccination)
async def update_vaccination(vaccination_data: VaccinationUpdate,
                             user: User = Depends(get_current_user),
                             service: VaccinationService = Depends()):
    return service.update_vaccination(user=user, vaccination_data=vaccination_data)


@router.delete('/')
async def delete_vaccination(vaccination_pk: VaccinationPK,
                             user: User = Depends(get_current_user),
                             service: VaccinationService = Depends()):
    service.delete_vaccination(user=user, vaccination_pk=vaccination_pk)
