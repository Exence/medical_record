from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session

from services.user import check_user_access_to_medcard

from models.medical_certificate import MedicalCertificateUpdate, MedicalCertificateCreate, MedicalCertificatePK
from models.user import User
from tables import MedicalCertificate


class MedicalCertificateService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, disease: str, cert_date: date) -> MedicalCertificate:
        medical_certificate = (
            self.session
            .query(MedicalCertificate)
            .filter_by(medcard_num=medcard_num, disease=disease, cert_date=cert_date)
            .first()
        )

        if not medical_certificate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Medical certificate is not found'
            )
        return medical_certificate

    def get_medical_certificates_by_medcard_num(self, medcard_num: int) -> list[MedicalCertificate]:
        medical_certificates = (
            self.session.query(MedicalCertificate)
            .filter_by(medcard_num=medcard_num)
            .order_by(MedicalCertificate.cert_date)
            .all()
        )
        return medical_certificates

    def get_medical_certificate_by_pk(self, medical_certificate_pk: MedicalCertificatePK):
        medical_certificate = self._get_by_pk(
                medical_certificate_pk.medcard_num, medical_certificate_pk.disease, medical_certificate_pk.cert_date)
        return medical_certificate

    def add_new_medical_certificate(self, medical_certificate_data: MedicalCertificateCreate):
        medical_certificate = MedicalCertificate(
            **medical_certificate_data.dict())
        self.session.add(medical_certificate)
        self.session.commit()
        return medical_certificate

    def update_medical_certificate(self, medical_certificate_data: MedicalCertificateUpdate):
        medical_certificate = self._get_by_pk(
            medical_certificate_data.medcard_num, medical_certificate_data.prev_disease, medical_certificate_data.prev_cert_date)
        for field, value in medical_certificate_data:
            if field != 'prev_disease' and field != 'prev_cert_date':
                setattr(medical_certificate, field, value)
        self.session.commit()
        return medical_certificate

    def delete_medical_certificate(self, medical_certificate_pk: MedicalCertificatePK):
        medical_certificate = self._get_by_pk(
            medical_certificate_pk.medcard_num, medical_certificate_pk.disease, medical_certificate_pk.cert_date)
        self.session.delete(medical_certificate)
        self.session.commit()
