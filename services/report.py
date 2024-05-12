from datetime import date
from fastapi import Depends
from sqlalchemy import desc, extract
from sqlalchemy.orm import Session

from database import get_session

from models.reports.tub_diagnostic import TubDiagnostic
from models.reports.annual import AnnualReport, AgeType
from models.user import User
from models.vaccination import VacReport
from tables import (Allergy,
                    Child,
                    Deworming,
                    MantouxTest,
                    MedicalCertificate,
                    MedicalExamination,
                    Screening,
                    Vaccination)


class ReportService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_children_by_mantoux_test_result(self, mantoux_test_result: str, start_date: date, end_date: date) -> list[Child]:
        return (
            self.session
                .query(Child)
                .join(MantouxTest, Child.medcard_num == MantouxTest.medcard_num)
                .filter(MantouxTest.result == mantoux_test_result)
                .filter(MantouxTest.check_date.between(start_date, end_date))
                .all()
        )
    
    def get_children_by_deworming_result(self, deworming_result: str, start_date: date, end_date: date) -> list[Child]:
        return (
            self.session
                .query(Child)
                .join(Deworming, Child.medcard_num == Deworming.medcard_num)
                .filter(Deworming.result == deworming_result)
                .filter(Deworming.deworming_date.between(start_date, end_date))
                .all()
        )

    def get_children_by_vaccine(self, vac: VacReport) -> list[Child]:
        return (
            self.session
            .query(Child)
            .join(Vaccination, Child.medcard_num == Vaccination.medcard_num)
            .filter(Vaccination.vac_name_id == vac.vac_name_id)
            .filter(Vaccination.vac_type == vac.vac_type)
            .distinct()
            .all()
        )
    
    def get_annual_report_by_age_type(self, age_type: AgeType, year: int):
        report_date = date(year, 12, 31)
        ### AgeType.FIRST
        min_age = 0
        max_age = 3
        max_diseases_for_year = 5
        if age_type == AgeType.SECOND:
            min_age = 4
            max_age = 5
            max_diseases_for_year = 4
        elif age_type == AgeType.THIRD:
            min_age = 6
            max_age = 9
            max_diseases_for_year = 3
        
        report = AnnualReport(year=year, age_type=age_type)

        children = (
            self.session
            .query(Child)
            .filter(extract('year', report_date) - extract('year', Child.birthday) >= min_age)
            .filter(extract('year', report_date) - extract('year', Child.birthday) <= max_age)
            .order_by(Child.surname)
            .all()
        )
        
        if not children:
            return report

        for child in children:
            ### Diseases
            medical_certificates = (
                self.session
                .query(MedicalCertificate)
                .filter(MedicalCertificate.medcard_num == child.medcard_num)
                .filter(extract('year', report_date) == extract('year', MedicalCertificate.start_date))
                .all()
            )

            disease_count = len(medical_certificates)
            if disease_count > max_diseases_for_year: 
                report.frequently_abs += 1
                report.frequently_list.append(child)
            elif not disease_count:
                report.health_indx_abs += 1
                report.health_indx_list.append(child)
            
            report.diseases_count_abs += disease_count

            for medical_certificate in medical_certificates:
                if medical_certificate.start_date and medical_certificate.end_date:
                    report.missed_days_abs = (medical_certificate.end_date - medical_certificate.start_date).days
            
            ### Health groups
            medical_examination = (
                self.session
                .query(MedicalExamination)
                .filter(MedicalExamination.medcard_num == child.medcard_num)
                .filter(extract('year', report_date) <= extract('year', MedicalExamination.examination_date))
                .order_by(desc(MedicalExamination.examination_date))
                .first()
            )

            if medical_examination:
                if medical_examination.health_group == 'I':
                    report.first_health_group += 1
                    report.first_health_group_list.append(child)
                elif medical_examination.health_group == 'II':
                    report.second_health_group += 1
                    report.second_health_group_list.append(child)
                elif medical_examination.health_group == 'III':
                    report.third_health_group += 1
                    report.third_health_group_list.append(child)
            
            ### Tub positive
            isPositiveMantouxTest = (
                self.session
                .query(MantouxTest)
                .filter(MantouxTest.medcard_num == child.medcard_num)
                .filter(MantouxTest.result == 'Положительно')
                .filter(extract('year', report_date) == extract('year', MantouxTest.check_date))
                .first()
            )

            if isPositiveMantouxTest:
                report.tub_positive += 1
                report.tub_positive_list.append(child)
            
            ### Disorders
            screening = (
                self.session
                .query(Screening)
                .filter(Screening.medcard_num == child.medcard_num)
                .filter(extract('year', report_date) == extract('year', Screening.examination_date))
                .order_by(desc(Screening.examination_date))
                .first()
            )

            if screening:
                if screening.speech_defects:
                    report.speech_defects += 1
                    report.speech_defects_list.append(child)
                if screening.carriage == 'Незначительные отклонения':
                    report.poor_posture += 1
                    report.poor_posture_list.append(child)
                if screening.carriage == 'Значительные отклонения':
                    report.scoliosis += 1
                    report.scoliosis_list.append(child)
                if screening.physical_fitness == 'Снижена':
                    report.physical_development_disorders += 1
                    report.physical_development_disorders_list.append(child)
                if screening.neurotic_disorders:
                    report.neurotic_disorders += 1
                    report.neurotic_disorders_list.append(child)
                if screening.thinking_and_speech_disorders:
                    report.thinking_and_speech_disorders += 1
                    report.thinking_and_speech_disorders_list.append(child)
                if screening.motor_development_disorders:
                    report.motor_development_disorders += 1
                    report.motor_development_disorders_list.append(child)
                if screening.attention_and_memory_disorders:
                    report.attention_and_memory_disorders += 1
                    report.attention_and_memory_disorders_list.append(child)
                if screening.social_contacts_disorders:
                    report.social_contacts_disorders += 1
                    report.social_contacts_disorders_list.append(child)

            ### Allergyes
            allergy = (
                self.session
                .query(Allergy)
                .filter(Allergy.medcard_num == child.medcard_num)
                .filter(Allergy.diagnosis_date <= report_date)
                .first()
            )
            if allergy:
                report.allergyes += 1
                report.allergyes_list.append(child)

            ### END FOR

        ### Calc
        report.children_count = len(children)
        report.frequently_per = round(report.frequently_abs / report.children_count * 100, 2)
        report.health_indx_per = round(report.health_indx_abs / report.children_count * 100, 2)
        report.diseases_count_on_thousand = round(report.diseases_count_abs / report.children_count * 1000, 2)
        report.missed_days_on_one = round(report.missed_days_abs / report.children_count)

        return report
