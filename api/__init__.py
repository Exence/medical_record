from fastapi import APIRouter
from .main import router as main_router
from .auth import router as auth_router
from .user import router as user_router
from .medical_record import router as medical_record_router


router = APIRouter()
router.include_router(main_router)
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(medical_record_router)
