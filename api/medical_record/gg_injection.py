from fastapi import (
    APIRouter,
    Depends,
)
from models.gg_injection import (
    GammaGlobulinInjectionPK,
    GammaGlobulinInjection,
    GammaGlobulinInjectionCreate,
    GammaGlobulinInjectionUpdate,
)
from models.user import User
from services.medical_record.gg_injection import GammaGlobulinInjectionService
from services.auth import get_current_user


router = APIRouter(
    prefix='/gg_injections',
    tags=['Gamma globulin injection']
)


@router.get('/', response_model=list[GammaGlobulinInjection])
async def get_gg_injections_by_medcard_num(medcard_num: int,
                                           user: User = Depends(
                                               get_current_user),
                                           service: GammaGlobulinInjectionService = Depends()):
    return service.get_gg_injections_by_medcard_num(user=user, medcard_num=medcard_num)


@router.post('/one', response_model=GammaGlobulinInjection)
async def get_gg_injection_by_pk(gg_injection_pk: GammaGlobulinInjectionPK,
                                 user: User = Depends(get_current_user),
                                 service: GammaGlobulinInjectionService = Depends()):
    return service.get_gg_injection_by_pk(user=user, gg_injection_pk=gg_injection_pk)


@router.post('/', response_model=GammaGlobulinInjection)
async def add_gg_injection(gg_injection_data: GammaGlobulinInjectionCreate,
                           user: User = Depends(get_current_user),
                           service: GammaGlobulinInjectionService = Depends()):
    return service.add_new_gg_injection(user=user, gg_injection_data=gg_injection_data)


@router.put('/', response_model=GammaGlobulinInjection)
async def update_gg_injection(gg_injection_data: GammaGlobulinInjectionUpdate,
                              user: User = Depends(get_current_user),
                              service: GammaGlobulinInjectionService = Depends()):
    return service.update_gg_injection(user=user, gg_injection_data=gg_injection_data)


@router.delete('/')
async def delete_gg_injection(gg_injection_pk: GammaGlobulinInjectionPK,
                              user: User = Depends(get_current_user),
                              service: GammaGlobulinInjectionService = Depends()):
    service.delete_gg_injection(user=user, gg_injection_pk=gg_injection_pk)
