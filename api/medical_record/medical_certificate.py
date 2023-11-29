from fastapi import (
    APIRouter,
    Depends,  
)
from models.medical_certificate import (
    MedicalCertificatePK,
    MedicalCertificate,
    MedicalCertificateCreate,
    MedicalCertificateUpdate,
)
from models.user import User
from services.medical_record.medical_certificate import MedicalCertificateService
from services.auth import get_current_user


router = APIRouter(
    prefix='/medical_certificate',
    tags=['Medical Certificate']
)

@router.get('/get_all', response_model=list[MedicalCertificate])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: MedicalCertificateService = Depends()):
    return service.get_medical_certificates_by_medcard_num(user=user, medcard_num=medcard_num)

@router.post('/get_one', response_model=MedicalCertificate)
async def get_medical_certificate_by_pk(medical_certificate_pk: MedicalCertificatePK, 
                         user: User = Depends(get_current_user),
                         service: MedicalCertificateService = Depends()):
    return service.get_medical_certificate_by_pk(user=user, medical_certificate_pk=medical_certificate_pk)

@router.post('/add', response_model=MedicalCertificate)
async def add_medical_certificate(medical_certificate_data: MedicalCertificateCreate, 
                      user: User = Depends(get_current_user),
                      service: MedicalCertificateService = Depends()):
    return service.add_new_medical_certificate(user=user, medical_certificate_data=medical_certificate_data)

@router.post('/update', response_model=MedicalCertificate)
async def update_medical_certificate(medical_certificate_data: MedicalCertificateUpdate, 
                         user: User = Depends(get_current_user),
                         service: MedicalCertificateService = Depends()):
    return service.update_medical_certificate(user=user, medical_certificate_data=medical_certificate_data)

@router.post('/delete')
async def delete_medical_certificate(medical_certificate_pk: MedicalCertificatePK, 
                         user: User = Depends(get_current_user),
                         service: MedicalCertificateService = Depends()):
    service.delete_medical_certificate(user=user, medical_certificate_pk=medical_certificate_pk)
