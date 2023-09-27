from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/medical_certificate',
    tags=['Medical certificate']
)

@router.post('/get')
async def get_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    medical_certificate = service.get_medical_certificate_by_pk(medical_certificate)
    return {"medical_certificate": medical_certificate}

@router.post('/add')
async def add_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.add_new_medical_certificate(medical_certificate)

@router.post('/update')
async def update_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.update_medical_certificate(medical_certificate)

@router.post('/delete')
async def delete_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.delete_medical_certificate(medical_certificate)