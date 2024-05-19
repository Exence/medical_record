from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionUpdate, OngoingMedicalSupervisionCreate, OngoingMedicalSupervisionPK
from models.user import User
from tables import OngoingMedicalSupervision


class OngoingMedicalSupervisionService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, medcard_num: int, examination_date: date) -> OngoingMedicalSupervision:
        ongoing_medical_supervision = (
            self.session
            .query(OngoingMedicalSupervision)
            .filter_by(medcard_num=medcard_num, examination_date=examination_date)
            .first()
        )

        if not ongoing_medical_supervision:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='OngoingMedicalSupervision is not found'
            )
        return ongoing_medical_supervision

    def get_ongoing_medical_supervisions_by_medcard_num(self, medcard_num: int) -> list[OngoingMedicalSupervision]:
        ongoing_medical_supervisions = (
            self.session.query(OngoingMedicalSupervision)
            .filter_by(medcard_num=medcard_num)
            .order_by(OngoingMedicalSupervision.examination_date)
            .all()
        )
        return ongoing_medical_supervisions

    def get_ongoing_medical_supervision_by_pk(self, ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK):
        ongoing_medical_supervision = self._get(
                ongoing_medical_supervision_pk.medcard_num, ongoing_medical_supervision_pk.examination_date)
        return ongoing_medical_supervision

    def add_new_ongoing_medical_supervision(self, ongoing_medical_supervision_data: OngoingMedicalSupervisionCreate):
        ongoing_medical_supervision = OngoingMedicalSupervision(
            **ongoing_medical_supervision_data.dict())
        self.session.add(ongoing_medical_supervision)
        self.session.commit()
        return ongoing_medical_supervision

    def update_ongoing_medical_supervision(self, ongoing_medical_supervision_data: OngoingMedicalSupervisionUpdate):
        ongoing_medical_supervision = self._get(
            ongoing_medical_supervision_data.medcard_num, ongoing_medical_supervision_data.prev_examination_date)
        for field, value in ongoing_medical_supervision_data:
            if field != 'prev_examination_date':
                setattr(ongoing_medical_supervision, field, value)
        self.session.commit()
        return ongoing_medical_supervision

    def delete_ongoing_medical_supervision(self, ongoing_medical_supervision_pk: OngoingMedicalSupervisionPK):
        ongoing_medical_supervision = self._get(
            ongoing_medical_supervision_pk.medcard_num, ongoing_medical_supervision_pk.examination_date)
        self.session.delete(ongoing_medical_supervision)
        self.session.commit()
