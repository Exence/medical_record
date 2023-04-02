from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    Response,
    Request,
)
from fastapi.templating import Jinja2Templates
from typing import Annotated

from models.user import (
    User,
    UserCreate,
    CreateUserForm,
)

from services.user import UserService


router = APIRouter(
    prefix='/users',
    tags=['User']
)
templates = Jinja2Templates(directory="templates")

@router.get('/create')
def show_create_user_form(request: Request):
    return templates.TemplateResponse(
        "/admins/users/create/index.html", {"request": request}
    )

@router.post('/create')
def create_user(request: Request, 
                form_data: CreateUserForm = Depends(CreateUserForm.as_form),
                service: UserService = Depends(), 
                access_token: str | None = Cookie(default=None)):
    """
    Процедура добавления нового Пользователя
    """
    msg = ""
    error = ""
    if service.create_new_user(form_data, access_token):
        msg = "Пользователь успешно добавлен в систему"
    else:
        error = "Ошибка работы с БД при добавлении пользователя"
    return templates.TemplateResponse(
                    "/admins/users/create/index.html", {"request": request, "msg": msg, "error": error}
                )

@router.get('/all')
def show_all_users(request: Request, service: UserService = Depends()):
    users = service.get_all_users()
    return templates.TemplateResponse(
        "/admins/users/all/index.html", {"request": request, "users": users}
    )
