from fastapi import (
    APIRouter,
    Depends,
)
from models.ongoing_medical_supervision import (
    OngoingMedicalSupervisionPK,
    OngoingMedicalSupervision,
    OngoingMedicalSupervisionCreate,
    OngoingMedicalSupervisionUpdate,
)
from models.user import User
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from services.auth import get_current_user


router = APIRouter(
    prefix='/ongoing_medical_supervision',
    tags=[' Ongoing medical supervision']
)


@router.get('/get_all', response_model=list[OngoingMedicalSupervision])
async def get_ongoing_medical_supervisions_by_medcard_num(medcard_num: int,
                                                          user: User = Depends(
                                                              get_current_user),
                                                          service: OngoingMedicalSupervisionService = Depends()):
    return service.get_ongoing_medical_supervisions_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=OngoingMedicalSupervision)
async def get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK,
                                                user: User = Depends(
                                                    get_current_user),
                                                service: OngoingMedicalSupervisionService = Depends()):
    return service.get_ongoing_medical_supervision_by_pk(user=user, ongoing_medical_supervision_pk=ongoing_medical_supervision_pk)


@router.post('/add', response_model=OngoingMedicalSupervision)
async def add_ongoing_medical_supervision(ongoing_medical_supervision_data: OngoingMedicalSupervisionCreate,
                                          user: User = Depends(
                                              get_current_user),
                                          service: OngoingMedicalSupervisionService = Depends()):
    return service.add_new_ongoing_medical_supervision(user=user, ongoing_medical_supervision_data=ongoing_medical_supervision_data)


@router.post('/update', response_model=OngoingMedicalSupervision)
async def update_ongoing_medical_supervision(ongoing_medical_supervision_data: OngoingMedicalSupervisionUpdate,
                                             user: User = Depends(
                                                 get_current_user),
                                             service: OngoingMedicalSupervisionService = Depends()):
    return service.update_ongoing_medical_supervision(user=user, ongoing_medical_supervision_data=ongoing_medical_supervision_data)


@router.post('/delete')
async def delete_ongoing_medical_supervision(ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK,
                                             user: User = Depends(
                                                 get_current_user),
                                             service: OngoingMedicalSupervisionService = Depends()):
    service.delete_ongoing_medical_supervision(
        user=user, ongoing_medical_supervision_pk=ongoing_medical_supervision_pk)
