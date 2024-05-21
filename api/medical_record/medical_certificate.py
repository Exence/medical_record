from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.medical_certificate import (
    MedicalCertificatePK,
    MedicalCertificate,
    MedicalCertificateCreate,
    MedicalCertificateUpdate,
)
from models.user import User
from services.medical_record.medical_certificate import MedicalCertificateService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/medical_certificates',
    tags=['Medical Certificate']
)


@router.get('/', response_model=list[MedicalCertificate])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: MedicalCertificateService = Depends()):
    """
    Получение списка сведений о справках от врача по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_medical_certificates_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=MedicalCertificate)
async def get_medical_certificate_by_pk(medical_certificate_pk: MedicalCertificatePK,
                                        medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: MedicalCertificateService = Depends()):
    """
    Получение сведений о справках от врача по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_medical_certificate_by_pk(medical_certificate_pk=medical_certificate_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=MedicalCertificate)
async def add_medical_certificate(medical_certificate_data: MedicalCertificateCreate,
                                  medcard_num: int,
                                  user: User = Depends(get_current_user),
                                  service: MedicalCertificateService = Depends()):
    """
    Добавление сведений о справках от врача
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_medical_certificate(medical_certificate_data=medical_certificate_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=MedicalCertificate)
async def update_medical_certificate(medical_certificate_data: MedicalCertificateUpdate,
                                     medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: MedicalCertificateService = Depends()):
    """
    Редактирование сведений о справках от врача
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_medical_certificate(medical_certificate_data=medical_certificate_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_medical_certificate(medical_certificate_pk: MedicalCertificatePK,
                                     medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: MedicalCertificateService = Depends()):
    """
    Удаление сведений о справках от врача
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_medical_certificate(medical_certificate_pk=medical_certificate_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
