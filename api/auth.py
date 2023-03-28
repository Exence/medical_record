from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import (
    User,
    Token,
)
from services.auth import (
    AuthService,
    get_current_user,
)


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

'''
@router.post('/sign-up', response_model=Token)
def sign_up(form_data: UserCreate, service: AuthService = Depends()):
    """
    Процедура регистрации нового Пользователя
    """
    return service.register_new_user(form_data)
'''

@router.post('/', response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    """
    Процедура авторизации Пользователя
    """
    return service.authenticate_user(
        login=form_data.username,
        password=form_data.password
    )

@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """
    Получение текущего Пользователя
    """
    return user