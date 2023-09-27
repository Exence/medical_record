from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/medical_examination',
    tags=['Medical examination']
)

@router.post('/get')
async def get_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    medical_examination = service.get_medical_examination_by_pk(medical_examination)
    return  medical_examination

@router.post('/add')
async def add_extra_class(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    age = service.add_new_medical_examination(medical_examination)
    return {"age": age}

@router.post('/update')
async def update_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    age = service.update_medical_examination(medical_examination)
    return {"age": age}

@router.post('/delete')
async def delete_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    service.delete_medical_examination(medical_examination)
