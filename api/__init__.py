from fastapi import APIRouter

from .medical_record import router as medical_record_router
from .auth import router as auth_router
from .clinic import router as clinic_router


router = APIRouter()

router.include_router(medical_record_router)
router.include_router(auth_router)
router.include_router(clinic_router)
