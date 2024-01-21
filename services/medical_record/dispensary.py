from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.dispensary import DispensaryUpdate, DispensaryCreate, DispensaryPK
from models.user import User
from tables import Dispensary


class DispensaryService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, start_date: date) -> Dispensary:
        dispensary = (
            self.session
            .query(Dispensary)
            .filter_by(medcard_num=medcard_num, start_date=start_date)
            .first()
        )

        if not dispensary:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Dispensary is not found'
            )
        return dispensary

    def get_dispensaryes_by_medcard_num(self, user: User, medcard_num: int) -> list[Dispensary]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(Dispensary)
                .filter_by(medcard_num=medcard_num)
                .order_by(Dispensary.start_date)
            )
            dispensaryes = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return dispensaryes

    def get_dispensary_by_pk(self, user: User, dispensary_pk: DispensaryPK):
        if check_user_access_to_medcard(user=user, medcard_num=dispensary_pk.medcard_num):
            dispensary = self._get_by_pk(
                dispensary_pk.medcard_num, dispensary_pk.start_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return dispensary

    def add_new_dispensary(self, user: User, dispensary_data: DispensaryCreate):
        if check_user_access_to_medcard(user=user, medcard_num=dispensary_data.medcard_num):
            dispensary = Dispensary(**dispensary_data.dict())
            self.session.add(dispensary)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return dispensary

    def update_dispensary(self, user: User, dispensary_data: DispensaryUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=dispensary_data.medcard_num):
            dispensary = self._get_by_pk(
                dispensary_data.medcard_num, dispensary_data.prev_start_date)
            for field, value in dispensary_data:
                if field != 'prev_start_date':
                    setattr(dispensary, field, value)
            self.session.commit()
            return dispensary
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_dispensary(self, user: User, dispensary_pk: DispensaryPK):
        if check_user_access_to_medcard(user=user, medcard_num=dispensary_pk.medcard_num):
            dispensary = self._get_by_pk(
                dispensary_pk.medcard_num, dispensary_pk.start_date)
            self.session.delete(dispensary)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
