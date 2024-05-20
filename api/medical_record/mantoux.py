from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.mantoux import (
    MantouxTestPK,
    MantouxTest,
    MantouxTestCreate,
    MantouxTestUpdate,
)
from models.user import User
from services.medical_record.mantoux import MantouxTestService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/mantoux_tests',
    tags=['MantouxTest']
)


@router.get('/', response_model=list[MantouxTest])
async def get_mantoux_tests_by_medcard_num(medcard_num: int,
                                           user: User = Depends(get_current_user),
                                           service: MantouxTestService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_mantoux_tests_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=MantouxTest)
async def get_mantoux_test_by_pk(mantoux_test_pk: MantouxTestPK,
                                 medcard_num: int,
                                 user: User = Depends(get_current_user),
                                 service: MantouxTestService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_mantoux_test_by_pk(mantoux_test_pk=mantoux_test_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=MantouxTest)
async def add_mantoux_test(mantoux_test_data: MantouxTestCreate,
                           medcard_num: int,
                           user: User = Depends(get_current_user),
                           service: MantouxTestService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_mantoux_test(mantoux_test_data=mantoux_test_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=MantouxTest)
async def update_mantoux_test(mantoux_test_data: MantouxTestUpdate,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: MantouxTestService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_mantoux_test(mantoux_test_data=mantoux_test_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_mantoux_test(mantoux_test_pk: MantouxTestPK,
                              medcard_num: int,
                              user: User = Depends(get_current_user),
                              service: MantouxTestService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_mantoux_test(mantoux_test_pk=mantoux_test_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
