from fastapi import APIRouter
from .main import router as main_router
from .auth import router as auth_router
from .clinic import router as clinic_router
from .user import router as user_router
from .medical_record.medical_record import router as medical_record_router
from .report import router as report_router
from .vaccine import router as vac_router


sub_routers = [
    main_router,
    auth_router,
    clinic_router,
    user_router,
    medical_record_router,
    report_router,
    vac_router,
]
router = APIRouter()

for sub_router in sub_routers:
    router.include_router(sub_router)
