from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session

from services.user import check_user_access_to_medcard

from models.past_illness import PastIllnessUpdate, PastIllnessCreate, PastIllnessPK
from models.user import User
from tables import PastIllness

class PastIllnessService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, start_date: date, diagnosis: str) -> PastIllness:
        past_illness = (
            self.session
            .query(PastIllness)
            .filter_by(medcard_num=medcard_num, start_date=start_date, diagnosis=diagnosis)
            .first()
        )

        if not past_illness:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Past illness is not found'
            )
        return past_illness

    def get_past_illnesses_by_medcard_num(self, user: User, medcard_num: int) -> list[PastIllness]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(PastIllness)
                .filter_by(medcard_num=medcard_num)
                .order_by(PastIllness.start_date)
            )
            past_illnesses = query.all()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return past_illnesses
    
    def get_past_illness_by_pk(self, user: User, past_illness_pk: PastIllnessPK):
        if check_user_access_to_medcard(user=user, medcard_num=past_illness_pk.medcard_num):
            past_illness = self._get_by_pk(medcard_num=past_illness_pk.medcard_num, start_date=past_illness_pk.start_date, diagnosis=past_illness_pk.diagnosis)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return past_illness

    def add_new_past_illness(self, user: User, past_illness_data: PastIllnessCreate):
        if check_user_access_to_medcard(user=user, medcard_num=past_illness_data.medcard_num):
            past_illness = PastIllness(**past_illness_data.dict())
            self.session.add(past_illness)
            self.session.commit()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return past_illness

    def update_past_illness(self, user: User, past_illness_data: PastIllnessUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=past_illness_data.medcard_num):
            past_illness = self._get_by_pk(past_illness_data.medcard_num, past_illness_data.prev_start_date, past_illness_data.prev_diagnosis)
            for field, value in past_illness_data:
                if field != 'prev_start_date' and field != 'prev_diagnosis':
                    setattr(past_illness, field, value)
            self.session.commit()
            return past_illness
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_past_illness(self, user: User, past_illness_pk: PastIllnessPK):
        if check_user_access_to_medcard(user=user, medcard_num=past_illness_pk.medcard_num):
            past_illness = self._get_by_pk(past_illness_pk.medcard_num, past_illness_pk.start_date, past_illness_pk.diagnosis)
            self.session.delete(past_illness)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
