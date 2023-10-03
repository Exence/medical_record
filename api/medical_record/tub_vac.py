from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.tub_vac import TuberculosisVaccinationService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/tub_vac',
    tags=['Tuberculosis vaccination']
)

@router.post('/get')
async def get_tub_vac(tub_vac_data: JsonForm,
                      user: User = Depends(get_current_user_from_cookie),
                      service: TuberculosisVaccinationService = Depends()):
    tub_vac = tub_vac_data.json_data
    tub_vac = service.get_tub_vac_by_pk(user=user, tub_vac_data=tub_vac)
    return  tub_vac

@router.post('/add')
async def add_extra_class(tub_vac_data: JsonForm,
                          user: User = Depends(get_current_user_from_cookie),
                          service: TuberculosisVaccinationService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.add_new_tub_vac(user=user, tub_vac=tub_vac)

@router.post('/update')
async def update_tub_vac(tub_vac_data: JsonForm,
                         user: User = Depends(get_current_user_from_cookie),
                         service: TuberculosisVaccinationService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.update_tub_vac(user=user, tub_vac=tub_vac)

@router.post('/delete')
async def delete_tub_vac(tub_vac_data: JsonForm,
                         user: User = Depends(get_current_user_from_cookie),
                         service: TuberculosisVaccinationService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.delete_tub_vac(user=user, tub_vac=tub_vac)
