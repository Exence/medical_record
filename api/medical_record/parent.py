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
    ParentsResponse
)
from models.user import User
from services.medical_record.parent import ParentService
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user


router = APIRouter(
    prefix='/parents',
    tags=['Parent']
)

@router.get('/', response_model=ParentsResponse)
async def get_parents_by_medcard_num( medcard_num: int,
                            user: User = Depends(get_current_user),
                            service: ParentService = Depends()):
    return service.get_parents_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/', response_model=Parent)
async def add_parent(parent_data: ParentCreate,
                     medcard_num: int,
                     user: User = Depends(get_current_user),
                     service: ParentService = Depends()):
    return service.add_new_parent(user=user, medcard_num=medcard_num, parent_data=parent_data)


@router.put('/', response_model=Parent)
async def update_parent(parent_data: ParentUpdate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends()):
    return service.update_parent(user=user, medcard_num=medcard_num, parent_data=parent_data)


@router.delete('/')
async def delete_parent(parent_type_request: ParentTypeRequest,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends(),
                        medcard_service: MedicalRecordService = Depends()):
    medcard_service.delete_parent_by_type(user=user, medcard_num=medcard_num,
                          parent_type=parent_type_request.parent_type, parent_service=service)
