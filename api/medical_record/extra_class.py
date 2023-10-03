from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.extra_class import ExtraClassService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/extra_class',
    tags=['Extra class']
)

@router.post('/add')
async def add_extra_class(extra_class_data: JsonForm,
                          user: User = Depends(get_current_user_from_cookie),
                          service: ExtraClassService = Depends()):
    extra_class = extra_class_data.json_data
    service.add_new_extra_class(user=user, extra_class=extra_class)

@router.post('/update')
async def update_extra_class(extra_class_data: JsonForm,
                             user: User = Depends(get_current_user_from_cookie),
                             service: ExtraClassService = Depends()):
    extra_class = extra_class_data.json_data
    service.update_extra_class(user=user, extra_class=extra_class)

@router.post('/delete')
async def delete_extra_class(extra_class_data: JsonForm,
                             user: User = Depends(get_current_user_from_cookie),
                             service: ExtraClassService = Depends()):
    extra_class = extra_class_data.json_data
    service.delete_extra_class(user=user, extra_class=extra_class)
