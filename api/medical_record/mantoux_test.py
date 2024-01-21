from fastapi import (
    APIRouter,
    Depends,
)
from models.mantoux_test import (
    MantouxTestPK,
    MantouxTest,
    MantouxTestCreate,
    MantouxTestUpdate,
)
from models.user import User
from services.medical_record.mantoux_test import MantouxTestService
from services.auth import get_current_user


router = APIRouter(
    prefix='/mantoux_test',
    tags=['MantouxTest']
)


@router.get('/get_all', response_model=list[MantouxTest])
async def get_mantoux_tests_by_medcard_num(medcard_num: int,
                                           user: User = Depends(
                                               get_current_user),
                                           service: MantouxTestService = Depends()):
    return service.get_mantoux_tests_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/get_one', response_model=MantouxTest)
async def get_mantoux_test_by_pk(mantoux_test_pk: MantouxTestPK,
                                 user: User = Depends(get_current_user),
                                 service: MantouxTestService = Depends()):
    return service.get_mantoux_test_by_pk(user=user, mantoux_test_pk=mantoux_test_pk)


@router.post('/add', response_model=MantouxTest)
async def add_mantoux_test(mantoux_test_data: MantouxTestCreate,
                           user: User = Depends(get_current_user),
                           service: MantouxTestService = Depends()):
    return service.add_new_mantoux_test(user=user, mantoux_test_data=mantoux_test_data)


@router.post('/update', response_model=MantouxTest)
async def update_mantoux_test(mantoux_test_data: MantouxTestUpdate,
                              user: User = Depends(get_current_user),
                              service: MantouxTestService = Depends()):
    return service.update_mantoux_test(user=user, mantoux_test_data=mantoux_test_data)


@router.post('/delete')
async def delete_mantoux_test(mantoux_test_pk: MantouxTestPK,
                              user: User = Depends(get_current_user),
                              service: MantouxTestService = Depends()):
    service.delete_mantoux_test(user=user, mantoux_test_pk=mantoux_test_pk)
