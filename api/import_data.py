from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
)
from models.user import User
from services.auth import get_current_user
from services.import_data import import_from_xlsx
from services.catalogs.clinic import ClinicService
from services.medical_record.medical_record import MedicalRecordService
from services.medical_record.parent import ParentService


router = APIRouter(
    prefix='/medical_record/import',
    tags=['Import from xlsx']
)

@router.get('/')
def import_data_from_xlsx(request: Request,
                          user: User = Depends(get_current_user),
                          medcard_service: MedicalRecordService = Depends(),
                          clinic_service: ClinicService = Depends(),
                          parent_service: ParentService = Depends()):
    import_from_xlsx(filename="./static/files/1.xlsx", 
                     kindergarten_num=user.kindergarten_num,
                     medcard_service=medcard_service,
                     clinic_service=clinic_service,
                     parent_service=parent_service)