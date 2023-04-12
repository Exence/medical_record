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
    extra_classes = service.get_extra_classes_by_medcard_num(medcard_num)
    past_illnesses = service.get_past_illnesses_by_medcard_num(medcard_num)
    medical_certificates = service.get_medical_certificates_by_medcard_num(medcard_num)
    return templates.TemplateResponse(
        "/medical_record/child/index.html", {"request": request, 
                                             "child": child, 
                                             "allergyes": allergyes, 
                                             "father": father,
                                             "mother": mother,
                                             "extra_classes": extra_classes,
                                             "past_illnesses": past_illnesses,
                                             "medical_certificates": medical_certificates}
    )



@router.post('/child/{medcard_num}/allergy/add')
async def add_allergy(allergy_data: JsonForm, medcard_num: int, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.add_new_allergy(medcard_num, allergy)

@router.post('/child/{medcard_num}/allergy/update')
async def update_allergy(allergy_data: JsonForm, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.update_allergy(allergy)

@router.post('/child/{medcard_num}/allergy/delete')
async def delete_allergy(allergy_data: JsonForm, service: MedicalRecordService = Depends()):
    allergy = allergy_data.json_data
    service.delete_allergy(allergy)


@router.post('/child/{medcard_num}/parent/add')
async def update_parent(parent_data: JsonForm,  service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    parent_id = service.add_parent(parent)
    return {"id": parent_id}

@router.post('/child/{medcard_num}/parent/update')
async def update_parent(parent_data: JsonForm, service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    service.update_parent(parent)

@router.post('/child/{medcard_num}/parent/delete')
async def delete_parent(parent_data: JsonForm, service: MedicalRecordService = Depends()):
    parent = parent_data.json_data
    service.delete_parent(parent)


@router.post('/child/{medcard_num}/extra_class/add')
async def add_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.add_new_extra_class(extra_class)

@router.post('/child/{medcard_num}/extra_class/update')
async def update_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.update_extra_class(extra_class)

@router.post('/child/{medcard_num}/extra_class/delete')
async def delete_extra_class(extra_class_data: JsonForm,  service: MedicalRecordService = Depends()):
    extra_class = extra_class_data.json_data
    service.delete_extra_class(extra_class)


@router.post('/child/{medcard_num}/past_illness/get')
async def get_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    past_illness = service.get_past_illness_by_pk(past_illness)
    return {"past_illness": past_illness}

@router.post('/child/{medcard_num}/past_illness/add')
async def add_extra_class(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.add_new_past_illness(past_illness)

@router.post('/child/{medcard_num}/past_illness/update')
async def update_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.update_past_illness(past_illness)

@router.post('/child/{medcard_num}/past_illness/delete')
async def delete_past_illness(past_illness_data: JsonForm,  service: MedicalRecordService = Depends()):
    past_illness = past_illness_data.json_data
    service.delete_past_illness(past_illness)



@router.post('/child/{medcard_num}/medical_certificate/get')
async def get_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    medical_certificate = service.get_medical_certificate_by_pk(medical_certificate)
    return {"medical_certificate": medical_certificate}

@router.post('/child/{medcard_num}/medical_certificate/add')
async def add_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.add_new_medical_certificate(medical_certificate)

@router.post('/child/{medcard_num}/medical_certificate/update')
async def update_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.update_medical_certificate(medical_certificate)

@router.post('/child/{medcard_num}/medical_certificate/delete')
async def delete_medical_certificate(medical_certificate_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_certificate = medical_certificate_data.json_data
    service.delete_medical_certificate(medical_certificate)
