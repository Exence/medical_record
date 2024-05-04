from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    Response,
    Request,
)
from fastapi.templating import Jinja2Templates

from models.user import User, UserUpdate

from services.auth import (
    AuthService, 
    get_current_user
)
from services.user import UserService


router = APIRouter(
    prefix='/users',
    tags=['User']
)
templates = Jinja2Templates(directory="templates")


def update_user_data(request: Request, auth_service: AuthService, updated_user: User, msg: str):
    try:
        jwt_token = auth_service.create_token(
            user_data=updated_user
        )
        current_user = auth_service.validate_token(jwt_token.access_token)
        response = templates.TemplateResponse(
            "cabinet/index.html", {"request": request,
                                   "msg": msg, "user": current_user}
        )
        response.set_cookie(
            key="access_token", value=f"{jwt_token.token_type} {jwt_token.access_token}", httponly=True
        )
        return response
    except:
        error = "Что-то пошло не так! Пожалуйста, пройдите повторную авторизацию!"
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request, "error": error}
        )

@router.get('/create')
def show_create_user_form(request: Request):
    return templates.TemplateResponse(
        "/admins/users/create/index.html", {"request": request}
    )


@router.get('/all')
def show_all_users(request: Request, service: UserService = Depends()):
    users = service.get_all_users()
    return templates.TemplateResponse(
        "/admins/users/all/index.html", {"request": request, "users": users}
    )


@router.get('/cabinet')
def show_cabinet(request: Request,
                   user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "cabinet/index.html", {"request": request, "user": user}
    )

@router.get('/update_profile')
def show_update_user_form(request: Request,
                   user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "cabinet/update_profile.html", {"request": request, "user": user}
    ) 
@router.post('/update_profile')
async def update_user(request: Request,
                user_service: UserService = Depends(),
                auth_service: AuthService = Depends(),
                user: User = Depends(get_current_user)):
    form_data = await request.form()
    updated_data = UserUpdate(**form_data)
    updated_user = user_service.update_user(current_data=user, updated_data=updated_data)
    return update_user_data(request=request,auth_service=auth_service,updated_user=updated_user,msg="Данные успешно обновлены")
    

@router.get('/change_password')
def show_change_password_form(request: Request,
                   user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "cabinet/change_password.html", {"request": request}
    )

@router.post('/change_password')
def change_password(request: Request,
                    current_password: str = Form(),
                    new_password:str = Form(),
                    auth_service: AuthService = Depends(),
                    user_service: UserService = Depends(),
                    user: User = Depends(get_current_user)):
    if auth_service.verify_password(current_password, user.password_hash):
        updated_user = user_service.change_password(user=user, new_password=new_password)
        return update_user_data(request=request,auth_service=auth_service,updated_user=updated_user,msg="Пароль успешно обновлен")
    else:
       error = "Текущий пароль указан неверно"
       return templates.TemplateResponse(
        "cabinet/change_password.html", {"request": request, "error": error}
    ) 
