from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/parent',
    tags=['Parent']
)

@router.post('/add')
async def update_parent(parent_data: JsonForm,  service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    parent_id = service.add_parent(parent)
    return {"id": parent_id}

@router.post('/update')
async def update_parent(parent_data: JsonForm, service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    service.update_parent(parent)

@router.post('/delete')
async def delete_parent(parent_data: JsonForm, service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    service.delete_parent(parent)