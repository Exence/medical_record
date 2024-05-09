from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.medical_record.parent import ParentService
from services.user import check_user_access_to_medcard

from models.child import ChildCreate, ChildEdit, CreateChildForm
from models.parent import ParentCreate, ParentType
from models.user import User
from tables import Child, ChildWithParents


def get_parent_data_from_str(str_data: str, parent_type: ParentType) -> ParentCreate | None:
    parent = str_data.split(";")
    return ParentCreate(
        surname=parent[0],
        name=parent[1],
        patronymic=parent[2],
        birthday_year=parent[3],
        education=parent[4],
        phone_num=parent[5],
        parent_type=parent_type
    ) if len(parent) == 6 else None

class MedicalRecordService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, medcard_num: int) -> Child:
        medcard = (
            self.session
            .query(Child)
            .filter_by(medcard_num=medcard_num)
            .first()
        )

        if not medcard:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='child is not found'
            )
        return medcard

    def get_medcard_by_num(self, user: User, medcard_num: int) -> Child:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            medcard = self._get(medcard_num)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medcard

    def add_new_medcard(self, user: User, child_form: CreateChildForm, parent_service: ParentService):
        child_data = dict()
        for key, value in child_form:
            if key not in ['father', 'mother', 'kindergarten_name']:
                child_data[key] = value
        child_data['father_id'] = None
        child_data['mother_id'] = None
        child_data['kindergarten_num'] = user.kindergarten_num

        medcard = Child(**child_data)
        self.session.add(medcard)
        self.session.commit()
        self.session.refresh(medcard)
        medcard_num = medcard.medcard_num
        self.session.close()

        father_data = get_parent_data_from_str(child_form.father, ParentType.FATHER)
        mother_data = get_parent_data_from_str(child_form.mother, parent_type=ParentType.MOTHER)
        
        parent_service.add_new_parent(user=user, 
                                      medcard_num=medcard_num, 
                                      parent_data=father_data) if father_data else dict(id=None)
        parent_service.add_new_parent(user=user, 
                                      medcard_num=medcard_num, 
                                      parent_data=mother_data) if mother_data else dict(id=None)
        return medcard

    def update_medcard(self, user: User, medcard_num: int, medcard_data: ChildEdit):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            medcard = self._get(medcard_num)
            for field, value in medcard_data:
                setattr(medcard, field, value)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medcard

    def delete_medcard(self, user: User, medcard_num: int):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            medcard = self._get(medcard_num)
            self.session.delete(medcard)
            self.session.commit()
            return {'detail': 'Medcard deleted'}
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def get_all_medcards(self, user: User) -> list[Child]:
        medcards = (
                self.session
                .query(Child)
                .filter_by(kindergarten_num=user.kindergarten_num)
                .order_by(Child.group_num)
                .all()
            )
        return medcards
    
    def get_childrens_with_parents(self, user: User) -> list[ChildWithParents]:
        childrens_with_parents = (
                self.session
                .query(ChildWithParents)
                .filter_by(kindergarten_num=user.kindergarten_num)
                .order_by(ChildWithParents.group_num)
                .all()
            )
        return childrens_with_parents
    
    def get_parents_by_medcard_num(self, user: User, medcard_num: int, parent_service: ParentService):
        child = self.get_medcard_by_num(user=user, medcard_num=medcard_num)
        father = parent_service._get(child.father_id) if child.father_id else None
        mother = parent_service._get(child.mother_id) if child.mother_id else None
        return father, mother
    
    def delete_parent_by_type(self, user: User, medcard_num: int, parent_type: ParentType, parent_service: ParentService):
        child = self.get_medcard_by_num(user=user, medcard_num=medcard_num)
        parents = {"father": child.father_id, "mother": child.mother_id}
        parent = parent_service._get(parents[f"{parent_type.value}"])
        self.session.delete(parent)
        setattr(child, f"{parent_type.value}_id", None)
        self.session.commit()
