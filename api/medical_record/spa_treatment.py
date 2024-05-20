from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.spa_treatment import (
    SpaTreatmentPK,
    SpaTreatment,
    SpaTreatmentCreate,
    SpaTreatmentUpdate,
)
from models.user import User
from services.medical_record.spa_treatment import SpaTreatmentService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/spa_treatments',
    tags=['Spa Treatment']
)


@router.get('/', response_model=list[SpaTreatment])
async def get_spa_treatments_by_medcard_num(medcard_num: int,
                                            user: User = Depends(get_current_user),
                                            service: SpaTreatmentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_spa_treatments_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=SpaTreatment)
async def get_spa_treatment_by_pk(spa_treatment_pk: SpaTreatmentPK,
                                  medcard_num: int,
                                  user: User = Depends(get_current_user),
                                  service: SpaTreatmentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_spa_treatment_by_pk(spa_treatment_pk=spa_treatment_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=SpaTreatment)
async def add_spa_treatment(spa_treatment_data: SpaTreatmentCreate,
                            medcard_num: int,
                            user: User = Depends(get_current_user),
                            service: SpaTreatmentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_spa_treatment(spa_treatment_data=spa_treatment_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=SpaTreatment)
async def update_spa_treatment(spa_treatment_data: SpaTreatmentUpdate,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_spa_treatment(spa_treatment_data=spa_treatment_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_spa_treatment(spa_treatment_pk: SpaTreatmentPK,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_spa_treatment(spa_treatment_pk=spa_treatment_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
