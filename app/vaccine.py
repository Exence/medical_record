from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
)
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
    prefix='/vaccine',
    tags=['Vaccine']
)
templates = Jinja2Templates(directory="templates")


@router.post('/get_all')
async def get_all_vaccine(service: VacNameService = Depends()):
    vac_names = service.get_all_vac_names()
    return vac_names
