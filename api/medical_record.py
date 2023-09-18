from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Request,
)
from fastapi.templating import Jinja2Templates

from models.child import CreateChildForm
from models.json import JsonForm
from services.medical_record import MedicalRecordService
from services.parent import get_parent_by_id
from services.vac_name import get_vac_names_by_type


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
    hospitalizations = service.get_hospitalizations_by_medcard_num(medcard_num)
    spa_treatments = service.get_spa_treatments_by_medcard_num(medcard_num)
    medical_certificates = service.get_medical_certificates_by_medcard_num(medcard_num)
    dispensaryes = service.get_dispensaryes_by_medcard_num(medcard_num)
    dewormings = service.get_dewormings_by_medcard_num(medcard_num)
    oral_sanations = service.get_oral_sanations_by_medcard_num(medcard_num)
    prof_vac_names = get_vac_names_by_type(service.connection, 'Профилактическая')
    epid_vac_names = get_vac_names_by_type(service.connection, 'По показаниям')
    prevaccination_checkups = service.get_prevaccination_checkups_by_medcard_num(medcard_num)
    prof_vaccinations = service.get_prof_vaccinations_by_medcard_num(medcard_num)
    epid_vaccinations = service.get_epid_vaccinations_by_medcard_num(medcard_num)
    gg_injections = service.get_gg_injections_by_medcard_num(medcard_num)
    mantoux_tests = service.get_mantoux_tests_by_medcard_num(medcard_num)
    tub_vacs = service.get_tub_vacs_by_medcard_num(medcard_num)
    medical_examinations = service.get_medical_examinations_by_medcard_num(medcard_num)
    ongoing_medical_supervisions = service.get_ongoing_medical_supervisions_by_medcard_num(medcard_num)
    screenings = service.get_screenings_by_medcard_num(medcard_num)
    return templates.TemplateResponse(
        "/medical_record/child/index.html", {"request": request, 
                                             "child": child, 
                                             "allergyes": allergyes, 
                                             "father": father,
                                             "mother": mother,
                                             "extra_classes": extra_classes,
                                             "past_illnesses": past_illnesses,
                                             "hospitalizations": hospitalizations,
                                             "spa_treatments": spa_treatments,
                                             "medical_certificates": medical_certificates,
                                             "dispensaryes": dispensaryes,
                                             "dewormings": dewormings,
                                             "oral_sanations": oral_sanations,
                                             "prof_vac_names": prof_vac_names,
                                             "epid_vac_names": epid_vac_names,
                                             "prevaccination_checkups": prevaccination_checkups,
                                             "prof_vaccinations": prof_vaccinations,
                                             "epid_vaccinations": epid_vaccinations,
                                             "gg_injections": gg_injections,
                                             "mantoux_tests": mantoux_tests,
                                             "tub_vacs": tub_vacs,
                                             "medical_examinations": medical_examinations,
                                             "ongoing_medical_supervisions": ongoing_medical_supervisions,
                                             "screenings": screenings}
    )



@router.post('/child/get')
async def get_child(child_data: JsonForm,  service: MedicalRecordService = Depends()):
    medcard_num = child_data.json_data["medcard_num"]
    child = service.get_child_by_medcard_num(medcard_num)
    return child

@router.post('/child/update')
async def update_child(child_data: JsonForm,  service: MedicalRecordService = Depends()):
    child = child_data.json_data
    service.update_child(child)

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


@router.post('/child/{medcard_num}/hospitalization/get')
async def get_hospitalization(hospitalization_data: JsonForm,  service: MedicalRecordService = Depends()):
    hospitalization = hospitalization_data.json_data
    hospitalization = service.get_hospitalization_by_pk(hospitalization)
    return {"hospitalization": hospitalization}

@router.post('/child/{medcard_num}/hospitalization/add')
async def add_extra_class(hospitalization_data: JsonForm,  service: MedicalRecordService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.add_new_hospitalization(hospitalization)

@router.post('/child/{medcard_num}/hospitalization/update')
async def update_hospitalization(hospitalization_data: JsonForm,  service: MedicalRecordService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.update_hospitalization(hospitalization)

@router.post('/child/{medcard_num}/hospitalization/delete')
async def delete_hospitalization(hospitalization_data: JsonForm,  service: MedicalRecordService = Depends()):
    hospitalization = hospitalization_data.json_data
    service.delete_hospitalization(hospitalization)


@router.post('/child/{medcard_num}/spa_treatment/get')
async def get_spa_treatment(spa_treatment_data: JsonForm,  service: MedicalRecordService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    spa_treatment = service.get_spa_treatment_by_pk(spa_treatment)
    return {"spa_treatment": spa_treatment}

@router.post('/child/{medcard_num}/spa_treatment/add')
async def add_extra_class(spa_treatment_data: JsonForm,  service: MedicalRecordService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.add_new_spa_treatment(spa_treatment)

@router.post('/child/{medcard_num}/spa_treatment/update')
async def update_spa_treatment(spa_treatment_data: JsonForm,  service: MedicalRecordService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.update_spa_treatment(spa_treatment)

@router.post('/child/{medcard_num}/spa_treatment/delete')
async def delete_spa_treatment(spa_treatment_data: JsonForm,  service: MedicalRecordService = Depends()):
    spa_treatment = spa_treatment_data.json_data
    service.delete_spa_treatment(spa_treatment)


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


@router.post('/child/{medcard_num}/dispensary/get')
async def get_dispensary(dispensary_data: JsonForm,  service: MedicalRecordService = Depends()):
    dispensary = dispensary_data.json_data
    dispensary = service.get_dispensary_by_pk(dispensary)
    return {"dispensary": dispensary}

@router.post('/child/{medcard_num}/dispensary/add')
async def add_extra_class(dispensary_data: JsonForm,  service: MedicalRecordService = Depends()):
    dispensary = dispensary_data.json_data
    service.add_new_dispensary(dispensary)

@router.post('/child/{medcard_num}/dispensary/update')
async def update_dispensary(dispensary_data: JsonForm,  service: MedicalRecordService = Depends()):
    dispensary = dispensary_data.json_data
    service.update_dispensary(dispensary)

@router.post('/child/{medcard_num}/dispensary/delete')
async def delete_dispensary(dispensary_data: JsonForm,  service: MedicalRecordService = Depends()):
    dispensary = dispensary_data.json_data
    service.delete_dispensary(dispensary)


@router.post('/child/{medcard_num}/visit_specialist_control/get_all')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm,  service: MedicalRecordService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_controls = service.get_visit_specialist_controls_by_dispensary(visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_controls}

@router.post('/child/{medcard_num}/visit_specialist_control/get')
async def get_visit_specialist_control(visit_specialist_control_data: JsonForm,  service: MedicalRecordService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    visit_specialist_control = service.get_visit_specialist_control_by_pk(visit_specialist_control)
    return {"visit_specialist_control": visit_specialist_control}

@router.post('/child/{medcard_num}/visit_specialist_control/add')
async def add_extra_class(visit_specialist_control_data: JsonForm,  service: MedicalRecordService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.add_new_visit_specialist_control(visit_specialist_control)

@router.post('/child/{medcard_num}/visit_specialist_control/update')
async def update_visit_specialist_control(visit_specialist_control_data: JsonForm,  service: MedicalRecordService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.update_visit_specialist_control(visit_specialist_control)

@router.post('/child/{medcard_num}/visit_specialist_control/delete')
async def delete_visit_specialist_control(visit_specialist_control_data: JsonForm,  service: MedicalRecordService = Depends()):
    visit_specialist_control = visit_specialist_control_data.json_data
    service.delete_visit_specialist_control(visit_specialist_control)


@router.post('/child/{medcard_num}/deworming/get')
async def get_deworming(deworming_data: JsonForm,  service: MedicalRecordService = Depends()):
    deworming = deworming_data.json_data
    deworming = service.get_deworming_by_pk(deworming)
    return {"deworming": deworming}

@router.post('/child/{medcard_num}/deworming/add')
async def add_extra_class(deworming_data: JsonForm,  service: MedicalRecordService = Depends()):
    deworming = deworming_data.json_data
    service.add_new_deworming(deworming)

@router.post('/child/{medcard_num}/deworming/update')
async def update_deworming(deworming_data: JsonForm,  service: MedicalRecordService = Depends()):
    deworming = deworming_data.json_data
    service.update_deworming(deworming)

@router.post('/child/{medcard_num}/deworming/delete')
async def delete_deworming(deworming_data: JsonForm,  service: MedicalRecordService = Depends()):
    deworming = deworming_data.json_data
    service.delete_deworming(deworming)

@router.post('/child/{medcard_num}/oral_sanation/get')
async def get_oral_sanation(oral_sanation_data: JsonForm,  service: MedicalRecordService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    oral_sanation = service.get_oral_sanation_by_pk(oral_sanation)
    return {"oral_sanation": oral_sanation}

@router.post('/child/{medcard_num}/oral_sanation/add')
async def add_extra_class(oral_sanation_data: JsonForm,  service: MedicalRecordService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.add_new_oral_sanation(oral_sanation)

@router.post('/child/{medcard_num}/oral_sanation/update')
async def update_oral_sanation(oral_sanation_data: JsonForm,  service: MedicalRecordService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.update_oral_sanation(oral_sanation)

@router.post('/child/{medcard_num}/oral_sanation/delete')
async def delete_oral_sanation(oral_sanation_data: JsonForm,  service: MedicalRecordService = Depends()):
    oral_sanation = oral_sanation_data.json_data
    service.delete_oral_sanation(oral_sanation)


@router.post('/child/{medcard_num}/prevaccination_checkup/get')
async def get_prevaccination_checkup(prevaccination_checkup_data: JsonForm,  service: MedicalRecordService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    prevaccination_checkup = service.get_prevaccination_checkup_by_pk(prevaccination_checkup)
    return {"prevaccination_checkup": prevaccination_checkup}

@router.post('/child/{medcard_num}/prevaccination_checkup/add')
async def add_extra_class(prevaccination_checkup_data: JsonForm,  service: MedicalRecordService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    return service.add_new_prevaccination_checkup(prevaccination_checkup)

@router.post('/child/{medcard_num}/prevaccination_checkup/update')
async def update_prevaccination_checkup(prevaccination_checkup_data: JsonForm,  service: MedicalRecordService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    return service.update_prevaccination_checkup(prevaccination_checkup)

@router.post('/child/{medcard_num}/prevaccination_checkup/delete')
async def delete_prevaccination_checkup(prevaccination_checkup_data: JsonForm,  service: MedicalRecordService = Depends()):
    prevaccination_checkup = prevaccination_checkup_data.json_data
    service.delete_prevaccination_checkup(prevaccination_checkup)


@router.post('/child/{medcard_num}/prof_vaccination/get')
async def get_prof_vaccination(prof_vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    prof_vaccination = prof_vaccination_data.json_data
    prof_vaccination = service.get_prof_vaccination_by_pk(prof_vaccination)
    return prof_vaccination

@router.post('/child/{medcard_num}/epid_vaccination/get')
async def get_epid_vaccination(epid_vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    epid_vaccination = epid_vaccination_data.json_data
    epid_vaccination = service.get_epid_vaccination_by_pk(epid_vaccination)
    return epid_vaccination

@router.post('/child/{medcard_num}/vaccination/add')
async def add_extra_class(vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    vaccination = vaccination_data.json_data
    service.add_new_vaccination(vaccination)

@router.post('/child/{medcard_num}/vaccination/update')
async def update_vaccination(vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    vaccination = vaccination_data.json_data
    service.update_vaccination(vaccination)

@router.post('/child/{medcard_num}/vaccination/delete')
async def delete_prof_vaccination(vaccination_data: JsonForm,  service: MedicalRecordService = Depends()):
    vaccination = vaccination_data.json_data
    service.delete_vaccination(vaccination)


@router.post('/child/{medcard_num}/gg_injection/get')
async def get_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    gg_injection = service.get_gg_injection_by_pk(gg_injection)
    return  gg_injection

@router.post('/child/{medcard_num}/gg_injection/add')
async def add_extra_class(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.add_new_gg_injection(gg_injection)

@router.post('/child/{medcard_num}/gg_injection/update')
async def update_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.update_gg_injection(gg_injection)

@router.post('/child/{medcard_num}/gg_injection/delete')
async def delete_gg_injection(gg_injection_data: JsonForm,  service: MedicalRecordService = Depends()):
    gg_injection = gg_injection_data.json_data
    service.delete_gg_injection(gg_injection)


@router.post('/child/{medcard_num}/mantoux_test/get')
async def get_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    mantoux_test = service.get_mantoux_test_by_pk(mantoux_test)
    return  mantoux_test

@router.post('/child/{medcard_num}/mantoux_test/add')
async def add_extra_class(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.add_new_mantoux_test(mantoux_test)

@router.post('/child/{medcard_num}/mantoux_test/update')
async def update_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.update_mantoux_test(mantoux_test)

@router.post('/child/{medcard_num}/mantoux_test/delete')
async def delete_mantoux_test(mantoux_test_data: JsonForm,  service: MedicalRecordService = Depends()):
    mantoux_test = mantoux_test_data.json_data
    service.delete_mantoux_test(mantoux_test)


@router.post('/child/{medcard_num}/tub_vac/get')
async def get_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    tub_vac = service.get_tub_vac_by_pk(tub_vac)
    return  tub_vac

@router.post('/child/{medcard_num}/tub_vac/add')
async def add_extra_class(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.add_new_tub_vac(tub_vac)

@router.post('/child/{medcard_num}/tub_vac/update')
async def update_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.update_tub_vac(tub_vac)

@router.post('/child/{medcard_num}/tub_vac/delete')
async def delete_tub_vac(tub_vac_data: JsonForm,  service: MedicalRecordService = Depends()):
    tub_vac = tub_vac_data.json_data
    service.delete_tub_vac(tub_vac)

@router.post('/child/{medcard_num}/medical_examination/get')
async def get_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    medical_examination = service.get_medical_examination_by_pk(medical_examination)
    return  medical_examination

@router.post('/child/{medcard_num}/medical_examination/add')
async def add_extra_class(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    age = service.add_new_medical_examination(medical_examination)
    return {"age": age}

@router.post('/child/{medcard_num}/medical_examination/update')
async def update_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    age = service.update_medical_examination(medical_examination)
    return {"age": age}

@router.post('/child/{medcard_num}/medical_examination/delete')
async def delete_medical_examination(medical_examination_data: JsonForm,  service: MedicalRecordService = Depends()):
    medical_examination = medical_examination_data.json_data
    service.delete_medical_examination(medical_examination)


@router.post('/child/{medcard_num}/ongoing_medical_supervision/get')
async def get_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  service: MedicalRecordService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    ongoing_medical_supervision = service.get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision)
    return  ongoing_medical_supervision

@router.post('/child/{medcard_num}/ongoing_medical_supervision/add')
async def add_extra_class(ongoing_medical_supervision_data: JsonForm,  service: MedicalRecordService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.add_new_ongoing_medical_supervision(ongoing_medical_supervision)

@router.post('/child/{medcard_num}/ongoing_medical_supervision/update')
async def update_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  service: MedicalRecordService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.update_ongoing_medical_supervision(ongoing_medical_supervision)

@router.post('/child/{medcard_num}/ongoing_medical_supervision/delete')
async def delete_ongoing_medical_supervision(ongoing_medical_supervision_data: JsonForm,  service: MedicalRecordService = Depends()):
    ongoing_medical_supervision = ongoing_medical_supervision_data.json_data
    service.delete_ongoing_medical_supervision(ongoing_medical_supervision)


@router.post('/child/{medcard_num}/screening/get')
async def get_screening(screening_data: JsonForm,  service: MedicalRecordService = Depends()):
    screening = screening_data.json_data
    screening = service.get_screening_by_pk(screening)
    return  screening

@router.post('/child/{medcard_num}/screening/add')
async def add_extra_class(screening_data: JsonForm,  service: MedicalRecordService = Depends()):
    screening = screening_data.json_data
    service.add_new_screening(screening)

@router.post('/child/{medcard_num}/screening/update')
async def update_screening(screening_data: JsonForm,  service: MedicalRecordService = Depends()):
    screening = screening_data.json_data
    service.update_screening(screening)

@router.post('/child/{medcard_num}/screening/delete')
async def delete_screening(screening_data: JsonForm,  service: MedicalRecordService = Depends()):
    screening = screening_data.json_data
    service.delete_screening(screening)
