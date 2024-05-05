from fastapi import APIRouter

from .clinic import router as clinic_router


router = APIRouter(
  prefix='/catalogs'
)

router.include_router(clinic_router)