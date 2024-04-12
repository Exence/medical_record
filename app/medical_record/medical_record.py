from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Request,
)
from fastapi.templating import Jinja2Templates

from models.child import ChildEdit, ChildCreate
from models.user import User

from services.auth import get_current_user
from services.kindergarten import KindergartenService
from services.medical_record.medical_record import MedicalRecordService

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
                child_data: ChildCreate,
                service: MedicalRecordService = Depends(),
                user: User = Depends(get_current_user)):
    """
    Процедура добавления новой медкарты на ребенка
    """
    msg = ""
    error = ""
    if service.add_new_medcard(user=user, child_data=child_data):
        msg = "Новая медкарта успешно добавлена в систему"
    else:
        error = "Ошибка работы с БД при добавлении медкарты. Медкарта НЕ добавлена!"
    return templates.TemplateResponse(
        "/medical_record/create/index.html", {
            "request": request, "msg": msg, "error": error}
    )


@router.get('/all')
def show_all_medcards(request: Request,
                      service: KindergartenService = Depends(),
                      user: User = Depends(get_current_user)):
    kindergarten = service.get_kindergarten_with_childrens(
        user)
    print(kindergarten)
    return templates.TemplateResponse(
        "/medical_record/all/index.html", {"request": request,
                                           "kindergarten": kindergarten}
    )


@router.get('/child/get/{medcard_num}')
async def get_child(medcard_num: int,
                    service: MedicalRecordService = Depends(),
                    user: User = Depends(get_current_user)):
    child = service.get_medcard_by_num(user=user, medcard_num=medcard_num)
    return child


@router.post('/child/update')
async def update_child(medcard_data: ChildEdit,
                       service: MedicalRecordService = Depends(),
                       user: User = Depends(get_current_user)):
    service.update_medcard(user=user, medcard_data=medcard_data)
