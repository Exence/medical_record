from fastapi import (
    APIRouter,
    Depends,
)
from models.medical_examination import MedicalExamination, MedicalExaminationPK, MedicalExaminationCreate, MedicalExaminationUpdate
from models.user import User
from services.medical_record.medical_examination import MedicalExaminationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/medical_examination',
    tags=['MedicalExamination']
)


@router.get('/get_all', response_model=list[MedicalExamination])
async def get_medical_examinations_by_medcard_num(medcard_num: int,
                                                  user: User = Depends(
                                                      get_current_user),
                                                  service: MedicalExaminationService = Depends()):
    return service.get_medical_examinations_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=MedicalExamination)
async def get_medical_examination_by_pk(medical_examination_pk: MedicalExaminationPK,
                                        user: User = Depends(get_current_user),
                                        service: MedicalExaminationService = Depends()):
    return service.get_medical_examination_by_pk(user=user, medical_examination_pk=medical_examination_pk)


@router.post('/add', response_model=MedicalExamination)
async def add_medical_examination(medical_examination_data: MedicalExaminationCreate,
                                  user: User = Depends(get_current_user),
                                  service: MedicalExaminationService = Depends()):
    return service.add_new_medical_examination(user=user, medical_examination_data=medical_examination_data)


@router.post('/update', response_model=MedicalExamination)
async def update_medical_examination(medical_examination_data: MedicalExaminationUpdate,
                                     user: User = Depends(get_current_user),
                                     service: MedicalExaminationService = Depends()):
    return service.update_medical_examination(user=user, medical_examination_data=medical_examination_data)


@router.post('/delete')
async def delete_medical_examination(medical_examination_pk: MedicalExaminationPK,
                                     user: User = Depends(get_current_user),
                                     service: MedicalExaminationService = Depends()):
    service.delete_medical_examination(
        user=user, medical_examination_pk=medical_examination_pk)
