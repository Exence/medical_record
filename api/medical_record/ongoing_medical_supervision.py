from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.ongoing_medical_supervision import (
    OngoingMedicalSupervisionPK,
    OngoingMedicalSupervision,
    OngoingMedicalSupervisionCreate,
    OngoingMedicalSupervisionUpdate,
)
from models.user import User
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/ongoing_medical_supervisions',
    tags=[' Ongoing medical supervision']
)


@router.get('/', response_model=list[OngoingMedicalSupervision])
async def get_ongoing_medical_supervisions_by_medcard_num(medcard_num: int,
                                                          user: User = Depends(get_current_user),
                                                          service: OngoingMedicalSupervisionService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_ongoing_medical_supervisions_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=OngoingMedicalSupervision)
async def get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK,
                                                medcard_num: int,
                                                user: User = Depends(get_current_user),
                                                service: OngoingMedicalSupervisionService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision_pk=ongoing_medical_supervision_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=OngoingMedicalSupervision)
async def add_ongoing_medical_supervision(ongoing_medical_supervision_data: OngoingMedicalSupervisionCreate,
                                          medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: OngoingMedicalSupervisionService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_ongoing_medical_supervision(ongoing_medical_supervision_data=ongoing_medical_supervision_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=OngoingMedicalSupervision)
async def update_ongoing_medical_supervision(ongoing_medical_supervision_data: OngoingMedicalSupervisionUpdate,
                                             medcard_num: int,
                                             user: User = Depends(get_current_user),
                                             service: OngoingMedicalSupervisionService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_ongoing_medical_supervision(ongoing_medical_supervision_data=ongoing_medical_supervision_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_ongoing_medical_supervision(ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK,
                                             medcard_num: int,
                                             user: User = Depends(get_current_user),
                                             service: OngoingMedicalSupervisionService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_ongoing_medical_supervision(ongoing_medical_supervision_pk=ongoing_medical_supervision_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
