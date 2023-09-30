from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record.allergy import AllergyService


router = APIRouter(
    prefix='/allergy',
    tags=['Allergy']
)

@router.post('/add')
async def add_allergy(allergy_data: JsonForm, medcard_num: int, service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.add_new_allergy(medcard_num, allergy)

@router.post('/update')
async def update_allergy(allergy_data: JsonForm, service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.update_allergy(allergy)

@router.post('/delete')
async def delete_allergy(allergy_data: JsonForm, service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.delete_allergy(allergy)