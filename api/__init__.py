from fastapi import APIRouter

from .medical_record import router as medical_record_router


router = APIRouter()

router.include_router(medical_record_router)
