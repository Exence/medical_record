from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from models.medical_record.medical_examination import (
    MedicalExamination,
    MedicalExaminationPK, 
    MedicalExaminationCreate, 
    MedicalExaminationUpdate,
)
from models.user import User
from services.medical_record.medical_examination import MedicalExaminationService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/medical_examinations',
    tags=['MedicalExamination']
)


@router.get('/', response_model=list[MedicalExamination])
async def get_medical_examinations_by_medcard_num(medcard_num: int,
                                                  user: User = Depends(get_current_user),
                                                  service: MedicalExaminationService = Depends()):
    """
    Получение списка сведений о плановых медицинских осмотрах по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_medical_examinations_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=MedicalExamination)
async def get_medical_examination_by_pk(medical_examination_pk: MedicalExaminationPK,
                                        medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: MedicalExaminationService = Depends()):
    """
    Получение сведений о плановом медицинском осмотре по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_medical_examination_by_pk(medical_examination_pk=medical_examination_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=MedicalExamination)
async def add_medical_examination(medical_examination_data: MedicalExaminationCreate,
                                  medcard_num: int,
                                  user: User = Depends(get_current_user),
                                  service: MedicalExaminationService = Depends()):
    """
    Добавление сведений о плановом медицинском осмотре
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_medical_examination(medical_examination_data=medical_examination_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=MedicalExamination)
async def update_medical_examination(medical_examination_data: MedicalExaminationUpdate,
                                     medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: MedicalExaminationService = Depends()):
    """
    Редактирование сведений о плановом медицинском осмотре
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_medical_examination(medical_examination_data=medical_examination_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_medical_examination(medical_examination_pk: MedicalExaminationPK,
                                     medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: MedicalExaminationService = Depends()):
    """
    Удаление сведений о плановом медицинском осмотре
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_medical_examination(medical_examination_pk=medical_examination_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
