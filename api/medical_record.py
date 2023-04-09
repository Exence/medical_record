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
from models.json import JsonForm
from services.medical_record import MedicalRecordService
from services.parent import get_parent_by_id


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

@router.get('/child/{medcard_num}')
def get_child_medcard(medcard_num: int, request: Request, service: MedicalRecordService = Depends()):
    child = service.get_child_by_medcard_num(medcard_num)
    allergyes = service.get_allergyes_by_medcard_num(medcard_num)
    father = get_parent_by_id(service.connection, child.father_id)
    mother = get_parent_by_id(service.connection, child.mother_id)
    return templates.TemplateResponse(
        "/medical_record/child/index.html", {"request": request, 
                                             "child": child, 
                                             "allergyes": allergyes, 
                                             "father": father,
                                             "mother": mother}
    )

@router.post('/child/{medcard_num}/allergy/add')
async def create_allergy(allergy_data: JsonForm, medcard_num: int, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.add_new_allergy(medcard_num, allergy)

@router.post('/child/{medcard_num}/allergy/update')
async def create_allergy(allergy_data: JsonForm, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.update_allergy(allergy)

@router.post('/child/{medcard_num}/allergy/delete')
async def create_allergy(allergy_data: JsonForm, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.delete_allergy(allergy)
