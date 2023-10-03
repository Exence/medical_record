from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/prof_vaccination',
    tags=['Prof vaccination']
)

@router.post('/get')
async def get_prof_vaccination(prof_vaccination_data: JsonForm,
                               user: User = Depends(get_current_user_from_cookie),
                               service: VaccinationService = Depends()):
    prof_vaccination = prof_vaccination_data.json_data
    prof_vaccination = service.get_prof_vaccination_by_pk(user=user, prof_vaccination_data=prof_vaccination)
    return prof_vaccination
