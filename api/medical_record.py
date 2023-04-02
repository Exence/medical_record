from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Form,
    Response,
    Request,
)
from fastapi.templating import Jinja2Templates

from models.child import CreateChildForm
from services.medical_record import MedicalRecordService


router = APIRouter(
    prefix='/medical_record',
    tags=['Medical record']
)
templates = Jinja2Templates(directory="templates")

@router.get('/create')
def show_create_medcard_form(request: Request):
    return templates.TemplateResponse(
        "/medical_record/create/index.html", {"request": request}
    )

@router.post('/create')
def create_user(request: Request, 
                form_data: CreateChildForm = Depends(CreateChildForm.as_form),
                service: MedicalRecordService = Depends(), 
                access_token: str | None = Cookie(default=None)):
    """
    Процедура добавления новой медкарты на ребенка
    """
    msg = ""
    error = ""
    if service.create_new_medcard(form_data, access_token):
        msg = "Новая медкарта успешно добавлена в систему"
    else:
        error = "Ошибка работы с БД при добавлении медкарты"
    return templates.TemplateResponse(
                    "/admins/users/create/index.html", {"request": request, "msg": msg, "error": error}
                )