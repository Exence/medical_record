from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.spa_treatment import SpaTreatmentUpdate, SpaTreatmentCreate, SpaTreatmentPK
from models.user import User
from tables import SpaTreatment


class SpaTreatmentService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, start_date: date) -> SpaTreatment:
        spa_treatment = (
            self.session
            .query(SpaTreatment)
            .filter_by(medcard_num=medcard_num, start_date=start_date)
            .first()
        )

        if not spa_treatment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='SpaTreatment is not found'
            )
        return spa_treatment

    def get_spa_treatments_by_medcard_num(self, medcard_num: int) -> list[SpaTreatment]:
        query = (
            self.session.query(SpaTreatment)
            .filter_by(medcard_num=medcard_num)
            .order_by(SpaTreatment.start_date)
        )
        spa_treatments = query.all()
        return spa_treatments

    def get_spa_treatment_by_pk(self, spa_treatment_pk: SpaTreatmentPK):
        spa_treatment = self._get_by_pk(
                spa_treatment_pk.medcard_num, spa_treatment_pk.start_date)
        return spa_treatment

    def add_new_spa_treatment(self, spa_treatment_data: SpaTreatmentCreate):
        spa_treatment = SpaTreatment(**spa_treatment_data.dict())
        self.session.add(spa_treatment)
        self.session.commit()
        return spa_treatment

    def update_spa_treatment(self, spa_treatment_data: SpaTreatmentUpdate):
        spa_treatment = self._get_by_pk(
            spa_treatment_data.medcard_num, spa_treatment_data.prev_start_date)
        for field, value in spa_treatment_data:
            if field != 'prev_start_date':
                setattr(spa_treatment, field, value)
        self.session.commit()
        return spa_treatment

    def delete_spa_treatment(self, spa_treatment_pk: SpaTreatmentPK):
        spa_treatment = self._get_by_pk(
            spa_treatment_pk.medcard_num, spa_treatment_pk.start_date)
        self.session.delete(spa_treatment)
        self.session.commit()
