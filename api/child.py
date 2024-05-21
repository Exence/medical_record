from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.child import Child, ChildCreate
from models.user import User
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard

router = APIRouter(
  prefix='/children',
  tags=['Child']
)


@router.post('/',response_model=Child)
async def add_new_medcard(child_data: ChildCreate,
                          medcard_num: int,
user: User = Depends(get_current_user),
                          service: MedicalRecordService = Depends()):
    """
    Добавление новой медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_medcard(child_data=child_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
