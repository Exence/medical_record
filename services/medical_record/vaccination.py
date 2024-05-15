from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.medical_record.vaccination import VaccinationUpdate, VaccinationCreate, VaccinationPK, VaccinationView
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

    def get_vaccinations_by_medcard_num(self, medcard_num: int) -> list[Vaccination]:
        vaccinations = (
            self.session.query(Vaccination)
            .filter_by(medcard_num=medcard_num)
            .order_by(Vaccination.vac_date)
            .all()
        )
        return vaccinations

    def get_vaccination_by_pk(self, vaccination_pk: VaccinationPK):
        vaccination = self._get_by_pk(
                vaccination_pk.medcard_num, vaccination_pk.vac_name_id, vaccination_pk.vac_type)
        return vaccination

    def add_new_vaccination(self, vaccination_data: VaccinationCreate):
        vaccination = Vaccination(**vaccination_data.dict())
        self.session.add(vaccination)
        self.session.commit()
        return vaccination

    def update_vaccination(self, vaccination_data: VaccinationUpdate):
        vaccination = self._get_by_pk(
            vaccination_data.medcard_num, vaccination_data.prev_vac_name_id, vaccination_data.prev_vac_type)
        for field, value in vaccination_data:
            if not field in ['prev_vac_name_id', 'prev_vac_type']:
                setattr(vaccination, field, value)
        self.session.commit()
        return vaccination

    def delete_vaccination(self, vaccination_pk: VaccinationPK):
        vaccination = self._get_by_pk(
            vaccination_pk.medcard_num, vaccination_pk.vac_name_id, vaccination_pk.vac_type)
        self.session.delete(vaccination)
        self.session.commit()

    def get_prof_vaccination_by_pk(self, prof_vaccination_pk: VaccinationPK) -> ProfVaccination:
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
        return prof_vaccination

    def get_prof_vaccinations_by_medcard_num(self, medcard_num: int) -> list[ProfVaccination]:
        prof_vaccination =  (
            self.session
            .query(ProfVaccination)
            .filter_by(medcard_num=medcard_num)
            .all()
        )
        return prof_vaccination
            

    def get_epid_vaccinations_by_medcard_num(self, medcard_num: int) -> list[EpidVaccination]:
        epid_vaccinations = (
            self.session
            .query(EpidVaccination)
            .filter_by(medcard_num=medcard_num)
            .all()
        )
        return epid_vaccinations

    def get_epid_vaccination_by_pk(self, epid_vaccination_pk: VaccinationPK) -> EpidVaccination:
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
