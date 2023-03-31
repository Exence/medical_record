from fastapi import APIRouter
from .main import router as main_router
from .auth import router as auth_router


router = APIRouter()
router.include_router(main_router)
router.include_router(auth_router)