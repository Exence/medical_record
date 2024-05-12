from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    HTTPException,
    Response,
    Request,
)
from urllib.parse import unquote
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from services.auth import (
    AuthService, 
    get_current_user
)
from services.catalogs.clinic import ClinicService


router = APIRouter(
    prefix='/clinics',
    tags=['Clinic']
)
templates = Jinja2Templates(directory="templates")

@router.get('/')
async def show_all_clinics(request: Request,
                           service: ClinicService = Depends(),
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
    clinics = service.get_all_clinics_as_dict()
    return templates.TemplateResponse('catalogs/clinics/index.html', {'request': request, 'clinics': clinics, 'msg': msg, 'err': err})
