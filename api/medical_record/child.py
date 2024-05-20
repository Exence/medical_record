from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.child import Child, ChildCreate, ChildEdit, ChildPK
from models.user import User
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    tags=['Child']
)

@router.get('/', response_model=Child)
async def get_child_by_medcard_num(medcard_num: int,
                                   user: User = Depends(get_current_user),
                                   service: MedicalRecordService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_medcard_by_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

@router.put('/', response_model=Child)
async def update_child(medcard_num: int,
                       medcard_data: ChildEdit,
                       user: User = Depends(get_current_user),
                       service: MedicalRecordService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_medcard(medcard_num=medcard_num, medcard_data=medcard_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_child_by_medcard_num(medcard_num: int,
                                      user: User = Depends(get_current_user),
                                      service: MedicalRecordService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_medcard(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    
