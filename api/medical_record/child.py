from fastapi import (
    APIRouter,
    Depends,
)
from models.child import Child, ChildCreate, ChildEdit, ChildPK
from models.user import User
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user


router = APIRouter(
    tags=['Child']
)

@router.get('/', response_model=Child)
async def get_child_by_medcard_num(medcard_num: int,
                                   user: User = Depends(get_current_user),
                                   service: MedicalRecordService = Depends()):
    return service.get_medcard_by_num(user=user, medcard_num=medcard_num)

@router.put('/', response_model=Child)
async def update_child(medcard_num: int,
                       medcard_data: ChildEdit,
                        user: User = Depends(get_current_user),
                        service: MedicalRecordService = Depends()):
    return service.update_medcard(user=user, medcard_num=medcard_num, medcard_data=medcard_data)

@router.delete('/')
async def delete_child_by_medcard_num(medcard_num: int,
                                      user: User = Depends(get_current_user),
                                      service: MedicalRecordService = Depends()):
    return service.delete_medcard(user=user, medcard_num=medcard_num)
