from fastapi import (
    APIRouter,
    Depends,
)
from models.extra_class import (
    ExtraClassPK,
    ExtraClass,
    ExtraClassCreate,
    ExtraClassUpdate,
)
from models.user import User
from services.medical_record.extra_class import ExtraClassService
from services.auth import get_current_user


router = APIRouter(
    prefix='/extra_classes',
    tags=['Extra Class']
)


@router.get('/', response_model=list[ExtraClass])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: ExtraClassService = Depends()):
    return service.get_extra_classes_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/one', response_model=ExtraClass)
async def get_extra_class_by_pk(extra_class_pk: ExtraClassPK,
                                user: User = Depends(get_current_user),
                                service: ExtraClassService = Depends()):
    return service.get_extra_class_by_pk(user=user, extra_class_pk=extra_class_pk)


@router.post('/', response_model=ExtraClass)
async def add_extra_class(extra_class_data: ExtraClassCreate,
                          user: User = Depends(get_current_user),
                          service: ExtraClassService = Depends()):
    return service.add_new_extra_class(user=user, extra_class_data=extra_class_data)


@router.put('/', response_model=ExtraClass)
async def update_extra_class(extra_class_data: ExtraClassUpdate,
                             user: User = Depends(get_current_user),
                             service: ExtraClassService = Depends()):
    return service.update_extra_class(user=user, extra_class_data=extra_class_data)


@router.delete('/')
async def delete_extra_class(extra_class_pk: ExtraClassPK,
                             user: User = Depends(get_current_user),
                             service: ExtraClassService = Depends()):
    service.delete_extra_class(user=user, extra_class_pk=extra_class_pk)
