from fastapi import (
    APIRouter,
    Depends,
)
from models.visit_specialist_control import (
    VisitSpecialistControlMain,
    VisitSpecialistControlPK,
    VisitSpecialistControl,
    VisitSpecialistControlCreate,
    VisitSpecialistControlUpdate,
)
from models.user import User
from services.medical_record.visit_specialist_control import VisitSpecialistControlService
from services.auth import get_current_user


router = APIRouter(
    prefix='/visit_specialist_controls',
    tags=['Visit specialist control']
)


@router.post('/all')
async def get_visit_specialist_control(visit_specialist_control: VisitSpecialistControlMain,
                                       user: User = Depends(get_current_user),
                                       service: VisitSpecialistControlService = Depends()):
    return service.get_visit_specialist_controls_by_dispensary(user=user, visit_specialist_control=visit_specialist_control)


@router.post('/one')
async def get_visit_specialist_control(visit_specialist_control_pk: VisitSpecialistControlPK,
                                       user: User = Depends(get_current_user),
                                       service: VisitSpecialistControlService = Depends()):
    return service.get_visit_specialist_control_by_pk(user=user, visit_specialist_control_pk=visit_specialist_control_pk)


@router.post('/')
async def add_extra_class(visit_specialist_control: VisitSpecialistControlCreate,
                          user: User = Depends(get_current_user),
                          service: VisitSpecialistControlService = Depends()):
    service.add_new_visit_specialist_control(
        user=user, visit_specialist_control_data=visit_specialist_control)


@router.put('/')
async def update_visit_specialist_control(visit_specialist_control: VisitSpecialistControlUpdate,
                                          user: User = Depends(
                                              get_current_user),
                                          service: VisitSpecialistControlService = Depends()):
    service.update_visit_specialist_control(
        user=user, visit_specialist_control_data=visit_specialist_control)


@router.delete('/')
async def delete_visit_specialist_control(visit_specialist_control_pk: VisitSpecialistControlPK,
                                          user: User = Depends(
                                              get_current_user),
                                          service: VisitSpecialistControlService = Depends()):
    service.delete_visit_specialist_control(
        user=user, visit_specialist_control_pk=visit_specialist_control_pk)
