from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session

from database import get_session

from models.catalogs.clinic import ClinicUpdate, ClinicCreate, ClinicPK

from models.user import User
from tables import Clinic, Child


class ClinicService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, id: int) -> Clinic:
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
        return self._get(id)
    
    def get_clinic_by_name(self, name: str):
        clinic = (
            self.session
            .query(Clinic)
            .filter_by(name=name)
            .first()
        )
        return clinic

    def add_new_clinic(self, clinic_data: ClinicCreate):
        clinic = Clinic(**clinic_data.dict())
        try:
            self.session.add(clinic)
            self.session.commit()
            return clinic
        except IntegrityError as e:
            error_message = str(e.orig)
            if "UNIQUE constraint failed" in error_message:
                error_message = "Данное имя поликлиники уже существует"
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_message
            )
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка в работе базы данных при добавлении поликлиники"
            )

    def update_clinic(self, clinic_data: ClinicUpdate):
        clinic = self._get(clinic_data.id)
        for field, value in clinic_data:
            setattr(clinic, field, value)
        
        try:
            self.session.commit()
            return clinic
        except IntegrityError as e:
            error_message = str(e.orig)
            if "UNIQUE constraint failed" in error_message:
                error_message = "Данное имя поликлиники уже существует"
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_message
            )
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка в работе базы данных при обновлении поликлиники"
            )

    def delete_clinic(self, clinic_pk: ClinicPK):
        if self.session.query(Child).filter_by(clinic_id=clinic_pk.id).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Невозможно удалить поликлинику, так как есть дети, записанные в эту поликлинику"
            )
        clinic = self._get(clinic_pk.id)
        try:
            self.session.delete(clinic)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка в работе базы данных при удалении поликлиники"
            )
