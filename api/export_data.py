from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
)
from fastapi.responses import FileResponse
from models.user import User
from models.base_table_name import BaseTableNameModel
from models.medical_record.visit_specialist_control import VisitSpecialistControlMain
from services.export_data import create_file_with_child_tab, append_data_in_xlsx_file

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
from services.medical_record.mantoux import MantouxTestService
from services.medical_record.tub_vac import TuberculosisVaccinationService
from services.medical_record.medical_examination import MedicalExaminationService
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from services.medical_record.screening import ScreeningService
from services.catalogs.vac_name import VacNameService
from services.medical_record.visit_specialist_control import VisitSpecialistControlService


router = APIRouter(
    prefix='/children/{medcard_num}/xlsx',
    tags=['Export to xlsx']
)


@router.get('/')
async def get_xlsx_data_by_medcard_num(medcard_num: int, request: Request,   
                                      service: MedicalRecordService = Depends(),
                                      parents_service: ParentService = Depends(),
                                      allergy_service: AllergyService = Depends(),
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
                                      screening_service: ScreeningService = Depends(),
                                      visit_specialist_control_service: VisitSpecialistControlService = Depends(),
                                      user: User = Depends(get_current_user)):
    if user:
        filename = f"./static/files/{medcard_num}.xlsx"
        child = service.get_medcard_by_num(medcard_num=medcard_num)
        if child:
            create_file_with_child_tab(filename=filename, child_data=child)
            append_data_in_xlsx_file(data=[child.clinic],tab_name=BaseTableNameModel.Clinic, filename=filename) 
            father, mother = service.get_parents_by_medcard_num(medcard_num=medcard_num,parent_service=parents_service)
            if father or mother:
              append_data_in_xlsx_file(data=[father, mother],tab_name=BaseTableNameModel.Parent, filename=filename)
            allergies = allergy_service.get_allergies_by_medcard_num(medcard_num=medcard_num)
            append_data_in_xlsx_file(data=allergies,tab_name=BaseTableNameModel.Allergy, filename=filename)
            extra_classes = extra_class_service.get_extra_classes_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=extra_classes,tab_name=BaseTableNameModel.ExtraClass, filename=filename)
            past_illnesses = past_illness_service.get_past_illnesses_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=past_illnesses,tab_name=BaseTableNameModel.PastIllness, filename=filename)
            hospitalizations = hospitalization_service.get_hospitalizations_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=hospitalizations,tab_name=BaseTableNameModel.Hospitalization, filename=filename)
            spa_treatments = spa_treatment_service.get_spa_treatments_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=spa_treatments,tab_name=BaseTableNameModel.SpaTreatment, filename=filename)
            medical_certificates = medical_certificate_service.get_medical_certificates_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=medical_certificates,tab_name=BaseTableNameModel.MedicalCertificate, filename=filename)
            dispensaries = dispensary_service.get_dispensaries_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=dispensaries,tab_name=BaseTableNameModel.Dispensary, filename=filename)
            dewormings = deworming_service.get_dewormings_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=dewormings,tab_name=BaseTableNameModel.Deworming, filename=filename)
            oral_sanations = oral_sanation_service.get_oral_sanations_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=oral_sanations,tab_name=BaseTableNameModel.OralSanation, filename=filename)
            prof_vac_names = vac_name_service.get_vac_names_by_type('Профилактическая')
            epid_vac_names = vac_name_service.get_vac_names_by_type('По показаниям')
            append_data_in_xlsx_file(data=prof_vac_names + epid_vac_names,tab_name=BaseTableNameModel.VacName, filename=filename)
            prevaccination_checkups = prevaccination_checkup_service.get_prevaccination_checkups_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=prevaccination_checkups,tab_name=BaseTableNameModel.PrevaccinationCheckup, filename=filename)
            vaccinations = vaccination_service.get_vaccinations_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=vaccinations,tab_name=BaseTableNameModel.Vaccination, filename=filename)
            gg_injections = gg_injection_service.get_gamma_globulin_injections_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=gg_injections,tab_name=BaseTableNameModel.GammaGlobulinInjection, filename=filename)
            mantoux_tests = mantoux_test_service.get_mantoux_tests_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=mantoux_tests,tab_name=BaseTableNameModel.MantouxTest, filename=filename)
            tub_vacs = tub_vac_service.get_tuberculosis_vaccinations_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=tub_vacs,tab_name=BaseTableNameModel.TuberculosisVaccination, filename=filename)
            medical_examinations = medical_examination_service.get_medical_examinations_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=medical_examinations,tab_name=BaseTableNameModel.MedicalExamination, filename=filename)
            ongoing_medical_supervisions = ongoing_medical_supervision_service.get_ongoing_medical_supervisions_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=ongoing_medical_supervisions,tab_name=BaseTableNameModel.OngoingMedicalSupervision, filename=filename)
            screenings = screening_service.get_screenings_by_medcard_num(
                medcard_num=medcard_num)
            append_data_in_xlsx_file(data=screenings,tab_name=BaseTableNameModel.Screening, filename=filename)
            visit_specialist_controls = []
            for dispensary in dispensaries:
                visit_specialist_control = visit_specialist_control_service.get_visit_specialist_controls_by_dispensary(VisitSpecialistControlMain(dispensary_id=dispensary.id))
                visit_specialist_controls += visit_specialist_control
            append_data_in_xlsx_file(data=visit_specialist_controls,tab_name=BaseTableNameModel.VisitSpecialistControl, filename=filename)

        return FileResponse(filename, filename=filename, media_type="text/csv")
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )