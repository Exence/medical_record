from fastapi import (
    APIRouter,
    Depends,  
)
from models.tub_vac import (
    TuberculosisVaccinationPK,
    TuberculosisVaccination,
    TuberculosisVaccinationCreate,
    TuberculosisVaccinationUpdate,
)
from models.user import User
from services.medical_record.tub_vac import TuberculosisVaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/tub_vac',
    tags=['Tuberculosis vaccination']
)

@router.post('/get_one')
async def get_tub_vac(tub_vac_pk: TuberculosisVaccinationPK,
                      user: User = Depends(get_current_user),
                      service: TuberculosisVaccinationService = Depends()):
    tub_vac = service.get_tub_vac_by_pk(user=user, tub_vac_pk=tub_vac_pk)
    return  tub_vac

@router.post('/add')
async def add_extra_class(tub_vac_data: TuberculosisVaccinationCreate,
                          user: User = Depends(get_current_user),
                          service: TuberculosisVaccinationService = Depends()):
    service.add_new_tub_vac(user=user, tub_vac_data=tub_vac_data)

@router.post('/update')
async def update_tub_vac(tub_vac_data: TuberculosisVaccinationUpdate,
                         user: User = Depends(get_current_user),
                         service: TuberculosisVaccinationService = Depends()):
    service.update_tub_vac(user=user, tub_vac_data=tub_vac_data)

@router.post('/delete')
async def delete_tub_vac(tub_vac_pk: TuberculosisVaccinationPK,
                         user: User = Depends(get_current_user),
                         service: TuberculosisVaccinationService = Depends()):
    service.delete_tub_vac(user=user, tub_vac_pk=tub_vac_pk)
