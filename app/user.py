from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    Response,
    Request,
)
from fastapi.templating import Jinja2Templates

from services.user import (
    AuthService,
    UserService,
)


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


@router.get('/all')
def show_all_users(request: Request, service: UserService = Depends()):
    users = service.get_all_users()
    return templates.TemplateResponse(
        "/admins/users/all/index.html", {"request": request, "users": users}
    )


@router.get('/cabinet')
def show_all_users(request: Request,
                   service: AuthService = Depends(),
                   access_token: str | None = Cookie(default=None)):
    current_user = service.validate_token(access_token)
    return templates.TemplateResponse(
        "/cabinet/index.html", {"request": request, "user": current_user}
    )
