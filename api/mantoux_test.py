from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/mantoux_test',
    tags=['Mantoux test']
)

@router.post('/get')
async def get_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    mantoux_test = service.get_mantoux_test_by_pk(mantoux_test)
    return  mantoux_test

@router.post('/add')
async def add_extra_class(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.add_new_mantoux_test(mantoux_test)

@router.post('/update')
async def update_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.update_mantoux_test(mantoux_test)

@router.post('/delete')
async def delete_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.delete_mantoux_test(mantoux_test)