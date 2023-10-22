from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.spa_treatment import SpaTreatmentService
from services.auth import get_current_user


router = APIRouter(
    prefix='/spa_treatment',
    tags=['Spa treatment']
)

@router.post('/get')
async def get_spa_treatment(spa_treatment_data: JsonForm,
                            user: User = Depends(get_current_user),
                            service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    spa_treatment = service.get_spa_treatment_by_pk(user=user, spa_treatment_data=spa_treatment)
    return {"spa_treatment": spa_treatment}

@router.post('/add')
async def add_extra_class(spa_treatment_data: JsonForm,
                          user: User = Depends(get_current_user),
                          service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.add_new_spa_treatment(user=user, spa_treatment_data=spa_treatment)

@router.post('/update')
async def update_spa_treatment(spa_treatment_data: JsonForm,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.update_spa_treatment(user=user, spa_treatment_data=spa_treatment)

@router.post('/delete')
async def delete_spa_treatment(spa_treatment_data: JsonForm,
                               user: User = Depends(get_current_user),
                               service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.delete_spa_treatment(user=user, spa_treatment_data=spa_treatment)
