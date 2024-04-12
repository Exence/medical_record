from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.child import ChildWithParentsView as ChildWithParentsViewModel
from models.kindergarten import KindergartenUpdate, KindergartenCreate, KindergartenWithChildrens
from models.user import User

from services.medical_record.medical_record import MedicalRecordService

from tables import Kindergarten, Child


class KindergartenService():
    def __init__(self, medcard_service: MedicalRecordService = Depends()):
        self.medcard_service = medcard_service

    def get_kindergarten_with_childrens(self,
                                        user: User
                                        ) -> KindergartenWithChildrens:
        childrens = self.medcard_service.get_childrens_with_parents(user=user)
        kindergarten_with_childrens = KindergartenWithChildrens(groups=dict())
        kindergarten_with_childrens['name'] = user.kindergarten_name
        
        for child in childrens:
            child = ChildWithParentsViewModel(**child.__dict__)
            if not kindergarten_with_childrens['groups'].get(f"{child.group_num}"):
                kindergarten_with_childrens['groups'][f"{
                    child.group_num}"] = [child]
            else:
                kindergarten_with_childrens['groups'][f"{
                    child.group_num}"].append(child)
        return kindergarten_with_childrens
