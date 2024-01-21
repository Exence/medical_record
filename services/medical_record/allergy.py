from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.allergy import AllergyUpdate, AllergyCreate, AllergyPK
from models.user import User
from tables import Allergy


class AllergyService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, allergen: str) -> Allergy:
        allergy = (
            self.session
            .query(Allergy)
            .filter_by(medcard_num=medcard_num, allergen=allergen)
            .first()
        )

        if not allergy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Allergy is not found'
            )
        return allergy

    def get_allergyes_by_medcard_num(self, user: User, medcard_num: int) -> list[Allergy]:
        if check_user_access_to_medcard(user=user, medcard_num=medcard_num):
            query = (
                self.session.query(Allergy)
                .filter_by(medcard_num=medcard_num)
                .order_by(Allergy.start_age)
            )
            allergyes = query.all()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return allergyes

    def get_allergy_by_pk(self, user: User, allergy_pk: AllergyPK):
        if check_user_access_to_medcard(user=user, medcard_num=allergy_pk.medcard_num):
            allergy = self._get_by_pk(
                allergy_pk.medcard_num, allergy_pk.allergen)
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return allergy

    def add_new_allergy(self, user: User, allergy_data: AllergyCreate):
        if check_user_access_to_medcard(user=user, medcard_num=allergy_data.medcard_num):
            allergy = Allergy(**allergy_data.dict())
            self.session.add(allergy)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return allergy

    def update_allergy(self, user: User, allergy_data: AllergyUpdate):
        if check_user_access_to_medcard(user=user, medcard_num=allergy_data.medcard_num):
            allergy = self._get_by_pk(
                allergy_data.medcard_num, allergy_data.prev_allergen)
            for field, value in allergy_data:
                if field != 'prev_allergen':
                    setattr(allergy, field, value)
            self.session.commit()
            return allergy
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_allergy(self, user: User, allergy_pk: AllergyPK):
        if check_user_access_to_medcard(user=user, medcard_num=allergy_pk.medcard_num):
            allergy = self._get_by_pk(
                allergy_pk.medcard_num, allergy_pk.allergen)
            self.session.delete(allergy)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
