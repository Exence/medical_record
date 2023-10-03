from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from services.auth import (
    AuthService,
)


router = APIRouter(
    prefix='/sign-in',
    tags=['Sign in']
)
templates = Jinja2Templates(directory="templates")

@router.post('/')
async def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )