from fastapi import (
    APIRouter,
    Depends,  
)
from models.vaccination import VaccinationPK
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/prof_vaccination',
    tags=['Prof vaccination']
)

@router.post('/get_one')
async def get_prof_vaccination(prof_vaccination_pk: VaccinationPK,
                               user: User = Depends(get_current_user),
                               service: VaccinationService = Depends()):
    prof_vaccination = service.get_prof_vaccination_by_pk(user=user, prof_vaccination_pk=prof_vaccination_pk)
    return prof_vaccination
