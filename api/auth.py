from fastapi import (
    APIRouter,
    Cookie,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import Token
from models.user import User

from services.auth import (
    AuthService,
    get_current_user
)


router = APIRouter(
    tags=['Auth']
)


@router.post('/sign-in', response_model=Token)
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
                  service: AuthService = Depends()) -> Token:
    return service.authenticate_user(
        password=form_data.password
    )

@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """
    Получение текущего Пользователя
    """
    return user
