from fastapi import (
    APIRouter,
    Depends,
)
from models.vaccination import VaccinationPK
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user


router = APIRouter(
    prefix='/epid_vaccination',
    tags=['Epid vaccination']
)


@router.post('/get_one')
async def get_epid_vaccination(epid_vaccination_pk: VaccinationPK,
                               user: User = Depends(get_current_user),
                               service: VaccinationService = Depends()):
    epid_vaccination = service.get_epid_vaccination_by_pk(
        user=user, epid_vaccination_pk=epid_vaccination_pk)
    return epid_vaccination
