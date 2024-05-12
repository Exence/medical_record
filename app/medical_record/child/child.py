from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    HTTPException,
    Request,
)
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from models.child import CreateChildForm
from models.json import JsonForm
from models.user import User

from services.auth import get_current_user
from services.medical_record.medical_record import MedicalRecordService
from services.medical_record.allergy import AllergyService
from services.catalogs.clinic import ClinicService
from services.medical_record.extra_class import ExtraClassService
from services.medical_record.past_illness import PastIllnessService
from services.medical_record.parent import ParentService
from services.medical_record.hospitalization import HospitalizationService
from services.medical_record.spa_treatment import SpaTreatmentService
from services.medical_record.medical_certificate import MedicalCertificateService
from services.medical_record.dispensary import DispensaryService
from services.medical_record.deworming import DewormingService
from services.medical_record.oral_sanation import OralSanationService
from services.medical_record.prevaccination_checkup import PrevaccinationCheckupService
from services.medical_record.vaccination import VaccinationService
from services.medical_record.gg_injection import GammaGlobulinInjectionService
from services.medical_record.mantoux_test import MantouxTestService
from services.medical_record.tub_vac import TuberculosisVaccinationService
from services.medical_record.medical_examination import MedicalExaminationService
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from services.medical_record.screening import ScreeningService
from services.catalogs.vac_name import VacNameService


router = APIRouter(
    prefix='/children/{medcard_num}',
    tags=['Child']
)

templates = Jinja2Templates(directory="templates")


@router.get('/')
def get_child_medcard(medcard_num: int, request: Request,   
                      service: MedicalRecordService = Depends(),
                      parents_service: ParentService = Depends(),
                      allergy_service: AllergyService = Depends(),
                      clinic_service: ClinicService = Depends(),
                      extra_class_service: ExtraClassService = Depends(),
                      past_illness_service: PastIllnessService = Depends(),
                      hospitalization_service: HospitalizationService = Depends(),
                      spa_treatment_service: SpaTreatmentService = Depends(),
                      medical_certificate_service: MedicalCertificateService = Depends(),
                      dispensary_service: DispensaryService = Depends(),
                      deworming_service: DewormingService = Depends(),
                      oral_sanation_service: OralSanationService = Depends(),
                      vac_name_service: VacNameService = Depends(),
                      prevaccination_checkup_service: PrevaccinationCheckupService = Depends(),
                      vaccination_service: VaccinationService = Depends(),
                      gg_injection_service: GammaGlobulinInjectionService = Depends(),
                      mantoux_test_service: MantouxTestService = Depends(),
                      tub_vac_service: TuberculosisVaccinationService = Depends(),
                      medical_examination_service: MedicalExaminationService = Depends(),
                      ongoing_medical_supervision_service: OngoingMedicalSupervisionService = Depends(),
                      screening_service: ScreeningService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        user = get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')

    child = service.get_medcard_by_num(medcard_num=medcard_num)
    father, mother = service.get_parents_by_medcard_num(medcard_num=medcard_num,parent_service=parents_service)
    kindergartens = [{"number": user.kindergarten_num, "name": user.kindergarten_name}]
    allergyes = allergy_service.get_allergyes_by_medcard_num(
        medcard_num=medcard_num)
    clinics = clinic_service.get_all_clinics_as_dict()
    extra_classes = extra_class_service.get_extra_classes_by_medcard_num(
        medcard_num=medcard_num)
    past_illnesses = past_illness_service.get_past_illnesses_by_medcard_num(
        medcard_num=medcard_num)
    hospitalizations = hospitalization_service.get_hospitalizations_by_medcard_num(
        medcard_num=medcard_num)
    spa_treatments = spa_treatment_service.get_spa_treatments_by_medcard_num(
        medcard_num=medcard_num)
    medical_certificates = medical_certificate_service.get_medical_certificates_by_medcard_num(
        medcard_num=medcard_num)
    dispensaryes = dispensary_service.get_dispensaryes_by_medcard_num(
        medcard_num=medcard_num)
    dewormings = deworming_service.get_dewormings_by_medcard_num(
        medcard_num=medcard_num)
    oral_sanations = oral_sanation_service.get_oral_sanations_by_medcard_num(
        medcard_num=medcard_num)
    vac_names = vac_name_service.get_all_vac_names_as_dict()
    prof_vac_names = vac_name_service.get_vac_names_by_type('Профилактическая')
    epid_vac_names = vac_name_service.get_vac_names_by_type('По показаниям')
    prevaccination_checkups = prevaccination_checkup_service.get_prevaccination_checkups_by_medcard_num(
        medcard_num=medcard_num)
    prof_vaccinations = vaccination_service.get_prof_vaccinations_by_medcard_num(
        medcard_num=medcard_num)
    epid_vaccinations = vaccination_service.get_epid_vaccinations_by_medcard_num(
        medcard_num=medcard_num)
    gg_injections = gg_injection_service.get_gg_injections_by_medcard_num(
        medcard_num=medcard_num)
    mantoux_tests = mantoux_test_service.get_mantoux_tests_by_medcard_num(
        medcard_num=medcard_num)
    tub_vacs = tub_vac_service.get_tub_vacs_by_medcard_num(
        medcard_num=medcard_num)
    medical_examinations = medical_examination_service.get_medical_examinations_by_medcard_num(
        medcard_num=medcard_num)
    ongoing_medical_supervisions = ongoing_medical_supervision_service.get_ongoing_medical_supervisions_by_medcard_num(
        medcard_num=medcard_num)
    screenings = screening_service.get_screenings_by_medcard_num(
        medcard_num=medcard_num)
    return templates.TemplateResponse(
        "/medical_record/children/index.html", {"request": request,
                                            "child": child,
                                            "kindergartens": kindergartens,
                                            "allergyes": allergyes,
                                            "clinics": clinics,
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
                                            "vac_names": vac_names,
                                            "prof_vaccinations": prof_vaccinations,
                                            "epid_vaccinations": epid_vaccinations,
                                            "gg_injections": gg_injections,
                                            "mantoux_tests": mantoux_tests,
                                            "tub_vacs": tub_vacs,
                                            "medical_examinations": medical_examinations,
                                            "ongoing_medical_supervisions": ongoing_medical_supervisions,
                                            "screenings": screenings}
    )
