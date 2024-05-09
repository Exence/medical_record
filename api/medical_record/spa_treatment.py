from fastapi import (
    APIRouter,
    Depends,
)
from models.spa_treatment import (
    SpaTreatmentPK,
    SpaTreatment,
    SpaTreatmentCreate,
    SpaTreatmentUpdate,
)
from models.user import User
from services.medical_record.spa_treatment import SpaTreatmentService
from services.auth import get_current_user


router = APIRouter(
    prefix='/spa_treatments',
    tags=['Spa Treatment']
)


@router.get('/', response_model=list[SpaTreatment])
async def get_spa_treatments_by_medcard_num(medcard_num: int,
                                            user: User = Depends(
                                                get_current_user),
                                            service: SpaTreatmentService = Depends()):
    return service.get_spa_treatments_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/one', response_model=SpaTreatment)
async def get_spa_treatment_by_pk(spa_treatment_pk: SpaTreatmentPK,
                                  user: User = Depends(get_current_user),
                                  service: SpaTreatmentService = Depends()):
    return service.get_spa_treatment_by_pk(user=user, spa_treatment_pk=spa_treatment_pk)


@router.post('/', response_model=SpaTreatment)
async def add_spa_treatment(spa_treatment_data: SpaTreatmentCreate,
                            user: User = Depends(get_current_user),
                            service: SpaTreatmentService = Depends()):
    return service.add_new_spa_treatment(user=user, spa_treatment_data=spa_treatment_data)


@router.put('/', response_model=SpaTreatment)
async def update_spa_treatment(spa_treatment_data: SpaTreatmentUpdate,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    return service.update_spa_treatment(user=user, spa_treatment_data=spa_treatment_data)


@router.delete('/')
async def delete_spa_treatment(spa_treatment_pk: SpaTreatmentPK,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    service.delete_spa_treatment(user=user, spa_treatment_pk=spa_treatment_pk)
