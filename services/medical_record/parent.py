from fastapi import (
    Depends,
    HTTPException,
    status,
)

from services.medical_record.medical_record import MedicalRecordService
from services.user import check_user_access_to_medcard

from models.child import Child, ChildPK
from models.parent import Parent, ParentUpdate, ParentCreate, PatentType
from models.user import User


class ParentService():
    def __init__(self, medical_record_service: MedicalRecordService = Depends()):
        self.medical_record_service = medical_record_service

    def get_parent_by_type(self, user: User, child_pk: ChildPK, parent_type: PatentType) -> Parent:
        child_table = self.medical_record_service.get_medcard_by_num(
            user=user, medcard_num=child_pk.medcard_num)
        child = dict(**child_table.__dict__)
        parent = child[parent_type]
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Parent is not found'
            )
        return parent

    def add_or_update_parent(self, user: User, child_pk: ChildPK, parent_data: ParentCreate) -> Parent:
        child_table = self.medical_record_service.get_medcard_by_num(
            user=user, medcard_num=child_pk.medcard_num)
        child = dict(**child_table.__dict__)
        parent = Parent(**parent_data.dict())
        child[parent_data.parent_type] = parent
        child = Child(**child)
        self.medical_record_service.update_medcard(
            user=user, medcard_data=child)
        return parent

    def delete_parent(self, user: User, child_pk: ChildPK, parent_type: PatentType):
        child_table = self.medical_record_service.get_medcard_by_num(
            user=user, medcard_num=child_pk.medcard_num)
        child = dict(**child_table.__dict__)
        child[parent_type] = {}
        child = Child(**child)
        self.medical_record_service.update_medcard(
            user=user, medcard_data=child)
