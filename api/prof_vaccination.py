from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/prof_vaccination',
    tags=['Prof vaccination']
)

@router.post('/get')
async def get_prof_vaccination(prof_vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    prof_vaccination = prof_vaccination_data.json_data
    prof_vaccination = service.get_prof_vaccination_by_pk(prof_vaccination)
    return prof_vaccination