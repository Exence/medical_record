from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.allergy import AllergyService
from services.auth import get_current_user


router = APIRouter(
    prefix='/allergy',
    tags=['Allergy']
)

@router.post('/get')
async def get_allergyes_by_medcard_num(medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: AllergyService = Depends()):
    allergyes = service.get_allergyes_by_medcard_num(user=user, medcard_num=medcard_num)
    return {"allergyes": allergyes}

@router.post('/add')
async def add_allergy(allergy_data: JsonForm, 
                      medcard_num: int, 
                      user: User = Depends(get_current_user),
                      service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.add_new_allergy(user=user,
                            medcard_num=medcard_num, 
                            allergy=allergy)

@router.post('/update')
async def update_allergy(allergy_data: JsonForm, 
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.update_allergy(user=user, allergy=allergy)

@router.post('/delete')
async def delete_allergy(allergy_data: JsonForm, 
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    allergy = allergy_data.json_data
    service.delete_allergy(user=user, allergy=allergy)
    