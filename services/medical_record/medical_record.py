from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.child import ChildCreate, ChildEdit
from models.user import User
from tables import Child, ChildWithParents


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

    def add_new_medcard(self, user: User, child_data: ChildCreate):
        medcard = Child(**child_data.dict())
        self.session.add(medcard)
        self.session.commit()
        return medcard

    def update_medcard(self, user: User, medcard_data: ChildEdit):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_data.medcard_num):
            medcard = self._get(medcard_data.medcard_num)
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
        print(childrens_with_parents)
        return childrens_with_parents
