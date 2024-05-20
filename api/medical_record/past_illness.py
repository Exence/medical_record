from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.past_illness import (
    PastIllnessPK,
    PastIllness,
    PastIllnessCreate,
    PastIllnessUpdate,
)
from models.user import User
from services.medical_record.past_illness import PastIllnessService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/past_illnesses',
    tags=['Past Illness']
)


@router.get('/', response_model=list[PastIllness])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: PastIllnessService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_past_illnesses_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=PastIllness)
async def get_past_illness_by_pk(past_illness_pk: PastIllnessPK,
                                 medcard_num: int,
                                 user: User = Depends(get_current_user),
                                 service: PastIllnessService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_past_illness_by_pk(past_illness_pk=past_illness_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=PastIllness)
async def add_past_illness(past_illness_data: PastIllnessCreate,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: PastIllnessService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_past_illness(past_illness_data=past_illness_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=PastIllness)
async def update_past_illness(past_illness_data: PastIllnessUpdate,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: PastIllnessService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_past_illness(past_illness_data=past_illness_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_past_illness(past_illness_pk: PastIllnessPK,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: PastIllnessService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_past_illness(past_illness_pk=past_illness_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
