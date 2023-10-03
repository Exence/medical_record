from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.mantoux_test import MantouxTestService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/mantoux_test',
    tags=['Mantoux test']
)

@router.post('/get')
async def get_mantoux_test(mantoux_test_data: JsonForm,
                           user: User = Depends(get_current_user_from_cookie),
                           service: MantouxTestService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    mantoux_test = service.get_mantoux_test_by_pk(user=user, mantoux_test_data=mantoux_test)
    return  mantoux_test

@router.post('/add')
async def add_extra_class(mantoux_test_data: JsonForm,
                          user: User = Depends(get_current_user_from_cookie),
                          service: MantouxTestService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.add_new_mantoux_test(user=user, mantoux_test=mantoux_test)

@router.post('/update')
async def update_mantoux_test(mantoux_test_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: MantouxTestService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.update_mantoux_test(user=user, mantoux_test=mantoux_test)

@router.post('/delete')
async def delete_mantoux_test(mantoux_test_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: MantouxTestService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.delete_mantoux_test(user=user, mantoux_test=mantoux_test)
