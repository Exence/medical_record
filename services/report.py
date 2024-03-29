from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_session

from models.child import ChildToShow
from models.tub_diagnostic import TubDiagnostic
from models.user import User
from models.vaccination import VacReport
from tables import Child, MantouxTest, Vaccination


class ReportService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_childrens_by_mantoux_test_result(self, user: User, mantoux_test_result: str, start_date: date, end_date: date) -> list[Child]:
        if not user.access_level in ['admin', 'db_admin']:
            childrens = (
                self.session
                .query(Child)
                .join(MantouxTest, Child.medcard_num == MantouxTest.medcard_num)
                .filter(MantouxTest.result == mantoux_test_result)
                .filter(MantouxTest.check_date.between(start_date, end_date))
                .filter_by(kindergarten_num=user.kindergarten_num)
                .all()
            )
            return childrens
        return (
            self.session
                .query(Child)
                .join(MantouxTest, Child.medcard_num == MantouxTest.medcard_num)
                .filter(MantouxTest.result == mantoux_test_result)
                .filter(MantouxTest.check_date.between(start_date, end_date))
                .all()
        )

    def get_childrens_by_vaccine(self, user: User, vac: VacReport) -> list[Child]:
        if not user.access_level in ['admin', 'db_admin']:
            childrens = (
                self.session
                .query(Child)
                .join(Vaccination, Child.medcard_num == Vaccination.medcard_num)
                .filter(Vaccination.vac_name_id == vac.vac_name_id)
                .filter(Vaccination.vac_type == vac.vac_type)
                .filter_by(kindergarten_num=user.kindergarten_num)
                .distinct()
            )
            return childrens
        return (
            self.session
            .query(Child)
                .join(Vaccination, Child.medcard_num == Vaccination.medcard_num)
                .filter(Vaccination.vac_name_id == vac.vac_name_id)
                .filter(Vaccination.vac_type == vac.vac_type)
                .distinct()
        )
