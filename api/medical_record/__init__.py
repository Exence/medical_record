from fastapi import APIRouter

from .child import router as child_router
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


sub_routers = [
    child_router,
    allergy_router,
    deworming_router,
    dispensary_router,
    epid_vaccination_router,
    extra_class_router,
    gg_injection_router,
    hospitalization_router,
    mantoux_test_router,
    medical_certificate_router,
    medical_examination_router,
    ongoing_medical_supervision_router,
    oral_sanation_router,
    parent_router,
    past_illness_router,
    prevaccination_checkup_router,
    prof_vaccination_router,
    screening_router,
    spa_treatment_router,
    tub_vac_router,
    vaccination_router,
    visit_specialist_control_router,
]

router = APIRouter(
    prefix='/children/{medcard_num}'
)

for sub_router in sub_routers:
    router.include_router(sub_router)
