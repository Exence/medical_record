from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.extra_class import (
    ExtraClassPK,
    ExtraClass,
    ExtraClassCreate,
    ExtraClassUpdate,
)
from models.user import User
from services.medical_record.extra_class import ExtraClassService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/extra_classes',
    tags=['Extra Class']
)


@router.get('/', response_model=list[ExtraClass])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: ExtraClassService = Depends()):
    """
    Получение списка сведений о дополнительных занятиях по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_extra_classes_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=ExtraClass)
async def get_extra_class_by_pk(extra_class_pk: ExtraClassPK,
                                medcard_num: int,
                                user: User = Depends(get_current_user),
                                service: ExtraClassService = Depends()):
    """
    Получение сведений о дополнительных занятиях по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_extra_class_by_pk(extra_class_pk=extra_class_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=ExtraClass)
async def add_extra_class(extra_class_data: ExtraClassCreate,
                          medcard_num: int,
                          user: User = Depends(get_current_user),
                          service: ExtraClassService = Depends()):
    """
    Добавление сведений о дополнительных занятиях
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_extra_class(extra_class_data=extra_class_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=ExtraClass)
async def update_extra_class(extra_class_data: ExtraClassUpdate,
                             medcard_num: int,
                             user: User = Depends(get_current_user),
                             service: ExtraClassService = Depends()):
    """
    Редактирование сведений о дополнительных занятиях
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_extra_class(extra_class_data=extra_class_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_extra_class(extra_class_pk: ExtraClassPK,
                             medcard_num: int,
                             user: User = Depends(get_current_user),
                             service: ExtraClassService = Depends()):
    """
    Удаление сведений о дополнительных занятиях
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_extra_class(extra_class_pk=extra_class_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
