from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/extra_class',
    tags=['Extra class']
)

@router.post('/add')
async def add_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.add_new_extra_class(extra_class)

@router.post('/update')
async def update_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.update_extra_class(extra_class)

@router.post('/delete')
async def delete_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.delete_extra_class(extra_class)