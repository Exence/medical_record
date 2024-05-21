from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.vaccination import VaccinationPK
from models.user import User
from services.medical_record.vaccination import VaccinationService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/epid_vaccinations',
    tags=['Epid vaccination']
)


@router.post('/one')
async def get_epid_vaccination(epid_vaccination_pk: VaccinationPK,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: VaccinationService = Depends()):
    """
    Получение сведений о прививках по показаниям по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_epid_vaccination_by_pk(epid_vaccination_pk=epid_vaccination_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
