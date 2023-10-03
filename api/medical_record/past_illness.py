from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.past_illness import PastIllnessService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/past_illness',
    tags=['Past illness']
)

@router.post('/get')
async def get_past_illness(past_illness_data: JsonForm,
                           user: User = Depends(get_current_user_from_cookie),
                           service: PastIllnessService = Depends()):
    past_illness = past_illness_data.json_data
    past_illness = service.get_past_illness_by_pk(user=user, past_illness_data=past_illness)
    return {"past_illness": past_illness}

@router.post('/add')
async def add_extra_class(past_illness_data: JsonForm,
                          user: User = Depends(get_current_user_from_cookie),
                          service: PastIllnessService = Depends()):
    past_illness = past_illness_data.json_data
    service.add_new_past_illness(user=user, past_illness=past_illness)

@router.post('/update')
async def update_past_illness(past_illness_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: PastIllnessService = Depends()):
    past_illness = past_illness_data.json_data
    service.update_past_illness(user=user, past_illness=past_illness)

@router.post('/delete')
async def delete_past_illness(past_illness_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: PastIllnessService = Depends()):
    past_illness = past_illness_data.json_data
    service.delete_past_illness(user=user, past_illness=past_illness)
