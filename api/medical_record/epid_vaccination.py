from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/epid_vaccination',
    tags=['Epid vaccination']
)

@router.post('/get')
async def get_epid_vaccination(epid_vaccination_data: JsonForm,
                               user: User = Depends(get_current_user),
                               service: VaccinationService = Depends()):
    epid_vaccination = epid_vaccination_data.json_data
    epid_vaccination = service.get_epid_vaccination_by_pk(user=user, epid_vaccination_data=epid_vaccination)
    return epid_vaccination
