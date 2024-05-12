from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session
from services.user import check_user_access_to_medcard

from models.visit_specialist_control import VisitSpecialistControlUpdate, VisitSpecialistControlCreate, VisitSpecialistControlPK, VisitSpecialistControlMain
from models.user import User
from tables import VisitSpecialistControl


class VisitSpecialistControlService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, medcard_num: int, start_dispanser_date: date, assigned_date: date) -> VisitSpecialistControl:
        visit_specialist_control = (
            self.session
            .query(VisitSpecialistControl)
            .filter_by(medcard_num=medcard_num, start_dispanser_date=start_dispanser_date, assigned_date=assigned_date)
            .first()
        )

        if not visit_specialist_control:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Visit Specialist Control is not found'
            )
        return visit_specialist_control

    def get_visit_specialist_controls_by_medcard_num(self, medcard_num: int) -> list[VisitSpecialistControl]:
        visit_specialist_controls = (
            self.session.query(VisitSpecialistControl)
            .filter_by(medcard_num=medcard_num)
            .order_by(VisitSpecialistControl.start_dispanser_date, VisitSpecialistControl.assigned_date)
            .all()
        )
        return visit_specialist_controls

    def get_visit_specialist_control_by_pk(self, visit_specialist_control_pk: VisitSpecialistControlPK):
        visit_specialist_control = self._get_by_pk(
                visit_specialist_control_pk.medcard_num, visit_specialist_control_pk.start_dispanser_date, visit_specialist_control_pk.assigned_date)
        return visit_specialist_control

    def add_new_visit_specialist_control(self, visit_specialist_control_data: VisitSpecialistControlCreate):
        visit_specialist_control = VisitSpecialistControl(
            **visit_specialist_control_data.dict())
        self.session.add(visit_specialist_control)
        self.session.commit()
        return visit_specialist_control

    def update_visit_specialist_control(self, visit_specialist_control_data: VisitSpecialistControlUpdate):
        visit_specialist_control = self._get_by_pk(
            visit_specialist_control_data.medcard_num, visit_specialist_control_data.start_dispanser_date, visit_specialist_control_data.prev_assigned_date)
        for field, value in visit_specialist_control_data:
            if not field in ['prev_assigned_date']:
                setattr(visit_specialist_control, field, value)
        self.session.commit()
        return visit_specialist_control

    def delete_visit_specialist_control(self, visit_specialist_control_pk: VisitSpecialistControlPK):
        visit_specialist_control = self._get_by_pk(
            visit_specialist_control_pk.medcard_num, visit_specialist_control_pk.start_dispanser_date, visit_specialist_control_pk.assigned_date)
        self.session.delete(visit_specialist_control)
        self.session.commit()

    def get_visit_specialist_controls_by_dispensary(self, visit_specialist_control: VisitSpecialistControlMain) -> list[VisitSpecialistControl]:
        visit_specialist_controls = (
            self.session
            .query(VisitSpecialistControl)
            .filter_by(medcard_num=visit_specialist_control.medcard_num, start_dispanser_date=visit_specialist_control.start_dispanser_date)
            .order_by(VisitSpecialistControl.assigned_date)
            .all()
        )
        return visit_specialist_controls
