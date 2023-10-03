from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.visit_specialist_control import VisitSpecialistControlService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/visit_specialist_control',
    tags=['Visit specialist control']
)

@router.post('/get_all')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm, 
                                       user: User = Depends(get_current_user_from_cookie), 
                                       service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_controls = service.get_visit_specialist_controls_by_dispensary(user=user, visit_specialist_control_data=visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_controls}

@router.post('/get')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm,  
                                       user: User = Depends(get_current_user_from_cookie),
                                       service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_control = service.get_visit_specialist_control_by_pk(user=user, visit_specialist_control_data=visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_control}

@router.post('/add')
async def add_extra_class(visit_specialist_control_data: JsonForm, 
                          user: User = Depends(get_current_user_from_cookie), 
                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.add_new_visit_specialist_control(user=user, visit_specialist_control=visit_specialist_control)

@router.post('/update')
async def update_visit_specialist_control(visit_specialist_control_data: JsonForm, 
                                          user: User = Depends(get_current_user_from_cookie), 
                                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.update_visit_specialist_control(user=user, visit_specialist_control=visit_specialist_control)

@router.post('/delete')
async def delete_visit_specialist_control(visit_specialist_control_data: JsonForm, 
                                          user: User = Depends(get_current_user_from_cookie), 
                                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.delete_visit_specialist_control(user=user, visit_specialist_control=visit_specialist_control)
