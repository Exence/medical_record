from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
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
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/tub_vacs',
    tags=['Tuberculosis vaccination']
)


@router.post('/one')
async def get_tuberculosis_vaccination(tub_vac_pk: TuberculosisVaccinationPK,
                                       medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: TuberculosisVaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        tub_vac = service.get_tuberculosis_vaccination_by_pk(tub_vac_pk=tub_vac_pk)
        return tub_vac
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/')
async def add_tuberculosis_vaccination(tub_vac_data: TuberculosisVaccinationCreate,
                                       medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: TuberculosisVaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_tuberculosis_vaccination(tub_vac_data=tub_vac_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/')
async def update_tuberculosis_vaccination(tub_vac_data: TuberculosisVaccinationUpdate,
                                          medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: TuberculosisVaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_tuberculosis_vaccination(tub_vac_data=tub_vac_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_tuberculosis_vaccination(tub_vac_pk: TuberculosisVaccinationPK,
                                          medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: TuberculosisVaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_tuberculosis_vaccination(tub_vac_pk=tub_vac_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
