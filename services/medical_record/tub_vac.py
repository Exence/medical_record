from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.tub_vac import TuberculosisVaccinationUpdate, TuberculosisVaccinationCreate, TuberculosisVaccinationPK
from models.user import User
from tables import TuberculosisVaccination

class TuberculosisVaccinationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, vac_date: date) -> TuberculosisVaccination:
        tub_vac = (
            self.session
            .query(TuberculosisVaccination)
            .filter_by(medcard_num=medcard_num,vac_date=vac_date)
            .first()
        )

        if not tub_vac:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='TuberculosisVaccination is not found'
            )
        return tub_vac

    def get_tub_vacs_by_medcard_num(self, user: User, medcard_num: int) -> list[TuberculosisVaccination]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(TuberculosisVaccination)
                .filter_by(medcard_num=medcard_num)
                .order_by(TuberculosisVaccination.vac_date)
            )
            tub_vacs = query.all()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return tub_vacs
    
    def get_tub_vac_by_pk(self, user: User, tub_vac_pk: TuberculosisVaccinationPK):
        if check_user_access_to_medcard(user=user, medcard_num=tub_vac_pk.medcard_num):
            tub_vac = self._get_by_pk(tub_vac_pk.medcard_num, tub_vac_pk.vac_date)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return tub_vac

    def add_new_tub_vac(self, user: User, tub_vac_data: TuberculosisVaccinationCreate):
        if check_user_access_to_medcard(user=user, medcard_num=tub_vac_data.medcard_num):
            tub_vac = TuberculosisVaccination(**tub_vac_data.dict())
            self.session.add(tub_vac)
            self.session.commit()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return tub_vac

    def update_tub_vac(self, user: User, tub_vac_data: TuberculosisVaccinationUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=tub_vac_data.medcard_num):
            tub_vac = self._get_by_pk(tub_vac_data.medcard_num, tub_vac_data.prev_vac_date)
            for field, value in tub_vac_data:
                if field != 'prev_vac_date':
                    setattr(tub_vac, field, value)
            self.session.commit()
            return tub_vac
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_tub_vac(self, user: User, tub_vac_pk: TuberculosisVaccinationPK):
        if check_user_access_to_medcard(user=user, medcard_num=tub_vac_pk.medcard_num):
            tub_vac = self._get_by_pk(tub_vac_pk.medcard_num, tub_vac_pk.vac_date)
            self.session.delete(tub_vac)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
