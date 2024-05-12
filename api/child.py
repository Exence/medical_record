from fastapi import (
    APIRouter,
    Depends,
)
from models.child import Child, ChildCreate
from models.user import User
from services.medical_record.medical_record import MedicalRecordService
from services.auth import get_current_user

router = APIRouter(
  prefix='/children',
  tags=['Child']
)


@router.post('/',response_model=Child)
async def add_new_medcard(child_data: ChildCreate,
                          user: User = Depends(get_current_user),
                          service: MedicalRecordService = Depends()):
    return service.add_new_medcard(child_data=child_data)
