from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record.visit_specialist_control import VisitSpecialistControlService


router = APIRouter(
    prefix='/visit_specialist_control',
    tags=['Visit specialist control']
)

@router.post('/get_all')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm,  
                                       service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_controls = service.get_visit_specialist_controls_by_dispensary(visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_controls}

@router.post('/get')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm,  
                                       service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_control = service.get_visit_specialist_control_by_pk(visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_control}

@router.post('/add')
async def add_extra_class(visit_specialist_control_data: JsonForm,  
                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.add_new_visit_specialist_control(visit_specialist_control)

@router.post('/update')
async def update_visit_specialist_control(visit_specialist_control_data: JsonForm,  
                                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.update_visit_specialist_control(visit_specialist_control)

@router.post('/delete')
async def delete_visit_specialist_control(visit_specialist_control_data: JsonForm,  
                                          service: VisitSpecialistControlService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.delete_visit_specialist_control(visit_specialist_control)