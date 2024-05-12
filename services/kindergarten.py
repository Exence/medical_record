from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.child import ChildWithParentsView as ChildWithParentsViewModel
from models.kindergarten import KindergartenUpdate, KindergartenCreate, KindergartenWithchildren
from models.user import User

from services.medical_record.medical_record import MedicalRecordService

from tables import Kindergarten, Child


class KindergartenService():
    def __init__(self, medcard_service: MedicalRecordService = Depends()):
        self.medcard_service = medcard_service

    def get_kindergarten_with_children(self,
                                        user: User
                                        ) -> KindergartenWithchildren:
        children = self.medcard_service.get_children_with_parents(user=user)
        kindergarten_with_children = KindergartenWithchildren(groups=dict())
        kindergarten_with_children['name'] = user.kindergarten_name
        
        for child in children:
            child = ChildWithParentsViewModel(**child.__dict__)
            if not kindergarten_with_children['groups'].get(f"{child.group_num}"):
                kindergarten_with_children['groups'][f"{
                    child.group_num}"] = [child]
            else:
                kindergarten_with_children['groups'][f"{
                    child.group_num}"].append(child)
        return kindergarten_with_children
