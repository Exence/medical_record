from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.oral_sanation import OralSanationUpdate, OralSanationCreate, OralSanationPK
from models.user import User
from tables import OralSanation


class OralSanationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, sanation_date: date) -> OralSanation:
        oral_sanation = (
            self.session
            .query(OralSanation)
            .filter_by(medcard_num=medcard_num, sanation_date=sanation_date)
            .first()
        )

        if not oral_sanation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='OralSanation is not found'
            )
        return oral_sanation

    def get_oral_sanations_by_medcard_num(self, user: User, medcard_num: int) -> list[OralSanation]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(OralSanation)
                .filter_by(medcard_num=medcard_num)
                .order_by(OralSanation.sanation_date)
            )
            oral_sanations = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return oral_sanations

    def get_oral_sanation_by_pk(self, user: User, oral_sanation_pk: OralSanationPK):
        if check_user_access_to_medcard(user=user, medcard_num=oral_sanation_pk.medcard_num):
            oral_sanation = self._get_by_pk(
                oral_sanation_pk.medcard_num, oral_sanation_pk.sanation_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return oral_sanation

    def add_new_oral_sanation(self, user: User, oral_sanation_data: OralSanationCreate):
        if check_user_access_to_medcard(user=user, medcard_num=oral_sanation_data.medcard_num):
            oral_sanation = OralSanation(**oral_sanation_data.dict())
            self.session.add(oral_sanation)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return oral_sanation

    def update_oral_sanation(self, user: User, oral_sanation_data: OralSanationUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=oral_sanation_data.medcard_num):
            oral_sanation = self._get_by_pk(
                oral_sanation_data.medcard_num, oral_sanation_data.prev_sanation_date)
            for field, value in oral_sanation_data:
                if field != 'prev_sanation_date':
                    setattr(oral_sanation, field, value)
            self.session.commit()
            return oral_sanation
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_oral_sanation(self, user: User, oral_sanation_pk: OralSanationPK):
        if check_user_access_to_medcard(user=user, medcard_num=oral_sanation_pk.medcard_num):
            oral_sanation = self._get_by_pk(
                oral_sanation_pk.medcard_num, oral_sanation_pk.sanation_date)
            self.session.delete(oral_sanation)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
