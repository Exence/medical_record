from fastapi import (
    APIRouter,
    Depends,
)
from models.catalogs.clinic import (
    ClinicPK,
    Clinic,
    ClinicCreate,
    ClinicUpdate,
)
from models.user import User
from services.catalogs.clinic import ClinicService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/clinics',
    tags=['Clinic']
)


@router.get('/', response_model=list[Clinic])
async def get_clinics(service: ClinicService = Depends()):
    return service.get_all_clinics_as_dict()


@router.get('/{id}', response_model=Clinic)
async def get_clinic_by_id(id: int,
                           medcard_num: int,
user: User = Depends(get_current_user),
                           service: ClinicService = Depends()):
    return service.get_clinic_by_id(id=id)


@router.post('/', response_model=Clinic)
async def add_clinic(clinic_data: ClinicCreate,
                     medcard_num: int,
user: User = Depends(get_current_user),
                     service: ClinicService = Depends()):
    return service.add_new_clinic(clinic_data=clinic_data)


@router.put('/', response_model=Clinic)
async def update_clinic(clinic_data: ClinicUpdate,
                        medcard_num: int,
user: User = Depends(get_current_user),
                        service: ClinicService = Depends()):
    return service.update_clinic(clinic_data=clinic_data)


@router.delete('/')
async def delete_clinic(clinic_pk: ClinicPK,
                        medcard_num: int,
user: User = Depends(get_current_user),
                        service: ClinicService = Depends()):
    service.delete_clinic(clinic_pk=clinic_pk)
