from fastapi import (
    APIRouter,
    Depends,  
)
from models.json import JsonForm
from models.user import User
from services.medical_record.parent import ParentService
from services.auth import get_current_user_from_cookie


router = APIRouter(
    prefix='/parent',
    tags=['Parent']
)

@router.post('/add')
async def update_parent(parent_data: JsonForm,
                        user: User = Depends(get_current_user_from_cookie),
                        service: ParentService = Depends()):
    parent = parent_data.json_data
    parent_id = service.add_parent(parent)
    return {"id": parent_id}

@router.post('/update')
async def update_parent(parent_data: JsonForm,
                        user: User = Depends(get_current_user_from_cookie),
                        service: ParentService = Depends()):
    parent = parent_data.json_data
    service.update_parent(parent)

@router.post('/delete')
async def delete_parent(parent_data: JsonForm,
                        user: User = Depends(get_current_user_from_cookie),
                        service: ParentService = Depends()):
    parent = parent_data.json_data
    service.delete_parent(parent)
