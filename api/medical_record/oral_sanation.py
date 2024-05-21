from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.oral_sanation import (
    OralSanationPK,
    OralSanation,
    OralSanationCreate,
    OralSanationUpdate,
)
from models.user import User
from services.medical_record.oral_sanation import OralSanationService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/oral_sanations',
    tags=['OralSanation']
)


@router.get('/', response_model=list[OralSanation])
async def get_oral_sanations_by_medcard_num(medcard_num: int,
                                            user: User = Depends(get_current_user),
                                            service: OralSanationService = Depends()):
    """
    Получение списка сведений о санации полости рта по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_oral_sanations_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=OralSanation)
async def get_oral_sanation_by_pk(oral_sanation_pk: OralSanationPK,
                                  medcard_num: int,
                                  user: User = Depends(get_current_user),
                                  service: OralSanationService = Depends()):
    """
    Получение сведений о санации полости рта по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_oral_sanation_by_pk(oral_sanation_pk=oral_sanation_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=OralSanation)
async def add_oral_sanation(oral_sanation_data: OralSanationCreate,
                            medcard_num: int,
                            user: User = Depends(get_current_user),
                            service: OralSanationService = Depends()):
    """
    Добавление сведений о санации полости рта
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_oral_sanation(oral_sanation_data=oral_sanation_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=OralSanation)
async def update_oral_sanation(oral_sanation_data: OralSanationUpdate,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: OralSanationService = Depends()):
    """
    Редактирование сведений о санации полости рта
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_oral_sanation(oral_sanation_data=oral_sanation_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_oral_sanation(oral_sanation_pk: OralSanationPK,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: OralSanationService = Depends()):
    """
    Удаление сведений о санации полости рта
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_oral_sanation(oral_sanation_pk=oral_sanation_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
