from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.allergy import Allergy, AllergyPK, AllergyCreate, AllergyUpdate
from models.user import User
from services.medical_record.allergy import AllergyService
from services.auth import get_current_user


router = APIRouter(
    prefix='/allergies',
    tags=['Allergy']
)


@router.get('/', response_model=list[Allergy])
async def get_allergies_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: AllergyService = Depends()):
    if user:
        return service.get_allergies_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Allergy)
async def get_allergy_by_pk(allergy_pk: AllergyPK,
                            user: User = Depends(get_current_user),
                            service: AllergyService = Depends()):
    return service.get_allergy_by_pk(allergy_pk=allergy_pk)


@router.post('/', response_model=Allergy)
async def add_allergy(allergy_data: AllergyCreate,
                      user: User = Depends(get_current_user),
                      service: AllergyService = Depends()):
    return service.add_new_allergy(allergy_data=allergy_data)


@router.put('/', response_model=Allergy)
async def update_allergy(allergy_data: AllergyUpdate,
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    return service.update_allergy(allergy_data=allergy_data)


@router.delete('/')
async def delete_allergy(allergy_pk: AllergyPK,
                         user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    service.delete_allergy(allergy_pk=allergy_pk)
