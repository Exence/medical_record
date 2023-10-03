from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.gg_injection import GammaGlobulinInjectionService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/gg_injection',
    tags=['Gamma-globulin injection']
)

@router.post('/get')
async def get_gg_injection(gg_injection_data: JsonForm,
                           user: User = Depends(get_current_user_from_cookie),
                           service: GammaGlobulinInjectionService = Depends()):
    gg_injection = gg_injection_data.json_data
    gg_injection = service.get_gg_injection_by_pk(user=user, gg_injection_data=gg_injection)
    return  gg_injection

@router.post('/add')
async def add_extra_class(gg_injection_data: JsonForm,
                          user: User = Depends(get_current_user_from_cookie),
                          service: GammaGlobulinInjectionService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.add_new_gg_injection(user=user, gg_injection=gg_injection)

@router.post('/update')
async def update_gg_injection(gg_injection_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: GammaGlobulinInjectionService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.update_gg_injection(user=user, gg_injection=gg_injection)

@router.post('/delete')
async def delete_gg_injection(gg_injection_data: JsonForm,
                              user: User = Depends(get_current_user_from_cookie),
                              service: GammaGlobulinInjectionService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.delete_gg_injection(user=user, gg_injection=gg_injection)
