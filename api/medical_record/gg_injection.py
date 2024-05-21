from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from models.medical_record.gg_injection import (
    GammaGlobulinInjectionPK,
    GammaGlobulinInjection,
    GammaGlobulinInjectionCreate,
    GammaGlobulinInjectionUpdate,
)
from models.user import User
from services.medical_record.gg_injection import GammaGlobulinInjectionService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/gg_injections',
    tags=['Gamma globulin injection']
)


@router.get('/', response_model=list[GammaGlobulinInjection])
async def get_gamma_globulin_injections_by_medcard_num(medcard_num: int,
                                           user: User = Depends(get_current_user),
                                           service: GammaGlobulinInjectionService = Depends()):
    """
    Получение списка сведений о введении гамма-глобулина по номеру медкарты
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_gamma_globulin_injections_by_medcard_num(medcard_num=medcard_num)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/one', response_model=GammaGlobulinInjection)
async def get_gamma_globulin_injection_by_pk(gg_injection_pk: GammaGlobulinInjectionPK,
                                             medcard_num: int,
                                             user: User = Depends(get_current_user),
                                             service: GammaGlobulinInjectionService = Depends()):
    """
    Получение сведений о введении гамма-глобулина по первичному ключу
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.get_gamma_globulin_injection_by_pk(gg_injection_pk=gg_injection_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.post('/', response_model=GammaGlobulinInjection)
async def add_gamma_globulin_injection(gg_injection_data: GammaGlobulinInjectionCreate,
                                       medcard_num: int,
                                       user: User = Depends(get_current_user),
                                       service: GammaGlobulinInjectionService = Depends()):
    """
    Добавление сведений о введении гамма-глобулина
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.add_new_gamma_globulin_injection(gg_injection_data=gg_injection_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.put('/', response_model=GammaGlobulinInjection)
async def update_gamma_globulin_injection(gg_injection_data: GammaGlobulinInjectionUpdate,
                                          medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: GammaGlobulinInjectionService = Depends()):
    """
    Редактирование сведений о введении гамма-глобулина
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.update_gamma_globulin_injection(gg_injection_data=gg_injection_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )


@router.delete('/')
async def delete_gamma_globulin_injection(gg_injection_pk: GammaGlobulinInjectionPK,
                                          medcard_num: int,
                                          user: User = Depends(get_current_user),
                                          service: GammaGlobulinInjectionService = Depends()):
    """
    Удаление сведений о введении гамма-глобулина
    """
    if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
        return service.delete_gamma_globulin_injection(gg_injection_pk=gg_injection_pk)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
