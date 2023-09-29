from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.spa_treatment import SpaTreatmentService


router = APIRouter(
    prefix='/spa_treatment',
    tags=['Spa treatment']
)

@router.post('/get')
async def get_spa_treatment(spa_treatment_data: JsonForm,  service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    spa_treatment = service.get_spa_treatment_by_pk(spa_treatment)
    return {"spa_treatment": spa_treatment}

@router.post('/add')
async def add_extra_class(spa_treatment_data: JsonForm,  service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.add_new_spa_treatment(spa_treatment)

@router.post('/update')
async def update_spa_treatment(spa_treatment_data: JsonForm,  service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.update_spa_treatment(spa_treatment)

@router.post('/delete')
async def delete_spa_treatment(spa_treatment_data: JsonForm,  service: SpaTreatmentService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.delete_spa_treatment(spa_treatment)