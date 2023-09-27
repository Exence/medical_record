from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/past_illness',
    tags=['Past illness']
)

@router.post('/get')
async def get_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    past_illness = service.get_past_illness_by_pk(past_illness)
    return {"past_illness": past_illness}

@router.post('/add')
async def add_extra_class(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.add_new_past_illness(past_illness)

@router.post('/update')
async def update_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.update_past_illness(past_illness)

@router.post('/delete')
async def delete_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.delete_past_illness(past_illness)