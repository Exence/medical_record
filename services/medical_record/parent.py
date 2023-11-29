from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.parent import ParentUpdate, ParentCreate
from models.user import User
from tables import Parent, Child

class ParentService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, parent_id: int) -> Parent:
        parent = (
            self.session
            .query(Parent)
            .filter_by(id=parent_id)
            .first()
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Parent is not found'
            )
        return parent
    
    def get_parent_by_id(self, user: User, medcard_num: int, parent_id: int):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            parent = self._get(parent_id)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return parent

    def add_new_parent(self, user: User, medcard_num: int, parent_data: ParentCreate):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            transaction = self.session.begin()
            try:
                parent = Parent(**parent_data.dict())
                self.session.add(parent)
                child = (
                    self.session
                    .query(Child)
                    .filter_by(medcard_num=medcard_num)
                    .first()
                )
                setattr(child, f"{parent_data.parent_type}_id", parent.id)
                transaction.commit()
            except Exception as error:
                print(error)
                transaction.rollback()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return parent

    def update_parent(self, user: User, medcard_num: int, parent_data: ParentUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            parent = self._get(parent_data.id)
            for field, value in parent_data:
                setattr(parent, field, value)
            self.session.commit()
            return parent
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_parent(self, user: User, medcard_num: int, parent_id: int):
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            parent = self._get(parent_id)
            self.session.delete(parent)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
