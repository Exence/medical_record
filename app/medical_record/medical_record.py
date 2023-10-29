from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Request,
)
from fastapi.templating import Jinja2Templates

from models.child import CreateChildForm
from models.child import ChildEdit
from services.medical_record.medical_record import MedicalRecordService, json_to_child_edit

from .child.child import router as child_router


router = APIRouter(
    prefix='/medical_record',
    tags=['Medical record']
)
router.include_router(child_router)

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
        error = "Ошибка работы с БД при добавлении медкарты. Медкарта НЕ добавлена!"
    return templates.TemplateResponse(
                    "/medical_record/create/index.html", {"request": request, "msg": msg, "error": error}
                )

@router.get('/all')
def show_all_medcards(request: Request, service: MedicalRecordService = Depends()):
    kindergartens = service.get_all_childrens()
    return templates.TemplateResponse(
        "/medical_record/all/index.html", {"request": request, "kindergartens": kindergartens}
    )

@router.get('/child/get/{medcard_num}')
async def get_child(medcard_num: int, service: MedicalRecordService = Depends()):
    child = service.get_child_by_medcard_num(medcard_num)
    return child

@router.post('/child/update')
async def update_child(child_data: ChildEdit = Depends(json_to_child_edit),  service: MedicalRecordService = Depends()):
    service.update_child(child_data)
