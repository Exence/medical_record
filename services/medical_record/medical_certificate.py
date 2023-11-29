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
            .filter_by(medcard_num=medcard_num,disease=disease,cert_date=cert_date)
            .first()
        )

        if not medical_certificate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Medical certificate is not found'
            )
        return medical_certificate

    def get_medical_certificates_by_medcard_num(self, user: User, medcard_num: int) -> list[MedicalCertificate]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(MedicalCertificate)
                .filter_by(medcard_num=medcard_num)
                .order_by(MedicalCertificate.cert_date)
            )
            medical_certificates = query.all()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medical_certificates
    
    def get_medical_certificate_by_pk(self, user: User, medical_certificate_pk: MedicalCertificatePK):
        if check_user_access_to_medcard(user=user, medcard_num=medical_certificate_pk.medcard_num):
            medical_certificate = self._get_by_pk(medical_certificate_pk.medcard_num, medical_certificate_pk.disease, medical_certificate_pk.cert_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medical_certificate

    def add_new_medical_certificate(self, user: User, medical_certificate_data: MedicalCertificateCreate):
        if check_user_access_to_medcard(user=user, medcard_num=medical_certificate_data.medcard_num):
            medical_certificate = MedicalCertificate(**medical_certificate_data.dict())
            self.session.add(medical_certificate)
            self.session.commit()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return medical_certificate

    def update_medical_certificate(self, user: User, medical_certificate_data: MedicalCertificateUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=medical_certificate_data.medcard_num):
            medical_certificate = self._get_by_pk(medical_certificate_data.medcard_num, medical_certificate_data.prev_disease, medical_certificate_data.prev_cert_date)
            for field, value in medical_certificate_data:
                if field != 'prev_disease' and field != 'prev_cert_date':
                    setattr(medical_certificate, field, value)
            self.session.commit()
            return medical_certificate
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_medical_certificate(self, user: User, medical_certificate_pk: MedicalCertificatePK):
        if check_user_access_to_medcard(user=user, medcard_num=medical_certificate_pk.medcard_num):
            medical_certificate = self._get_by_pk(medical_certificate_pk.medcard_num, medical_certificate_pk.disease, medical_certificate_pk.cert_date)
            self.session.delete(medical_certificate)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
