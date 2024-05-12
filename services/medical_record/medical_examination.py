from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.medical_examination import MedicalExaminationUpdate, MedicalExaminationCreate, MedicalExaminationPK
from models.user import User
from tables import MedicalExamination


class MedicalExaminationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, period: str) -> MedicalExamination:
        medical_examination = (
            self.session
            .query(MedicalExamination)
            .filter_by(medcard_num=medcard_num, period=period)
            .first()
        )

        if not medical_examination:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='MedicalExamination is not found'
            )
        return medical_examination

    def get_medical_examinations_by_medcard_num(self, medcard_num: int) -> list[MedicalExamination]:
        medical_examinations = (
            self.session.query(MedicalExamination)
            .filter_by(medcard_num=medcard_num)
            .order_by(MedicalExamination.age)
            .all()
        )
        return medical_examinations

    def get_medical_examination_by_pk(self, medical_examination_pk: MedicalExaminationPK):
        medical_examination = self._get_by_pk(
                medical_examination_pk.medcard_num, medical_examination_pk.period)
        return medical_examination

    def add_new_medical_examination(self, medical_examination_data: MedicalExaminationCreate):
        medical_examination = MedicalExamination(
            **medical_examination_data.dict())
        self.session.add(medical_examination)
        self.session.commit()
        return medical_examination

    def update_medical_examination(self, medical_examination_data: MedicalExaminationUpdate):
        medical_examination = self._get_by_pk(
            medical_examination_data.medcard_num, medical_examination_data.prev_period)
        for field, value in medical_examination_data:
            if field != 'prev_period':
                setattr(medical_examination, field, value)
        self.session.commit()
        return medical_examination

    def delete_medical_examination(self, medical_examination_pk: MedicalExaminationPK):
        medical_examination = self._get_by_pk(
            medical_examination_pk.medcard_num, medical_examination_pk.period)
        self.session.delete(medical_examination)
        self.session.commit()
