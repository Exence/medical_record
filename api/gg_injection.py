from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/gg_injection',
    tags=['Gamma-globulin injection']
)

@router.post('/get')
async def get_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    gg_injection = service.get_gg_injection_by_pk(gg_injection)
    return  gg_injection

@router.post('/add')
async def add_extra_class(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.add_new_gg_injection(gg_injection)

@router.post('/update')
async def update_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.update_gg_injection(gg_injection)

@router.post('/delete')
async def delete_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.delete_gg_injection(gg_injection)