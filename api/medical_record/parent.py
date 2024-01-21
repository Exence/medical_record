from fastapi import (
    APIRouter,
    Depends,
)

from models.child import ChildPK
from models.parent import (
    Parent,
    ParentCreate,
    PatentType,
    ParentUpdate,
)
from models.user import User
from services.medical_record.parent import ParentService
from services.auth import get_current_user


router = APIRouter(
    prefix='/parent',
    tags=['Parent']
)


@router.post('/get_one', response_model=Parent)
async def get_parent_by_type(parent_type: PatentType,
                             medcard_num: int,
                             user: User = Depends(get_current_user),
                             service: ParentService = Depends()):
    child_pk = ChildPK(medcard_num=medcard_num)
    return service.get_parent_by_type(user=user, child_pk=child_pk, parent_type=parent_type)


@router.post('/add', response_model=Parent)
async def add_parent(parent_data: ParentCreate,
                     medcard_num: int,
                     user: User = Depends(get_current_user),
                     service: ParentService = Depends()):
    child_pk = ChildPK(medcard_num=medcard_num)
    return service.add_or_update_parent(user=user, child_pk=child_pk, parent_data=parent_data)


@router.post('/update', response_model=Parent)
async def update_parent(parent_data: ParentCreate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends()):
    child_pk = ChildPK(medcard_num=medcard_num)
    return service.add_or_update_parent(user=user, child_pk=child_pk, parent_data=parent_data)


@router.post('/delete')
async def delete_parent(parent_type: PatentType,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends()):
    child_pk = ChildPK(medcard_num=medcard_num)
    service.delete_parent(user=user, child_pk=child_pk,
                          parent_type=parent_type)
