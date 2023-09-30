from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from services.medical_record.vaccination import VaccinationService


router = APIRouter(
    prefix='/epid_vaccination',
    tags=['Epid vaccination']
)

@router.post('/get')
async def get_epid_vaccination(epid_vaccination_data: JsonForm,  service: VaccinationService = Depends()):
    epid_vaccination = epid_vaccination_data.json_data
    epid_vaccination = service.get_epid_vaccination_by_pk(epid_vaccination)
    return epid_vaccination