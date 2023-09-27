from fastapi import APIRouter
from .allergy import router as allergy_router
from .deworming import router as deworming_router
from .dispensary import router as dispensary_router
from .epid_vaccination import router as epid_vaccination_router
from .extra_class import router as extra_class_router
from .gg_injection import router as gg_injection_router
from .hospitalization import router as hospitalization_router
from .mantoux_test import router as mantoux_test_router
from .medical_certificate import router as medical_certificate_router
from .medical_examination import router as medical_examination_router
from .ongoing_medical_supervision import router as ongoing_medical_supervision_router
from .oral_sanation import router as oral_sanation_router
from .parent import router as parent_router
from .past_illness import router as past_illness_router
from .prevaccination_checkup import router as prevaccination_checkup_router
from .prof_vaccination import router as prof_vaccination_router
from .screening import router as screening_router
from .spa_treatment import router as spa_treatment_router
from .tub_vac import router as tub_vac_router
from .vaccination import router as vaccination_router
from .visit_specialist_control import router as visit_specialist_control_router



router = APIRouter()
router.include_router(allergy_router)
router.include_router(deworming_router)
router.include_router(dispensary_router)
router.include_router(epid_vaccination_router)
router.include_router(extra_class_router)
router.include_router(gg_injection_router)
router.include_router(hospitalization_router)
router.include_router(mantoux_test_router)
router.include_router(medical_certificate_router)
router.include_router(medical_examination_router)
router.include_router(ongoing_medical_supervision_router)
router.include_router(oral_sanation_router)
router.include_router(parent_router)
router.include_router(past_illness_router)
router.include_router(prevaccination_checkup_router)
router.include_router(prof_vaccination_router)
router.include_router(screening_router)
router.include_router(spa_treatment_router)
router.include_router(tub_vac_router)
router.include_router(vaccination_router)
router.include_router(visit_specialist_control_router)
