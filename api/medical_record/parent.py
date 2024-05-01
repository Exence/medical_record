from fastapi import (
    APIRouter,
    Depends,
)

from models.child import ChildPK
from models.parent import (
    Parent,
    ParentCreate,
    ParentTypeRequest,
    ParentUpdate,
)
from models.user import User
from services.medical_record.parent import ParentService
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user


router = APIRouter(
    prefix='/parent',
    tags=['Parent']
)


@router.post('/get_one', response_model=Parent)
async def get_parent_by_type(parent_type: ParentTypeRequest,
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
    return service.add_new_parent(user=user, medcard_num=medcard_num, parent_data=parent_data)


@router.post('/update', response_model=Parent)
async def update_parent(parent_data: ParentUpdate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends()):
    return service.update_parent(user=user, medcard_num=medcard_num, parent_data=parent_data)


@router.post('/delete')
async def delete_parent(parent_type_request: ParentTypeRequest,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends(),
                        medcard_service: MedicalRecordService = Depends()):
    medcard_service.delete_parent_by_type(user=user, medcard_num=medcard_num,
                          parent_type=parent_type_request.parent_type, parent_service=service)
