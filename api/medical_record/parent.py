from fastapi import (
    APIRouter,
    Depends,  
)
from models.parent import (
    Parent,
    ParentCreate,
    ParentUpdate,
)
from models.user import User
from services.medical_record.parent import ParentService
from services.auth import get_current_user


router = APIRouter(
    prefix='/parent',
    tags=['Parent']
)

@router.post('/get_one', response_model=Parent)
async def get_parent_by_id(parent_id: int, 
                         user: User = Depends(get_current_user),
                         service: ParentService = Depends()):
    return service.get_parent_by_id(user=user, parent_id=parent_id)

@router.post('/add', response_model=Parent)
async def add_parent(parent_data: ParentCreate, 
                      user: User = Depends(get_current_user),
                      service: ParentService = Depends()):
    return service.add_new_parent(user=user, parent_data=parent_data)

@router.post('/update', response_model=Parent)
async def update_parent(parent_data: ParentUpdate, 
                         user: User = Depends(get_current_user),
                         service: ParentService = Depends()):
    return service.update_parent(user=user, parent_data=parent_data)

@router.post('/delete')
async def delete_parent(parent_id: int, 
                         user: User = Depends(get_current_user),
                         service: ParentService = Depends()):
    service.delete_parent(user=user, parent_id=parent_id)
