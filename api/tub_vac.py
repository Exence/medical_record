from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/tub_vac',
    tags=['Tuberculosis vaccination']
)

@router.post('/get')
async def get_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    tub_vac = service.get_tub_vac_by_pk(tub_vac)
    return  tub_vac

@router.post('/add')
async def add_extra_class(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.add_new_tub_vac(tub_vac)

@router.post('/update')
async def update_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.update_tub_vac(tub_vac)

@router.post('/delete')
async def delete_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.delete_tub_vac(tub_vac)