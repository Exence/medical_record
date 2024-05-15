from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    HTTPException,
    Response,
    Request,
)
from urllib.parse import unquote
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from models.auth import Token
from models.json import JsonForm
from models.catalogs.vac_name import VacName
from models.user import User
from services.auth import (
    AuthService,
    get_current_user,
)
from services.catalogs.vac_name import VacNameService


router = APIRouter(
    prefix='/vac_names',
    tags=['Vaccine Name']
)
templates = Jinja2Templates(directory="templates")


@router.get('/')
async def show_all_vac_names(request: Request,
                           service: VacNameService = Depends(),
                           msg: str = Cookie(None),
                           err: str = Cookie(None)):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
        
    if msg:
        msg = unquote(msg)
    if err:
        err = unquote(err)
    vac_names = service.get_all_vac_names_as_dict()
    return templates.TemplateResponse('catalogs/vac_names/index.html', {'request': request,
                                                                        'vac_names': vac_names,
                                                                        'msg': msg,
                                                                        'err': err})