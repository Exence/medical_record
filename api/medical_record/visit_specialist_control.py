from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.visit_specialist_control import (
    VisitSpecialistControlMain,
    VisitSpecialistControlPK,
    VisitSpecialistControl,
    VisitSpecialistControlCreate,
    VisitSpecialistControlUpdate,
)
from models.user import User
from services.medical_record.visit_specialist_control import VisitSpecialistControlService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/visit_specialist_controls',
    tags=['Visit specialist control']
)


@router.post('/all')
async def get_visit_specialist_control(visit_specialist_control: VisitSpecialistControlMain,
                                       medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: VisitSpecialistControlService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_visit_specialist_controls_by_dispensary(visit_specialist_control=visit_specialist_control)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one')
async def get_visit_specialist_control(visit_specialist_control_pk: VisitSpecialistControlPK,
                                       medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: VisitSpecialistControlService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_visit_specialist_control_by_pk(visit_specialist_control_pk=visit_specialist_control_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/')
async def add_extra_class(visit_specialist_control: VisitSpecialistControlCreate,
                          medcard_num: int,
                          user: User = Depends(get_current_user),
                          service: VisitSpecialistControlService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_visit_specialist_control(visit_specialist_control_data=visit_specialist_control)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/')
async def update_visit_specialist_control(visit_specialist_control: VisitSpecialistControlUpdate,
                                          medcard_num: int,
                                          user: User = Depends(
                                              get_current_user),
                                          service: VisitSpecialistControlService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_visit_specialist_control(visit_specialist_control_data=visit_specialist_control)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_visit_specialist_control(visit_specialist_control_pk: VisitSpecialistControlPK,
                                          medcard_num: int,
                                          user: User = Depends(
                                              get_current_user),
                                          service: VisitSpecialistControlService = Depends()):
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_visit_specialist_control(visit_specialist_control_pk=visit_specialist_control_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
