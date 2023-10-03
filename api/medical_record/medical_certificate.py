from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.medical_certificate import MedicalCertificateService

from services.auth import get_current_user_from_cookie

router = APIRouter(
    prefix='/medical_certificate',
    tags=['Medical certificate']
)

@router.post('/get')
async def get_medical_certificate(medical_certificate_data: JsonForm,
                                  user: User = Depends(get_current_user_from_cookie),
                                  service: MedicalCertificateService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    medical_certificate = service.get_medical_certificate_by_pk(user=user, medical_certificate_data=medical_certificate)
    return {"medical_certificate": medical_certificate}

@router.post('/add')
async def add_medical_certificate(medical_certificate_data: JsonForm,
                                  user: User = Depends(get_current_user_from_cookie),
                                  service: MedicalCertificateService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.add_new_medical_certificate(user=user, medical_certificate=medical_certificate)

@router.post('/update')
async def update_medical_certificate(medical_certificate_data: JsonForm,
                                     user: User = Depends(get_current_user_from_cookie),
                                     service: MedicalCertificateService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.update_medical_certificate(user=user, medical_certificate=medical_certificate)

@router.post('/delete')
async def delete_medical_certificate(medical_certificate_data: JsonForm,
                                     user: User = Depends(get_current_user_from_cookie),
                                     service: MedicalCertificateService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.delete_medical_certificate(user=user, medical_certificate=medical_certificate)
