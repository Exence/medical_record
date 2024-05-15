from fastapi import (
    APIRouter,
    Depends,
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


router = APIRouter(
    prefix='/prevaccination_checkups',
    tags=['Prevaccination Checkup']
)


@router.get('/', response_model=list[PrevaccinationCheckup])
async def get_prevaccination_checkup_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: PrevaccinationCheckupService = Depends()):
    return service.get_prevaccination_checkups_by_medcard_num(medcard_num=medcard_num)


@router.post('/one', response_model=PrevaccinationCheckup)
async def get_prevaccination_checkup_by_pk(prevaccination_checkup_pk: PrevaccinationCheckupPK,
                                           user: User = Depends(
                                               get_current_user),
                                           service: PrevaccinationCheckupService = Depends()):
    return service.get_prevaccination_checkup_by_pk(prevaccination_checkup_pk=prevaccination_checkup_pk)


@router.post('/', response_model=PrevaccinationCheckup)
async def add_prevaccination_checkup(prevaccination_checkup_data: PrevaccinationCheckupCreate,
                                     user: User = Depends(get_current_user),
                                     service: PrevaccinationCheckupService = Depends()):
    return service.add_new_prevaccination_checkup(prevaccination_checkup_data=prevaccination_checkup_data)


@router.put('/', response_model=PrevaccinationCheckup)
async def update_prevaccination_checkup(prevaccination_checkup_data: PrevaccinationCheckupUpdate,
                                        user: User = Depends(get_current_user),
                                        service: PrevaccinationCheckupService = Depends()):
    return service.update_prevaccination_checkup(prevaccination_checkup_data=prevaccination_checkup_data)


@router.delete('/')
async def delete_prevaccination_checkup(prevaccination_checkup_pk: PrevaccinationCheckupPK,
                                        user: User = Depends(get_current_user),
                                        service: PrevaccinationCheckupService = Depends()):
    service.delete_prevaccination_checkup(prevaccination_checkup_pk=prevaccination_checkup_pk)
