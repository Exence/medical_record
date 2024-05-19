from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.medical_record.screening import ScreeningUpdate, ScreeningCreate, ScreeningPK
from models.user import User
from tables import Screening


class ScreeningService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, medcard_num: int, examination_date: date) -> Screening:
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

    def get_screenings_by_medcard_num(self, medcard_num: int) -> list[Screening]:
        screenings = (
            self.session.query(Screening)
            .filter_by(medcard_num=medcard_num)
            .order_by(Screening.age)
            .all()
        )
        return screenings

    def get_screening_by_pk(self, screening_pk: ScreeningPK):
        screening = self._get(
                screening_pk.medcard_num, screening_pk.examination_date)
        return screening

    def add_new_screening(self, screening_data: ScreeningCreate):
        screening = Screening(**screening_data.dict())
        self.session.add(screening)
        self.session.commit()
        self.session.refresh(screening)
        return screening

    def update_screening(self, screening_data: ScreeningUpdate):
        screening = self._get(
            screening_data.medcard_num, screening_data.prev_examination_date)
        for field, value in screening_data:
            if field != 'prev_examination_date':
                setattr(screening, field, value)
        self.session.commit()
        self.session.refresh(screening)
        return screening

    def delete_screening(self, screening_pk: ScreeningPK):
        screening = self._get(
            screening_pk.medcard_num, screening_pk.examination_date)
        self.session.delete(screening)
        self.session.commit()
