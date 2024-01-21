from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.deworming import DewormingUpdate, DewormingCreate, DewormingPK
from models.user import User
from tables import Deworming


class DewormingService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, deworming_date: date) -> Deworming:
        deworming = (
            self.session
            .query(Deworming)
            .filter_by(medcard_num=medcard_num, deworming_date=deworming_date)
            .first()
        )

        if not deworming:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Deworming is not found'
            )
        return deworming

    def get_dewormings_by_medcard_num(self, user: User, medcard_num: int) -> list[Deworming]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(Deworming)
                .filter_by(medcard_num=medcard_num)
                .order_by(Deworming.deworming_date)
            )
            dewormings = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return dewormings

    def get_deworming_by_pk(self, user: User, deworming_pk: DewormingPK):
        if check_user_access_to_medcard(user=user, medcard_num=deworming_pk.medcard_num):
            deworming = self._get_by_pk(
                deworming_pk.medcard_num, deworming_pk.deworming_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return deworming

    def add_new_deworming(self, user: User, deworming_data: DewormingCreate):
        if check_user_access_to_medcard(user=user, medcard_num=deworming_data.medcard_num):
            deworming = Deworming(**deworming_data.dict())
            self.session.add(deworming)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return deworming

    def update_deworming(self, user: User, deworming_data: DewormingUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=deworming_data.medcard_num):
            deworming = self._get_by_pk(
                deworming_data.medcard_num, deworming_data.prev_deworming_date)
            for field, value in deworming_data:
                if field != 'prev_deworming_date':
                    setattr(deworming, field, value)
            self.session.commit()
            return deworming
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_deworming(self, user: User, deworming_pk: DewormingPK):
        if check_user_access_to_medcard(user=user, medcard_num=deworming_pk.medcard_num):
            deworming = self._get_by_pk(
                deworming_pk.medcard_num, deworming_pk.deworming_date)
            self.session.delete(deworming)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
