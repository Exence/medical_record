from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.child import Child as ChildModel
from models.kindergarten import KindergartenUpdate, KindergartenCreate, KindergartenWithChildrens
from models.user import User

from tables import Kindergarten, Child


class KindergartenService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, kindergarten_num: int) -> Kindergarten:
        kindergarten = (
            self.session
            .query(Kindergarten)
            .filter_by(number=kindergarten_num)
            .first()
        )

        if not kindergarten:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Kindergarten is not found'
            )
        return kindergarten

    def get_all_kindergartens(self) -> list[Kindergarten]:
        query = (
            self.session.query(Kindergarten)
            .order_by(Kindergarten.number)
        )
        kindergartens = query.all()

        return kindergartens

    def get_kindergarten_by_num(self, kindergarten_num: int):
        return self._get(kindergarten_num)

    def get_kindergartens_by_user_access(self, user: User) -> list[Kindergarten]:
        query = (
            self.session.query(Kindergarten)
            .order_by(Kindergarten.name)
            .filter(Kindergarten.name != 'admins')
        )
        if user.access_level == 'user':
            query.filter_by(number=user.kindergarten_num)
        kindergartens = query.all()

        return kindergartens

    def add_new_kindergarten(self, user: User, kindergarten_data: KindergartenCreate):
        if user.access_level == 'admin' or user.access_level == 'db_admin':
            kindergarten = kindergarten(**kindergarten_data.dict())
            self.session.add(kindergarten)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return kindergarten

    def update_kindergarten(self, user: User, kindergarten_data: KindergartenUpdate):
        if user.access_level == 'admin' or user.access_level == 'db_admin':
            kindergarten = self._get(kindergarten_data.prev_number)
            for field, value in kindergarten_data:
                if field != 'prev_number':
                    setattr(kindergarten, field, value)
            self.session.commit()
            return kindergarten
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_kindergarten(self, user: User, kindergarten_num: int):
        if user.access_level == 'admin' or user.access_level == 'db_admin':
            kindergarten = self._get(kindergarten_num)
            self.session.delete(kindergarten)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def get_medcards_by_kindergarten_num(self, user: User, kindergarten_num: int) -> list[Child]:
        if user.access_level == 'admin' or user.access_level == 'db_admin' or user.kindergarten_num == kindergarten_num:
            medcards = (
                self.session
                .query(Child)
                .filter_by(kindergarten_num=kindergarten_num)
                .order_by(Child.group_num)
                .all()
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medcards

    def get_kindergarten_with_childrens(self,
                                        user: User,
                                        kindergarten_num: int
                                        ) -> KindergartenWithChildrens:
        childrens = self.get_medcards_by_kindergarten_num(
            user=user, kindergarten_num=kindergarten_num)
        kindergarten_with_childrens = KindergartenWithChildrens(groups=dict())
        for child in childrens:
            child = ChildModel(**child.__dict__)
            if not kindergarten_with_childrens['groups'].get(f"{child.group_num}"):
                kindergarten_with_childrens['groups'][f"{
                    child.group_num}"] = [child]
            else:
                kindergarten_with_childrens['groups'][f"{
                    child.group_num}"].append(child)
        return kindergarten_with_childrens

    def get_all_accessible_kindergartens_with_childrens(self, user: User) -> list[KindergartenWithChildrens]:
        if user.access_level == 'user':
            return self.get_kindergarten_with_childrens(user=user, kindergarten_num=user.kindergarten_num)
        else:
            kindergartens = self.get_all_kindergartens()
            kindergartens_with_childrens = []
            for kindergarten in kindergartens:
                kindergartens_with_childrens.append(
                    self.get_kindergarten_with_childrens(
                        user=user, kindergarten_num=kindergarten.number)
                )
        return kindergartens_with_childrens
