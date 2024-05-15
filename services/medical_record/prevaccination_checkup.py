from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session

from services.user import check_user_access_to_medcard

from models.medical_record.prevaccination_checkup import (
    PrevaccinationCheckup as PrevaccinationCheckupModel,
    PrevaccinationCheckupUpdate, 
    PrevaccinationCheckupCreate, 
    PrevaccinationCheckupPK)
from models.user import User
from tables import PrevaccinationCheckup


class PrevaccinationCheckupService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, examination_date: date) -> PrevaccinationCheckup:
        prevaccination_checkup = (
            self.session
            .query(PrevaccinationCheckup)
            .filter_by(medcard_num=medcard_num, examination_date=examination_date)
            .first()
        )

        if not prevaccination_checkup:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Medical certificate is not found'
            )
        return prevaccination_checkup

    def get_prevaccination_checkups_by_medcard_num(self, medcard_num: int) -> list[PrevaccinationCheckupModel]:
        prevaccination_checkups = (
            self.session.query(PrevaccinationCheckup)
            .filter_by(medcard_num=medcard_num)
            .order_by(PrevaccinationCheckup.examination_date)
            .all()
        )
        return prevaccination_checkups

    def get_prevaccination_checkup_by_pk(self, prevaccination_checkup_pk: PrevaccinationCheckupPK):
        prevaccination_checkup = self._get_by_pk(
                prevaccination_checkup_pk.medcard_num, prevaccination_checkup_pk.examination_date)
        return prevaccination_checkup

    def add_new_prevaccination_checkup(self, prevaccination_checkup_data: PrevaccinationCheckupCreate):
        prevaccination_checkup = PrevaccinationCheckup(
            **prevaccination_checkup_data.dict())
        self.session.add(prevaccination_checkup)
        self.session.commit()
        return prevaccination_checkup

    def update_prevaccination_checkup(self, prevaccination_checkup_data: PrevaccinationCheckupUpdate):
        prevaccination_checkup = self._get_by_pk(
            prevaccination_checkup_data.medcard_num, prevaccination_checkup_data.examination_date)
        for field, value in prevaccination_checkup_data:
            if field != 'prev_examination_date':
                setattr(prevaccination_checkup, field, value)
        self.session.commit()
        return prevaccination_checkup

    def delete_prevaccination_checkup(self, prevaccination_checkup_pk: PrevaccinationCheckupPK):
        prevaccination_checkup = self._get_by_pk(
            prevaccination_checkup_pk.medcard_num, prevaccination_checkup_pk.examination_date)
        self.session.delete(prevaccination_checkup)
        self.session.commit()
