from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.clinic import ClinicUpdate, ClinicCreate, ClinicPK, ClinicDict

from models.user import User
from tables import Clinic


class ClinicService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, id: int) -> Clinic:
        clinic = (
            self.session
            .query(Clinic)
            .filter_by(id=id)
            .first()
        )

        if not clinic:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Clinic is not found'
            )
        return clinic

    def get_all_clinics_as_dict(self) -> dict:
        query = (
            self.session
            .query(Clinic)
            .all()
        )
        clinics = dict()
        for clinic in query:
            clinics[clinic.id] = clinic.name

        return clinics

    def get_clinic_by_id(self, id: int) -> Clinic:
        return self._get_by_pk(id)

    def add_new_clinic(self, user: User, clinic_data: ClinicCreate):
        if user:
            clinic = Clinic(**clinic_data.dict())
            self.session.add(clinic)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return clinic

    def update_clinic(self, user: User, clinic_data: ClinicUpdate):
        if user:
            clinic = self._get_by_pk(clinic_data.id)
            for field, value in clinic_data:
                setattr(clinic, field, value)
            self.session.commit()
            return clinic
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_clinic(self, user: User, clinic_pk: ClinicPK):
        if user:
            clinic = self._get_by_pk(clinic_pk.id)
            self.session.delete(clinic)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
