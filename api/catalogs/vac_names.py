from fastapi import (
    APIRouter,
    Depends,
)
from models.catalogs.vac_name import (
    VacNamePK,
    VacName,
    VacNameCreate,
    VacNameUpdate,
    VacNameTypeDict
)
from models.user import User
from services.catalogs.vac_name import VacNameService
from services.auth import get_current_user
from services.user import check_user_access_to_medcard


router = APIRouter(
    prefix='/vac_names',
    tags=['Vac Name']
)


@router.get('/', response_model=VacNameTypeDict)
async def get_vac_names(service: VacNameService = Depends()):
    return service.get_all_vac_names_as_dict()


@router.get('/{id}', response_model=VacName)
async def get_vac_name_by_id(id: int,
                           medcard_num: int,
user: User = Depends(get_current_user),
                           service: VacNameService = Depends()):
    return service.get_vac_name_by_id(id=id)


@router.post('/', response_model=VacName)
async def add_vac_name(vac_name_data: VacNameCreate,
                     medcard_num: int,
user: User = Depends(get_current_user),
                     service: VacNameService = Depends()):
    return service.add_new_vac_name(vac_name_data=vac_name_data)


@router.put('/', response_model=VacName)
async def update_vac_name(vac_name_data: VacNameUpdate,
                        medcard_num: int,
user: User = Depends(get_current_user),
                        service: VacNameService = Depends()):
    return service.update_vac_name(vac_name_data=vac_name_data)


@router.delete('/')
async def delete_vac_name(vac_name_pk: VacNamePK,
                        medcard_num: int,
user: User = Depends(get_current_user),
                        service: VacNameService = Depends()):
    service.delete_vac_name(vac_name_pk=vac_name_pk)
