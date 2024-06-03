from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    HTTPException,
    Request,
)
from fastapi.responses import RedirectResponse
from settings import templates

from models.medical_record.child import ChildEdit, CreateChildForm
from models.user import User

from services.auth import get_current_user
from services.catalogs.clinic import ClinicService
from services.kindergarten import KindergartenService
from services.medical_record.medical_record import MedicalRecordService
from services.medical_record.parent import ParentService

from .child.child import router as child_router


router = APIRouter(
    prefix='/medical_record',
    tags=['Medical record']
)
router.include_router(child_router)




@router.get('/create')
def show_create_medcard_form(request: Request,
                             clinic_service: ClinicService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        user = get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    clinics = clinic_service.get_all_clinics_as_dict()
    if user:
        return templates.TemplateResponse(
            "/medical_record/create/index.html", {"request": request, 
                                                "kindergarten_name": user.kindergarten_name,
                                                "kindergarten_num": user.kindergarten_num,
                                                "clinics": clinics
                                                }
        )
    else:
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request}
        )


@router.post('/create')
async def create_user(request: Request,
                service: MedicalRecordService = Depends(),
                parent_service: ParentService = Depends(),
                clinic_service: ClinicService = Depends()):
    """
    Процедура добавления новой медкарты на ребенка
    """
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        user = get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    if user:
        form_data = await request.form()
        child_form = CreateChildForm(**form_data, kindergarten_num=user.kindergarten_num)
        msg = ""
        error = ""
        if service.add_new_medcard_from_form(child_form=child_form, parent_service=parent_service):
            msg = "Новая медкарта успешно добавлена в систему"
        else:
            error = "Ошибка работы с БД при добавлении медкарты. Медкарта НЕ добавлена!"
        clinics = clinic_service.get_all_clinics_as_dict()
        return templates.TemplateResponse(
            "/medical_record/create/index.html", {
                "request": request, "msg": msg, "error": error, "kindergarten_name": user.kindergarten_name, "clinics": clinics}
        )
    else:
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request}
        )


@router.get('/all')
def show_all_medcards(request: Request,
                      service: KindergartenService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        user = get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    if user:
        kindergarten = service.get_kindergarten_with_children(
            user)
        return templates.TemplateResponse(
            "/medical_record/all/index.html", {"request": request,
                                            "kindergarten": kindergarten}
        )
    else:
        return templates.TemplateResponse(
            "login_page/index.html", {"request": request}
        )
