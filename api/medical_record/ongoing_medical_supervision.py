from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from services.auth import get_current_user


router = APIRouter(
    prefix='/ongoing_medical_supervision',
    tags=['Ongoing medical supervision']
)

@router.post('/get')
async def get_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm, 
                                          user: User = Depends(get_current_user), 
                                          service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    ongoing_medical_supervision = service.get_ongoing_medical_supervision_by_pk(user=user, ongoing_medical_supervision_data=ongoing_medical_supervision)
    return  ongoing_medical_supervision

@router.post('/add')
async def add_extra_class(ongoing_medical_supervision_data: JsonForm,  
                          user: User = Depends(get_current_user),
                          service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.add_new_ongoing_medical_supervision(user=user, ongoing_medical_supervisio=ongoing_medical_supervision)

@router.post('/update')
async def update_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  
                                             user: User = Depends(get_current_user),
                                             service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.update_ongoing_medical_supervision(user=user, ongoing_medical_supervisio=ongoing_medical_supervision)

@router.post('/delete')
async def delete_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm, 
                                             user: User = Depends(get_current_user), 
                                             service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.delete_ongoing_medical_supervision(user=user, ongoing_medical_supervisio=ongoing_medical_supervision)
