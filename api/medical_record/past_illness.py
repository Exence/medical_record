from fastapi import (
    APIRouter,
    Depends,
)
from models.past_illness import (
    PastIllnessPK,
    PastIllness,
    PastIllnessCreate,
    PastIllnessUpdate,
)
from models.user import User
from services.medical_record.past_illness import PastIllnessService
from services.auth import get_current_user


router = APIRouter(
    prefix='/past_illness',
    tags=['Past Illness']
)


@router.get('/get_all', response_model=list[PastIllness])
async def get_extra_cas_by_medcard_num(medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: PastIllnessService = Depends()):
    return service.get_past_illnesses_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=PastIllness)
async def get_past_illness_by_pk(past_illness_pk: PastIllnessPK,
                                 user: User = Depends(get_current_user),
                                 service: PastIllnessService = Depends()):
    return service.get_past_illness_by_pk(user=user, past_illness_pk=past_illness_pk)


@router.post('/add', response_model=PastIllness)
async def add_past_illness(past_illness_data: PastIllnessCreate,
                           user: User = Depends(get_current_user),
                           service: PastIllnessService = Depends()):
    return service.add_new_past_illness(user=user, past_illness_data=past_illness_data)


@router.post('/update', response_model=PastIllness)
async def update_past_illness(past_illness_data: PastIllnessUpdate,
                              user: User = Depends(get_current_user),
                              service: PastIllnessService = Depends()):
    return service.update_past_illness(user=user, past_illness_data=past_illness_data)


@router.post('/delete')
async def delete_past_illness(past_illness_pk: PastIllnessPK,
                              user: User = Depends(get_current_user),
                              service: PastIllnessService = Depends()):
    service.delete_past_illness(user=user, past_illness_pk=past_illness_pk)
