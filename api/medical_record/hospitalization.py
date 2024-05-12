from fastapi import (
    APIRouter,
    Depends,
)
from models.hospitalization import (
    HospitalizationPK,
    Hospitalization,
    HospitalizationCreate,
    HospitalizationUpdate,
)
from models.user import User
from services.medical_record.hospitalization import HospitalizationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/hospitalizations',
    tags=['Hospitalization']
)


@router.get('/', response_model=list[Hospitalization])
async def get_hospitalizations_by_medcard_num(medcard_num: int,
                                              user: User = Depends(
                                                  get_current_user),
                                              service: HospitalizationService = Depends()):
    return service.get_hospitalizations_by_medcard_num(medcard_num=medcard_num)


@router.post('/one', response_model=Hospitalization)
async def get_hospitalization_by_pk(hospitalization_pk: HospitalizationPK,
                                    user: User = Depends(get_current_user),
                                    service: HospitalizationService = Depends()):
    return service.get_hospitalization_by_pk(hospitalization_pk=hospitalization_pk)


@router.post('/', response_model=Hospitalization)
async def add_hospitalization(hospitalization_data: HospitalizationCreate,
                              user: User = Depends(get_current_user),
                              service: HospitalizationService = Depends()):
    return service.add_new_hospitalization(hospitalization_data=hospitalization_data)


@router.put('/', response_model=Hospitalization)
async def update_hospitalization(hospitalization_data: HospitalizationUpdate,
                                 user: User = Depends(get_current_user),
                                 service: HospitalizationService = Depends()):
    return service.update_hospitalization(hospitalization_data=hospitalization_data)


@router.delete('/')
async def delete_hospitalization(hospitalization_pk: HospitalizationPK,
                                 user: User = Depends(get_current_user),
                                 service: HospitalizationService = Depends()):
    service.delete_hospitalization(hospitalization_pk=hospitalization_pk)
