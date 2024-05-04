from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    Response,
    Request,
)
from urllib.parse import unquote
from fastapi.templating import Jinja2Templates

from models.clinic import Clinic, ClinicCreate, ClinicUpdate

from services.auth import (
    AuthService, 
    get_current_user
)
from services.clinic import ClinicService


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
    if msg:
        msg = unquote(msg)
    if err:
        err = unquote(err)
    clinics = service.get_all_clinics_as_dict()
    return templates.TemplateResponse('clinics/index.html', {'request': request, 'clinics': clinics, 'msg': msg, 'err': err})
