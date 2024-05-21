import os
from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    status,
    Request,
    UploadFile,
)
from models.user import User
from services.auth import get_current_user
from services.user import check_user_access_to_medcard
from services.import_data import import_from_xlsx
from services.catalogs.clinic import ClinicService
from services.medical_record.medical_record import MedicalRecordService
from services.medical_record.parent import ParentService
from services.medical_record.dispensary import DispensaryService
from services.medical_record.visit_specialist_control import VisitSpecialistControlService
from services.medical_record.allergy import AllergyService
from services.medical_record.extra_class import ExtraClassService
from services.medical_record.past_illness import PastIllnessService
from services.medical_record.hospitalization import HospitalizationService
from services.medical_record.spa_treatment import SpaTreatmentService
from services.medical_record.medical_certificate import MedicalCertificateService
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


router = APIRouter(
    prefix='/medical_record/import',
    tags=['Import from xlsx']
)

@router.post('/')
async def import_data_from_xlsx(request: Request,
                          file: UploadFile = File(...),
                          user: User = Depends(get_current_user),
                          medcard_service: MedicalRecordService = Depends(),
                          clinic_service: ClinicService = Depends(),
                          parent_service: ParentService = Depends(),
                          dispensary_service: DispensaryService = Depends(),
                          visit_s_control_service: VisitSpecialistControlService = Depends(),
                          allergy_service: AllergyService = Depends(),
                          extra_class_service: ExtraClassService = Depends(),
                          past_illness_service: PastIllnessService = Depends(),
                          hospitalization_service: HospitalizationService = Depends(),
                          spa_treatment_service: SpaTreatmentService = Depends(),
                          medical_certificate_service: MedicalCertificateService = Depends(),
                          deworming_service: DewormingService = Depends(),
                          oral_sanation_service: OralSanationService = Depends(),
                          prevaccination_checkup_service: PrevaccinationCheckupService = Depends(),
                          vaccination_service: VaccinationService = Depends(),
                          gg_injection_service: GammaGlobulinInjectionService = Depends(),
                          mantoux_test_service: MantouxTestService = Depends(),
                          tub_vac_service: TuberculosisVaccinationService = Depends(),
                          medical_examination_service: MedicalExaminationService = Depends(),
                          ongoing_medical_supervision_service: OngoingMedicalSupervisionService = Depends(),
                          screening_service: ScreeningService = Depends(),
                          vac_name_service: VacNameService = Depends(),):
    """
    Импорт медкарты из файла
    """
    if user:
        try:
            contents = await file.read()
            filename = f"./static/files/{user.kindergarten_num}_{file.filename}"
            with open(filename, "wb") as f:
                f.write(contents)
        except:
            raise HTTPException(
                status_code=422,
                detail='Проблемы при загрузке файла'
            )

        try:
            import_from_xlsx(filename=filename, 
                            kindergarten_num=user.kindergarten_num,
                            medcard_service=medcard_service,
                            clinic_service=clinic_service,
                            parent_service=parent_service,
                            dispensary_service=dispensary_service,
                            visit_s_control_service=visit_s_control_service,
                            allergy_service=allergy_service,
                            extra_class_service=extra_class_service,
                            past_illness_service=past_illness_service,
                            hospitalization_service=hospitalization_service,
                            spa_treatment_service=spa_treatment_service,
                            medical_certificate_service=medical_certificate_service,
                            deworming_service=deworming_service,
                            oral_sanation_service=oral_sanation_service,
                            prevaccination_checkup_service=prevaccination_checkup_service,
                            vaccination_service=vaccination_service,
                            gg_injection_service=gg_injection_service,
                            mantoux_test_service=mantoux_test_service,
                            tub_vac_service=tub_vac_service,
                            medical_examination_service=medical_examination_service,
                            ongoing_medical_supervision_service=ongoing_medical_supervision_service,
                            screening_service=screening_service,
                            vac_name_service=vac_name_service)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=422,
                detail='Проблемы при импорте данных. Возможно не все данные были добавлены'
            )
        if os.path.exists(filename):
            os.remove(filename)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    