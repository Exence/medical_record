from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from models.medical_record.child import ChildPK
from models.medical_record.parent import (
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
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/parents',
    tags=['Parent']
)

@router.get('/', response_model=ParentsResponse)
async def get_parents_by_medcard_num(medcard_num: int,
                                     user: User = Depends(get_current_user),
                                     service: ParentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_parents_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=Parent)
async def add_parent(parent_data: ParentCreate,
                     medcard_num: int,
                     user: User = Depends(get_current_user),
                     service: ParentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_parent(medcard_num=medcard_num, parent_data=parent_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

@router.put('/', response_model=Parent)
async def update_parent(parent_data: ParentUpdate,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_parent(medcard_num=medcard_num, parent_data=parent_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_parent(parent_type_request: ParentTypeRequest,
                        medcard_num: int,
                        user: User = Depends(get_current_user),
                        service: ParentService = Depends(),
                        medcard_service: MedicalRecordService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return medcard_service.delete_parent_by_type(medcard_num=medcard_num,
                                                     parent_type=parent_type_request.parent_type,
                                                     parent_service=service)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
