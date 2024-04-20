from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.vaccination import VaccinationUpdate, VaccinationCreate, VaccinationPK, VaccinationView
from models.user import User
from tables import Vaccination, ProfVaccination, EpidVaccination, VacName


class VaccinationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, vac_name_id: int, vac_type: str) -> Vaccination:
        vaccination = (
            self.session
            .query(Vaccination)
            .filter_by(medcard_num=medcard_num, vac_name_id=vac_name_id, vac_type=vac_type)
            .first()
        )

        if not vaccination:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Vaccination is not found'
            )
        return vaccination

    def get_vaccinations_by_medcard_num(self, user: User, medcard_num: int) -> list[Vaccination]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(Vaccination)
                .join(VacName, Vaccination.vac_name_id == VacName.id)
                .filter_by(medcard_num=medcard_num)
                .order_by(VacName.name)
                .order_by(Vaccination.vac_date)
            )
            vaccinations = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return vaccinations

    def get_vaccination_by_pk(self, user: User, vaccination_pk: VaccinationPK):
        if check_user_access_to_medcard(user=user, medcard_num=vaccination_pk.medcard_num):
            vaccination = self._get_by_pk(
                vaccination_pk.medcard_num, vaccination_pk.vac_name_id, vaccination_pk.vac_type)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return vaccination

    def add_new_vaccination(self, user: User, vaccination_data: VaccinationCreate):
        if check_user_access_to_medcard(user=user, medcard_num=vaccination_data.medcard_num):
            vaccination = Vaccination(**vaccination_data.dict())
            self.session.add(vaccination)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return vaccination

    def update_vaccination(self, user: User, vaccination_data: VaccinationUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=vaccination_data.medcard_num):
            vaccination = self._get_by_pk(
                vaccination_data.medcard_num, vaccination_data.prev_vac_name_id, vaccination_data.prev_vac_type)
            for field, value in vaccination_data:
                if not field in ['prev_vac_name_id', 'prev_vac_type']:
                    setattr(vaccination, field, value)
            self.session.commit()
            return vaccination
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_vaccination(self, user: User, vaccination_pk: VaccinationPK):
        if check_user_access_to_medcard(user=user, medcard_num=vaccination_pk.medcard_num):
            vaccination = self._get_by_pk(
                vaccination_pk.medcard_num, vaccination_pk.vac_name_id, vaccination_pk.vac_type)
            self.session.delete(vaccination)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def get_prof_vaccination_by_pk(self, user: User, prof_vaccination_pk: VaccinationPK) -> ProfVaccination:
        if check_user_access_to_medcard(user=user, medcard_num=prof_vaccination_pk.medcard_num):
            prof_vaccination = (
                self.session
                .query(ProfVaccination)
                .filter_by(medcard_num=prof_vaccination_pk.medcard_num, vac_name_id=prof_vaccination_pk.vac_name_id, vac_type=prof_vaccination_pk.vac_type)
                .first()
            )

        if not prof_vaccination:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Prof vaccination is not found'
            )
        print(prof_vaccination)
        return prof_vaccination

    def get_prof_vaccinations_by_medcard_num(self, user: User, medcard_num: int) -> list[ProfVaccination]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            return (
                self.session
                .query(ProfVaccination)
                .filter_by(medcard_num=medcard_num)
                .all()
            )

    def get_epid_vaccinations_by_medcard_num(self, user: User, medcard_num: int) -> list[EpidVaccination]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            return (
                self.session
                .query(EpidVaccination)
                .filter_by(medcard_num=medcard_num)
                .all()
            )

    def get_epid_vaccination_by_pk(self, user: User, epid_vaccination_pk: VaccinationPK) -> EpidVaccination:
        if check_user_access_to_medcard(user=user, medcard_num=epid_vaccination_pk.medcard_num):
            epid_vaccination = (
                self.session
                .query(EpidVaccination)
                .filter_by(medcard_num=epid_vaccination_pk.medcard_num, vac_name_id=epid_vaccination_pk.vac_name_id, vac_type=epid_vaccination_pk.vac_type)
                .first()
            )

        if not epid_vaccination:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Epid vaccination is not found'
            )
        return epid_vaccination
