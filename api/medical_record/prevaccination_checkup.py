from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.prevaccination_checkup import PrevaccinationCheckupService
from services.auth import get_current_user


router = APIRouter(
    prefix='/prevaccination_checkup',
    tags=['Prevaccination checkup']
)

@router.post('/get')
async def get_prevaccination_checkup(prevaccination_checkup_data: JsonForm, 
                                     user: User = Depends(get_current_user), 
                                     service: PrevaccinationCheckupService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    prevaccination_checkup = service.get_prevaccination_checkup_by_pk(user=user, prevaccination_checkup_data=prevaccination_checkup)
    return {"prevaccination_checkup": prevaccination_checkup}

@router.post('/add')
async def add_extra_class(prevaccination_checkup_data: JsonForm, 
                          user: User = Depends(get_current_user), 
                          service: PrevaccinationCheckupService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    return service.add_new_prevaccination_checkup(user=user, prevaccination_checkup=prevaccination_checkup)

@router.post('/update')
async def update_prevaccination_checkup(prevaccination_checkup_data: JsonForm, 
                                        user: User = Depends(get_current_user), 
                                        service: PrevaccinationCheckupService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    return service.update_prevaccination_checkup(user=user, prevaccination_checkup=prevaccination_checkup)

@router.post('/delete')
async def delete_prevaccination_checkup(prevaccination_checkup_data: JsonForm,  
                                        user: User = Depends(get_current_user),
                                        service: PrevaccinationCheckupService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    service.delete_prevaccination_checkup(user=user, prevaccination_checkup=prevaccination_checkup)
