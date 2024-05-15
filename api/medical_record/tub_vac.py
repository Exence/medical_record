from fastapi import (
    APIRouter,
    Depends,
)
from models.medical_record.tub_vac import (
    TuberculosisVaccinationPK,
    TuberculosisVaccination,
    TuberculosisVaccinationCreate,
    TuberculosisVaccinationUpdate,
)
from models.user import User
from services.medical_record.tub_vac import TuberculosisVaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/tub_vacs',
    tags=['Tuberculosis vaccination']
)


@router.post('/one')
async def get_tuberculosis_vaccination(tub_vac_pk: TuberculosisVaccinationPK,
                      user: User = Depends(get_current_user),
                      service: TuberculosisVaccinationService = Depends()):
    tub_vac = service.get_tuberculosis_vaccination_by_pk(tub_vac_pk=tub_vac_pk)
    return tub_vac


@router.post('/')
async def add_tuberculosis_vaccination(tub_vac_data: TuberculosisVaccinationCreate,
                          user: User = Depends(get_current_user),
                          service: TuberculosisVaccinationService = Depends()):
    service.add_new_tuberculosis_vaccination(tub_vac_data=tub_vac_data)


@router.put('/')
async def update_tuberculosis_vaccination(tub_vac_data: TuberculosisVaccinationUpdate,
                         user: User = Depends(get_current_user),
                         service: TuberculosisVaccinationService = Depends()):
    service.update_tuberculosis_vaccination(tub_vac_data=tub_vac_data)


@router.delete('/')
async def delete_tuberculosis_vaccination(tub_vac_pk: TuberculosisVaccinationPK,
                         user: User = Depends(get_current_user),
                         service: TuberculosisVaccinationService = Depends()):
    service.delete_tuberculosis_vaccination(tub_vac_pk=tub_vac_pk)
