from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.screening import ScreeningUpdate, ScreeningCreate, ScreeningPK
from models.user import User
from tables import Screening


class ScreeningService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, examination_date: date) -> Screening:
        screening = (
            self.session
            .query(Screening)
            .filter_by(medcard_num=medcard_num, examination_date=examination_date)
            .first()
        )

        if not screening:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Screening is not found'
            )
        return screening

    def get_screenings_by_medcard_num(self, user: User, medcard_num: int) -> list[Screening]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            screenings = (
                self.session.query(Screening)
                .filter_by(medcard_num=medcard_num)
                .order_by(Screening.age)
                .all()
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return screenings

    def get_screening_by_pk(self, user: User, screening_pk: ScreeningPK):
        if check_user_access_to_medcard(user=user, medcard_num=screening_pk.medcard_num):
            screening = self._get_by_pk(
                screening_pk.medcard_num, screening_pk.examination_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return screening

    def add_new_screening(self, user: User, screening_data: ScreeningCreate):
        if check_user_access_to_medcard(user=user, medcard_num=screening_data.medcard_num):
            screening = Screening(**screening_data.dict())
            self.session.add(screening)
            self.session.commit()
            self.session.refresh(screening)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return screening

    def update_screening(self, user: User, screening_data: ScreeningUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=screening_data.medcard_num):
            screening = self._get_by_pk(
                screening_data.medcard_num, screening_data.prev_examination_date)
            for field, value in screening_data:
                if field != 'prev_examination_date':
                    setattr(screening, field, value)
            self.session.commit()
            self.session.refresh(screening)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return screening

    def delete_screening(self, user: User, screening_pk: ScreeningPK):
        if check_user_access_to_medcard(user=user, medcard_num=screening_pk.medcard_num):
            screening = self._get_by_pk(
                screening_pk.medcard_num, screening_pk.examination_date)
            self.session.delete(screening)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
