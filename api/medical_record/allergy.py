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
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/allergies',
    tags=['Allergy']
)


@router.get('/', response_model=list[Allergy])
async def get_allergies_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: AllergyService = Depends()):
    """
    Получение списка имеющихся у ребенка аллергий по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_allergies_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=Allergy)
async def get_allergy_by_pk(medcard_num: int,
                            allergy_pk: AllergyPK,
                            user: User = Depends(get_current_user),
                            service: AllergyService = Depends()):
    """
    Получение сведений об аллергии по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_allergy_by_pk(allergy_pk=allergy_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Allergy)
async def add_allergy(allergy_data: AllergyCreate,
                      medcard_num: int,
user: User = Depends(get_current_user),
                      service: AllergyService = Depends()):
    """
    Добавление сведений об аллергии
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_allergy(allergy_data=allergy_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=Allergy)
async def update_allergy(allergy_data: AllergyUpdate,
                         medcard_num: int,
user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    """
    Редактирование сведений об аллергии
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_allergy(allergy_data=allergy_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_allergy(allergy_pk: AllergyPK,
                         medcard_num: int,
user: User = Depends(get_current_user),
                         service: AllergyService = Depends()):
    """
    Удаление сведений об аллергии
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        service.delete_allergy(allergy_pk=allergy_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
