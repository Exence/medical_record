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

from api import router as api_router

router = APIRouter(
    prefix='/child/{medcard_num}',
    tags=['Child']
)
router.include_router(api_router)

templates = Jinja2Templates(directory="templates")

@router.get('/')
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
