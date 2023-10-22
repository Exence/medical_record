from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/vaccination',
    tags=['Vaccination']
)

@router.post('/add')
async def add_extra_class(vaccination_data: JsonForm,
                          user: User = Depends(get_current_user),
                          service: VaccinationService = Depends()):
    vaccination = vaccination_data.json_data
    service.add_new_vaccination(user=user, vaccination=vaccination)

@router.post('/update')
async def update_vaccination(vaccination_data: JsonForm,
                             user: User = Depends(get_current_user),
                             service: VaccinationService = Depends()):
    vaccination = vaccination_data.json_data
    service.update_vaccination(user=user, vaccination=vaccination)

@router.post('/delete')
async def delete_prof_vaccination(vaccination_data: JsonForm,
                                  user: User = Depends(get_current_user),
                                  service: VaccinationService = Depends()):
    vaccination = vaccination_data.json_data
    service.delete_vaccination(user=user, vaccination=vaccination)
