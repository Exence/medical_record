from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.mantoux_test import MantouxTestUpdate, MantouxTestCreate, MantouxTestPK
from models.user import User
from tables import MantouxTest


class MantouxTestService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, check_date: date) -> MantouxTest:
        mantoux_test = (
            self.session
            .query(MantouxTest)
            .filter_by(medcard_num=medcard_num, check_date=check_date)
            .first()
        )

        if not mantoux_test:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='MantouxTest is not found'
            )
        return mantoux_test

    def get_mantoux_tests_by_medcard_num(self, user: User, medcard_num: int) -> list[MantouxTest]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(MantouxTest)
                .filter_by(medcard_num=medcard_num)
                .order_by(MantouxTest.check_date)
            )
            mantoux_tests = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return mantoux_tests

    def get_mantoux_test_by_pk(self, user: User, mantoux_test_pk: MantouxTestPK):
        if check_user_access_to_medcard(user=user, medcard_num=mantoux_test_pk.medcard_num):
            mantoux_test = self._get_by_pk(
                mantoux_test_pk.medcard_num, mantoux_test_pk.check_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return mantoux_test

    def add_new_mantoux_test(self, user: User, mantoux_test_data: MantouxTestCreate):
        if check_user_access_to_medcard(user=user, medcard_num=mantoux_test_data.medcard_num):
            mantoux_test = MantouxTest(**mantoux_test_data.dict())
            self.session.add(mantoux_test)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return mantoux_test

    def update_mantoux_test(self, user: User, mantoux_test_data: MantouxTestUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=mantoux_test_data.medcard_num):
            mantoux_test = self._get_by_pk(
                mantoux_test_data.medcard_num, mantoux_test_data.prev_check_date)
            for field, value in mantoux_test_data:
                if field != 'prev_check_date':
                    setattr(mantoux_test, field, value)
            self.session.commit()
            return mantoux_test
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_mantoux_test(self, user: User, mantoux_test_pk: MantouxTestPK):
        if check_user_access_to_medcard(user=user, medcard_num=mantoux_test_pk.medcard_num):
            mantoux_test = self._get_by_pk(
                mantoux_test_pk.medcard_num, mantoux_test_pk.check_date)
            self.session.delete(mantoux_test)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
