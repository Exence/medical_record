from fastapi import APIRouter
from .child import router as child_router
from .medical_record import router as medical_record_router
from .auth import router as auth_router
from .catalogs import router as catalogs_router
from .export_data import router as export_router
from .import_data import router as import_router


router = APIRouter(
  prefix='/api/v1'
)

sub_routers = [
    child_router,
    medical_record_router,
    auth_router,
    catalogs_router,
    export_router,
    import_router,
]

for sub_router in sub_routers:
    router.include_router(sub_router)
