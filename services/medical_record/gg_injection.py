from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.gg_injection import GammaGlobulinInjectionUpdate, GammaGlobulinInjectionCreate, GammaGlobulinInjectionPK
from models.user import User
from tables import GammaGlobulinInjection


class GammaGlobulinInjectionService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, vac_date: date) -> GammaGlobulinInjection:
        gg_injection = (
            self.session
            .query(GammaGlobulinInjection)
            .filter_by(medcard_num=medcard_num, vac_date=vac_date)
            .first()
        )

        if not gg_injection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='GammaGlobulinInjection is not found'
            )
        return gg_injection

    def get_gg_injections_by_medcard_num(self, medcard_num: int) -> list[GammaGlobulinInjection]:
        gg_injections = (
            self.session.query(GammaGlobulinInjection)
            .filter_by(medcard_num=medcard_num)
            .order_by(GammaGlobulinInjection.vac_date)
            .all()
        )
        return gg_injections

    def get_gg_injection_by_pk(self, gg_injection_pk: GammaGlobulinInjectionPK):
        gg_injection = self._get_by_pk(gg_injection_pk.medcard_num, gg_injection_pk.vac_date)
        return gg_injection

    def add_new_gg_injection(self, gg_injection_data: GammaGlobulinInjectionCreate):
        gg_injection = GammaGlobulinInjection(**gg_injection_data.dict())
        self.session.add(gg_injection)
        self.session.commit()
        return gg_injection

    def update_gg_injection(self, gg_injection_data: GammaGlobulinInjectionUpdate):
        gg_injection = self._get_by_pk(
            gg_injection_data.medcard_num, gg_injection_data.prev_vac_date)
        for field, value in gg_injection_data:
            if field != 'prev_vac_date':
                setattr(gg_injection, field, value)
        self.session.commit()
        return gg_injection

    def delete_gg_injection(self, gg_injection_pk: GammaGlobulinInjectionPK):
        gg_injection = self._get_by_pk(
            gg_injection_pk.medcard_num, gg_injection_pk.vac_date)
        self.session.delete(gg_injection)
        self.session.commit()
