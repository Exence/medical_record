from fastapi import (
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_session

from services.user import check_user_access_to_medcard

from models.medical_record.extra_class import ExtraClassUpdate, ExtraClassCreate, ExtraClassPK
from models.user import User
from tables import ExtraClass


class ExtraClassService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, medcard_num: int, classes_type: str, age: int) -> ExtraClass:
        extra_class = (
            self.session
            .query(ExtraClass)
            .filter_by(medcard_num=medcard_num, classes_type=classes_type, age=age)
            .first()
        )

        if not extra_class:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Extra class is not found'
            )
        return extra_class

    def get_extra_classes_by_medcard_num(self, medcard_num: int) -> list[ExtraClass]:
        extra_classes = (
            self.session.query(ExtraClass)
            .filter_by(medcard_num=medcard_num)
            .order_by(ExtraClass.classes_type)
            .all()
        )
        return extra_classes

    def get_extra_class_by_pk(self, extra_class_pk: ExtraClassPK):
        extra_class = self._get(extra_class_pk.medcard_num, extra_class_pk.classes_type, extra_class_pk.age)
        return extra_class

    def add_new_extra_class(self, extra_class_data: ExtraClassCreate):
        extra_class = ExtraClass(**extra_class_data.dict())
        self.session.add(extra_class)
        self.session.commit()
        return extra_class

    def update_extra_class(self, extra_class_data: ExtraClassUpdate):
        extra_class = self._get(
            extra_class_data.medcard_num, extra_class_data.prev_classes_type, extra_class_data.prev_age)
        for field, value in extra_class_data:
            if field != 'prev_classes_type' and field != 'prev_age':
                setattr(extra_class, field, value)
        self.session.commit()
        return extra_class

    def delete_extra_class(self, extra_class_pk: ExtraClassPK):
        extra_class = self._get(
            extra_class_pk.medcard_num, extra_class_pk.classes_type, extra_class_pk.age)
        self.session.delete(extra_class)
        self.session.commit()
