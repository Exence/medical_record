from fastapi import APIRouter
from .child import router as child_router
from .medical_record import router as medical_record_router
from .auth import router as auth_router
from .catalogs import router as catalogs_router


router = APIRouter(
  prefix='/api/v1'
)

router.include_router(child_router)
router.include_router(medical_record_router)
router.include_router(auth_router)
router.include_router(catalogs_router)
