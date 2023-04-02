from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from models.auth import Token
from models.user import User
from services.auth import (
    AuthService,
    get_current_user,
)


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)
templates = Jinja2Templates(directory="templates")

@router.post('/')
async def sign_in(
    response: Response,
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    """
    Процедура авторизации Пользователя
    """
    try:
        jwt_token = service.authenticate_user(
            login=form_data.username,
            password=form_data.password
        )
        msg = "Login Succesful"
        response = templates.TemplateResponse(
                    "login_page/index.html", {"request": request, "msg": msg}
                )
        response.set_cookie(
            key="access_token", value=f"{jwt_token.access_token}", httponly=True
        )
        return response
    except:
        msg = "Something Wrong while authentication or storing tokens!"
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request, "error": msg}
        )

@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """
    Получение текущего Пользователя
    """
    return user