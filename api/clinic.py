from fastapi import (
    APIRouter,
    Depends,
)
from models.clinic import (
    ClinicPK,
    Clinic,
    ClinicCreate,
    ClinicUpdate,
)
from models.user import User
from services.clinic import ClinicService
from services.auth import get_current_user


router = APIRouter(
    prefix='/clinic',
    tags=['Clinic']
)


@router.get('/get_all', response_model=list[Clinic])
async def get_clinics(service: ClinicService = Depends()):
    return service.get_all_clinics_as_dict()


@router.post('/get_one', response_model=Clinic)
async def get_clinic_by_id(id: int,
                           user: User = Depends(get_current_user),
                           service: ClinicService = Depends()):
    return service.get_clinic_by_id(id=id)


@router.post('/add', response_model=Clinic)
async def add_clinic(clinic_data: ClinicCreate,
                     user: User = Depends(get_current_user),
                     service: ClinicService = Depends()):
    return service.add_new_clinic(user=user, clinic_data=clinic_data)


@router.post('/update', response_model=Clinic)
async def update_clinic(clinic_data: ClinicUpdate,
                        user: User = Depends(get_current_user),
                        service: ClinicService = Depends()):
    return service.update_clinic(user=user, clinic_data=clinic_data)


@router.post('/delete')
async def delete_clinic(clinic_pk: ClinicPK,
                        user: User = Depends(get_current_user),
                        service: ClinicService = Depends()):
    service.delete_clinic(user=user, clinic_pk=clinic_pk)
