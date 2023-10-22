from fastapi import (
    APIRouter,
    Cookie,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import Token

from services.auth import (
    AuthService,
)


router = APIRouter(
    prefix='/sign-in',
    tags=['Sign in']
)

@router.post('/', response_model=Token)
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
                  service: AuthService = Depends()) -> Token:
    return service.authenticate_user(
                login=form_data.username,
                password=form_data.password
            )
