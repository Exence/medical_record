from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.dispensary import DispensaryUpdate, DispensaryCreate, DispensaryPK
from models.user import User
from tables import Dispensary


class DispensaryService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_id(self, id: int) -> Dispensary:
        dispensary = (
            self.session
            .query(Dispensary)
            .filter_by(id=id)
            .first()
        )

        if not dispensary:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Dispensary is not found'
            )
        return dispensary

    def get_dispensaryes_by_medcard_num(self, medcard_num: int) -> list[Dispensary]:
        dispensaryes = (
            self.session.query(Dispensary)
            .filter_by(medcard_num=medcard_num)
            .order_by(Dispensary.start_date)
            .all()
        )
        return dispensaryes

    def get_dispensary_by_id(self, id: int):
        dispensary = self._get_by_id(id=id)
        return dispensary

    def add_new_dispensary(self, dispensary_data: DispensaryCreate):
        dispensary = Dispensary(**dispensary_data.dict())
        self.session.add(dispensary)
        self.session.commit()
        self.session.refresh(dispensary)
        return dispensary

    def update_dispensary(self, dispensary_data: DispensaryUpdate):
        dispensary = self._get_by_id(id=dispensary_data.id)
        for field, value in dispensary_data:
            setattr(dispensary, field, value)
        self.session.commit()
        return dispensary

    def delete_dispensary(self, id: int):
        dispensary = self._get_by_id(id=id)
        self.session.delete(dispensary)
        self.session.commit()
