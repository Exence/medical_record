from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from settings import templates

from services.auth import (
    AuthService,
)


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)



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
            password=form_data.password
        )
        current_user = service.validate_token(jwt_token.access_token)
        msg = "Успешный вход"
        response = templates.TemplateResponse(
            "cabinet/index.html", {"request": request,
                                   "msg": msg, "user": current_user}
        )
        response.set_cookie(
            key="access_token", value=f"{jwt_token.token_type} {jwt_token.access_token}", httponly=True
        )
        return response
    except:
        error = "Ошибка авторизации! Проверьте правильность пароля!"
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request, "error": error}
        )


@router.get('/leave')
def delete_cookies(response: Response, request: Request,):
    msg = "Выход успешно выполнен"
    response = templates.TemplateResponse(
        "login_page/index.html", {"request": request, "msg": msg}
    )
    response.delete_cookie(key="access_token")
    return response
