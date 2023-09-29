from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.ongoing_medical_supervision import OngoingMedicalSupervisionService


router = APIRouter(
    prefix='/ongoing_medical_supervision',
    tags=['Ongoing medical supervision']
)

@router.post('/get')
async def get_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  
                                          service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    ongoing_medical_supervision = service.get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision)
    return  ongoing_medical_supervision

@router.post('/add')
async def add_extra_class(ongoing_medical_supervision_data: JsonForm,  
                          service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.add_new_ongoing_medical_supervision(ongoing_medical_supervision)

@router.post('/update')
async def update_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  
                                             service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.update_ongoing_medical_supervision(ongoing_medical_supervision)

@router.post('/delete')
async def delete_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  
                                             service: OngoingMedicalSupervisionService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.delete_ongoing_medical_supervision(ongoing_medical_supervision)