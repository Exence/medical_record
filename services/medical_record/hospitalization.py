from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.medical_record.hospitalization import HospitalizationUpdate, HospitalizationCreate, HospitalizationPK
from models.user import User
from tables import Hospitalization


class HospitalizationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, medcard_num: int, start_date: date) -> Hospitalization:
        hospitalization = (
            self.session
            .query(Hospitalization)
            .filter_by(medcard_num=medcard_num, start_date=start_date)
            .first()
        )

        if not hospitalization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Hospitalization is not found'
            )
        return hospitalization

    def get_hospitalizations_by_medcard_num(self, medcard_num: int) -> list[Hospitalization]:
        hospitalizations = (
            self.session.query(Hospitalization)
            .filter_by(medcard_num=medcard_num)
            .order_by(Hospitalization.start_date)
            .all()
        )
        return hospitalizations

    def get_hospitalization_by_pk(self, hospitalization_pk: HospitalizationPK):
        hospitalization = self._get(
                hospitalization_pk.medcard_num, hospitalization_pk.start_date)
        return hospitalization

    def add_new_hospitalization(self, hospitalization_data: HospitalizationCreate):
        hospitalization = Hospitalization(**hospitalization_data.dict())
        self.session.add(hospitalization)
        self.session.commit()
        return hospitalization

    def update_hospitalization(self, hospitalization_data: HospitalizationUpdate):
        hospitalization = self._get(
            hospitalization_data.medcard_num, hospitalization_data.prev_start_date)
        for field, value in hospitalization_data:
            if field != 'prev_start_date':
                setattr(hospitalization, field, value)
        self.session.commit()
        return hospitalization

    def delete_hospitalization(self, hospitalization_pk: HospitalizationPK):
        hospitalization = self._get(
            hospitalization_pk.medcard_num, hospitalization_pk.start_date)
        self.session.delete(hospitalization)
        self.session.commit()
