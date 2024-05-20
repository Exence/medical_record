from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.prevaccination_checkup import (
    PrevaccinationCheckupPK,
    PrevaccinationCheckup,
    PrevaccinationCheckupCreate,
    PrevaccinationCheckupUpdate,
)
from models.user import User
from services.medical_record.prevaccination_checkup import PrevaccinationCheckupService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/prevaccination_checkups',
    tags=['Prevaccination Checkup']
)


@router.get('/', response_model=list[PrevaccinationCheckup])
async def get_prevaccination_checkup_by_medcard_num(medcard_num: int,
                                                    user: User = Depends(get_current_user),
                                                    service: PrevaccinationCheckupService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_prevaccination_checkups_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=PrevaccinationCheckup)
async def get_prevaccination_checkup_by_pk(prevaccination_checkup_pk: PrevaccinationCheckupPK,
                                           medcard_num: int,
                                           user: User = Depends(get_current_user),
                                           service: PrevaccinationCheckupService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_prevaccination_checkup_by_pk(prevaccination_checkup_pk=prevaccination_checkup_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=PrevaccinationCheckup)
async def add_prevaccination_checkup(prevaccination_checkup_data: PrevaccinationCheckupCreate,
                                     medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: PrevaccinationCheckupService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_prevaccination_checkup(prevaccination_checkup_data=prevaccination_checkup_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=PrevaccinationCheckup)
async def update_prevaccination_checkup(prevaccination_checkup_data: PrevaccinationCheckupUpdate,
                                        medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: PrevaccinationCheckupService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_prevaccination_checkup(prevaccination_checkup_data=prevaccination_checkup_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        ) 


@router.delete('/')
async def delete_prevaccination_checkup(prevaccination_checkup_pk: PrevaccinationCheckupPK,
                                        medcard_num: int,
                                        user: User = Depends(get_current_user),
                                        service: PrevaccinationCheckupService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_prevaccination_checkup(prevaccination_checkup_pk=prevaccination_checkup_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
