from fastapi import (
    APIRouter,
    Depends,  
)
from models.allergyes import AllergyPK, AllergyCreate, AllergyUpdate
from models.user import User
from services.medical_record.allergy import (
    AllergyService, 
    json_to_allergy_pk, 
    json_to_allergy_create, 
    json_to_allergy_update,
)
from services.auth import get_current_user


router = APIRouter(
    prefix='/allergy',
    tags=['Allergy']
)

@router.get('/get/')
async def get_allergyes_by_medcard_num(medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: AllergyService = Depends()):
    allergyes = service.get_allergyes_by_medcard_num(user=user, medcard_num=medcard_num)
    return {"allergyes": allergyes}

@router.post('/add')
async def add_allergy(allergy: AllergyCreate = Depends(json_to_allergy_create), 
                      user: User = Depends(get_current_user),
                      service: AllergyService = Depends()):
    service.add_new_allergy(user=user, allergy=allergy)

@router.post('/update')
async def update_allergy(allergy: AllergyUpdate = Depends(json_to_allergy_update), 
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    service.update_allergy(user=user, allergy=allergy)

@router.post('/delete')
async def delete_allergy(allergy: AllergyPK = Depends(json_to_allergy_pk), 
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    service.delete_allergy(user=user, allergy=allergy)
    