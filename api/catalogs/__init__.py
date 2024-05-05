from fastapi import APIRouter

from .clinics import router as clinic_router
from .vac_names import router as vac_names_router


router = APIRouter(
  prefix='/catalogs'
)

router.include_router(clinic_router)
router.include_router(vac_names_router)
