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
    """
    Получение списка сведений о наименованиях прививок
    """
    return service.get_all_vac_names_as_dict()


@router.get('/{id}', response_model=VacName)
async def get_vac_name_by_id(id: int,
                             user: User = Depends(get_current_user),
                             service: VacNameService = Depends()):
    """
    Получение сведений о наименованиии прививки по id
    """
    return service.get_vac_name_by_id(id=id)


@router.post('/', response_model=VacName)
async def add_vac_name(vac_name_data: VacNameCreate,
                       user: User = Depends(get_current_user),
                       service: VacNameService = Depends()):
    """
    Добавление сведений о наименованиии прививки
    """
    return service.add_new_vac_name(vac_name_data=vac_name_data)


@router.put('/', response_model=VacName)
async def update_vac_name(vac_name_data: VacNameUpdate,
                          user: User = Depends(get_current_user),
                          service: VacNameService = Depends()):
    """
    Редактирование сведений о наименованиии прививки
    """
    return service.update_vac_name(vac_name_data=vac_name_data)


@router.delete('/')
async def delete_vac_name(vac_name_pk: VacNamePK,
                          user: User = Depends(get_current_user),
                          service: VacNameService = Depends()):
    """
    Удаление сведений о наименованиии прививки
    """
    service.delete_vac_name(vac_name_pk=vac_name_pk)
