from fastapi import APIRouter
from .main import router as main_router
from .auth import router as auth_router
from .catalogs import router as catalogs_router
from .user import router as user_router
from .medical_record.medical_record import router as medical_record_router
from .report import router as report_router


sub_routers = [
    main_router,
    auth_router,
    catalogs_router,
    user_router,
    medical_record_router,
    report_router,
]
router = APIRouter()

for sub_router in sub_routers:
    router.include_router(sub_router)
