from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Response,
    Request,
)
from urllib.parse import unquote
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from models.auth import Token
from models.json import JsonForm
from models.vac_name import VacName
from models.user import User
from services.auth import (
    AuthService,
    get_current_user,
)
from services.vac_name import VacNameService


router = APIRouter(
    prefix='/vac_names',
    tags=['Vaccine Name']
)
templates = Jinja2Templates(directory="templates")


@router.get('/')
async def show_all_clinics(request: Request,
                           service: VacNameService = Depends(),
                           msg: str = Cookie(None),
                           err: str = Cookie(None)):
    if msg:
        msg = unquote(msg)
    if err:
        err = unquote(err)
    vac_names = service.get_all_vac_names_as_dict()
    return templates.TemplateResponse('catalogs/vac_names/index.html', {'request': request,
                                                                        'vac_names': vac_names,
                                                                        'msg': msg,
                                                                        'err': err})