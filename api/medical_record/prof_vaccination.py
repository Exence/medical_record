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
    prefix='/prof_vaccinations',
    tags=['Prof vaccination']
)


@router.post('/one')
async def get_prof_vaccination(prof_vaccination_pk: VaccinationPK,
                               medcard_num: int,
                               user: User = Depends(get_current_user),
                               service: VaccinationService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_prof_vaccination_by_pk(prof_vaccination_pk=prof_vaccination_pk)
        
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    
