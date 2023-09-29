from typing import Any

from database import (
      execute_read_query_first,
      )

from models.allergyes import Allergy
from models.child import (
    Child,
    CreateChildForm,
    ChildToShow,
    )
from models.deworming import Deworming
from models.dispensary import Dispensary
from models.extra_classes import ExtraClass
from models.gg_injection import GammaGlobulinInjection
from models.hospitalization import Hospitalization
from models.mantoux_test import MantouxTest
from models.medical_certificate import MedicalCertificate
from models.medical_examination import MedicalExamination
from models.ongoing_medical_supervision import OngoingMedicalSupervision
from models.oral_sanation import OralSanation
from models.parent import (
        ParentCreate,
)
from models.past_illness import PastIllness
from models.prevaccination_checkup import (
        PrevaccinationCheckup,
        PrevaccinationCheckupView,
)
from models.screening import Screening
from models.spa_treatment import SpaTreatment
from models.tub_vac import TuberculosisVaccination
from models.user import (
    User,
)
from models.vac_name import VacName
from models.vaccination import Vaccination
from models.visit_specialist_control import VisitSpecialistControl

from services.kindergarten import get_kindergarten_name_by_num


class SerializationService():

        @classmethod
        def serialization_user(cls, connection: Any, user_data: tuple) -> User:
                cursor = connection.cursor()
                kindergarten_name = get_kindergarten_name_by_num(cursor, user_data[6])
                cursor.close()

                return User (
                        login = user_data[0],
                        surname = user_data[1],
                        name = user_data[2],
                        patronymic = user_data[3],
                        password_hash = user_data[4],
                        access_level = user_data[5],
                        kindergarten_num = user_data[6],
                        kindergarten_name = kindergarten_name
                )

        @classmethod
        def serialization_parent_to_create(cls, parent_data: tuple) -> ParentCreate:
                return ParentCreate(
                        surname=parent_data[0],
                        name=parent_data[1],
                        patronymic=parent_data[2],
                        birthday_year=parent_data[3],
                        education=parent_data[4],
                        phone_num=parent_data[5])

        @classmethod
        def serialization_child(cls, child_data: tuple) -> Child:
                return Child(
                        medcard_num=child_data[0],
                        surname=child_data[1],
                        name=child_data[2],
                        patronymic=child_data[3],
                        kindergarten_num=child_data[4],
                        birthday=child_data[5],
                        sex=child_data[6],
                        group_num=child_data[7],
                        address=child_data[8],
                        clinic=child_data[9],
                        edu_type=child_data[10],
                        entering_date=child_data[11],
                        father_id=child_data[12],
                        mother_id=child_data[13],
                        family_characteristics=child_data[14],
                        family_microclimate=child_data[15],
                        rest_and_class_opportunities=child_data[16],
                        case_history=child_data[17]
                )

        @classmethod
        def serialization_child_to_create(cls, form_data: CreateChildForm, father_id: int, mother_id: int, kindergarten_num: int) -> tuple:
                return [(form_data.surname,
                        form_data.name,
                        form_data.patronymic,
                        kindergarten_num,
                        form_data.birthday,
                        form_data.sex[0],
                        form_data.group_num,
                        form_data.address,
                        form_data.clinic,
                        'ДДУ',
                        form_data.entering_date,
                        father_id,
                        mother_id,
                        form_data.family_characteristics,
                        form_data.family_microclimate,
                        form_data.rest_and_class_opportunities,
                        form_data.case_history,
                )]

        @classmethod
        def serialization_child_to_show(cls, child_data: tuple) -> ChildToShow:
                return ChildToShow(
                        medcard_num = child_data[0],
                        surname = child_data[1],
                        name = child_data[2],
                        patronymic = child_data[3],
                        kindergarten_name = child_data[4],
                        birthday = child_data[5],
                        group_num = child_data[6],
                        father_surname = child_data[7],
                        father_name = child_data[8],
                        father_patronymic = child_data[9],
                        father_phone_num = child_data[10],
                        mother_surname = child_data[11],
                        mother_name = child_data[12],
                        mother_patronymic = child_data[13],
                        mother_phone_num = child_data[14]) 

        @classmethod
        def serialization_allergy(cls, allergy_data: tuple) -> Allergy:
                return Allergy (
                        medcard_num=allergy_data[0],
                        allergen=allergy_data[1],
                        allergy_type=allergy_data[2],
                        start_age=allergy_data[3],
                        reaction_type=allergy_data[4],
                        diagnosis_date=allergy_data[5],
                        note=allergy_data[6]
                )

        @classmethod
        def serialization_allergy_to_create(cls, medcard_num: int, allergy: dict):
                return [(
                        medcard_num, 
                        allergy["allergen"],
                        allergy["allergy_type"],
                        allergy["start_age"],
                        allergy["reaction_type"],
                        allergy["diagnosis_date"],
                        allergy["note"],
                        
                )]

        @classmethod
        def serialization_extra_class(cls, extra_class_data: tuple) -> ExtraClass:
                return ExtraClass(
                        medcard_num=extra_class_data[0],
                        classes_type=extra_class_data[1],
                        age=extra_class_data[2],
                        hours_on_week=extra_class_data[3]
                )

        @classmethod
        def serialization_past_illness(cls, past_illness_data: tuple) -> PastIllness:
                return PastIllness(
                        medcard_num=past_illness_data[0],
                        start_date=past_illness_data[1],
                        end_date=past_illness_data[2],
                        diagnosis=past_illness_data[3]
                )

        @classmethod
        def serialization_hospitalization(cls, hospitalization_data: tuple) -> Hospitalization:
                return Hospitalization(
                        medcard_num=hospitalization_data[0],
                        start_date=hospitalization_data[1],
                        end_date=hospitalization_data[2],
                        diagnosis=hospitalization_data[3],
                        founding=hospitalization_data[4]
                )

        @classmethod
        def serialization_spa_treatment(cls, spa_treatment_data: tuple) -> SpaTreatment:
                return SpaTreatment(
                        medcard_num=spa_treatment_data[0],
                        start_date=spa_treatment_data[1],
                        end_date=spa_treatment_data[2],
                        diagnosis=spa_treatment_data[3],
                        founding_specialization=spa_treatment_data[4],
                        climatic_zone=spa_treatment_data[5]
                )

        @classmethod
        def serialization_medical_certificate(cls, medical_certificate_data: tuple):
                return MedicalCertificate(
                        medcard_num=medical_certificate_data[0],
                        disease=medical_certificate_data[1],
                        cert_date=medical_certificate_data[2],
                        start_date=medical_certificate_data[3],
                        end_date=medical_certificate_data[4],
                        infection_contact=medical_certificate_data[5],
                        sport_exemption_date=medical_certificate_data[6],
                        vac_exemption_date=medical_certificate_data[7],
                        doctor=medical_certificate_data[8]
                )

        @classmethod
        def serialization_dispensary(cls, dispensary_data: tuple) -> Dispensary:
                return Dispensary(
                        medcard_num=dispensary_data[0],
                        start_date=dispensary_data[1],
                        diagnosis=dispensary_data[2],
                        specialist=dispensary_data[3],
                        end_date=dispensary_data[4],
                        end_reason=dispensary_data[5]
                )

        @classmethod
        def serialization_visit_specialist_control(cls, visit_data: tuple) -> VisitSpecialistControl:
                return VisitSpecialistControl(
                        medcard_num=visit_data[0],
                        start_dispanser_date=visit_data[1],
                        assigned_date=visit_data[2],
                        fact_date=visit_data[3]
                )

        @classmethod
        def serialization_deworming(cls, deworming_data: tuple) -> Deworming:
                return Deworming(
                        medcard_num=deworming_data[0],
                        deworming_date=deworming_data[1],
                        result=deworming_data[2]                        
                )

        @classmethod
        def serialization_oral_sanation(cls, oral_sanation_data: tuple) -> OralSanation:
                return OralSanation(
                        medcard_num=oral_sanation_data[0],
                        sanation_date=oral_sanation_data[1],
                        dental_result=oral_sanation_data[2],
                        sanation_result=oral_sanation_data[3]
                )

        @classmethod
        def serialization_vac_name(cls, vac_name_data: tuple) -> VacName:
                return VacName(
                        id=vac_name_data[0],
                        name=vac_name_data[1],
                        vac_type=vac_name_data[2]
                )

        @classmethod
        def serialization_prevaccination_checkup(cls, prevaccination_checkup_data: tuple) -> PrevaccinationCheckupView:
                return PrevaccinationCheckupView(
                        medcard_num=prevaccination_checkup_data[0],
                        examination_date=prevaccination_checkup_data[1],
                        age=prevaccination_checkup_data[2],
                        diagnosis=prevaccination_checkup_data[3],
                        report=prevaccination_checkup_data[4],
                        vac_name=prevaccination_checkup_data[5],
                        no_vac_date=prevaccination_checkup_data[6],
                        doctor=prevaccination_checkup_data[7]
                )

        @classmethod
        def serialization_vaccination(cls, vaccination_data: tuple) -> Vaccination:
                return Vaccination(
                        medcard_num = vaccination_data[0],
	                vac_name_id = vaccination_data[1],
	                vac_name = vaccination_data[2],
	                vac_type = vaccination_data[3],
	                vac_date = vaccination_data[4],
	                serial = vaccination_data[5],
	                dose = vaccination_data[6],
	                introduction_method = vaccination_data[7],
	                reaction = vaccination_data[8],
	                doctor = vaccination_data[9]
                )

        @classmethod
        def serialization_gg_injection(cls, gg_injection_data: tuple) -> GammaGlobulinInjection:
                return GammaGlobulinInjection(
                        medcard_num=gg_injection_data[0],
                        vac_date=gg_injection_data[1],
                        reason=gg_injection_data[2],
                        serial=gg_injection_data[3],
                        dose=gg_injection_data[4],
                        reaction=gg_injection_data[5],
                        doctor=gg_injection_data[6]
                )

        @classmethod
        def serialization_mantoux_test(cls, mantoux_test_data: tuple) ->  MantouxTest:
                return MantouxTest(
                        medcard_num=mantoux_test_data[0],
                        check_date=mantoux_test_data[1],
                        result=mantoux_test_data[2]
                )

        @classmethod
        def serialization_tub_vac(cls, tub_vac_data: tuple) -> TuberculosisVaccination:
                return TuberculosisVaccination(
                        medcard_num=tub_vac_data[0],
                        vac_date=tub_vac_data[1],
                        serial=tub_vac_data[2],
                        dose=tub_vac_data[3],
                        doctor=tub_vac_data[4]
                )

        @classmethod
        def serialization_medical_examination(cls, medical_examination_data: tuple) -> MedicalExamination:
                return MedicalExamination(
                        medcard_num=medical_examination_data[0],
                        period=medical_examination_data[1],
                        examination_date=medical_examination_data[2],
                        age=medical_examination_data[3],
                        height=medical_examination_data[4],
                        weight=medical_examination_data[5],
                        complaints=medical_examination_data[6],
                        pediatrician=medical_examination_data[7],
                        orthopaedist=medical_examination_data[8],
                        ophthalmologist=medical_examination_data[9],
                        otolaryngologist=medical_examination_data[10],
                        dermatologist=medical_examination_data[11],
                        neurologist=medical_examination_data[12],
                        speech_therapist=medical_examination_data[13],
                        denta_surgeon=medical_examination_data[14],
                        psychologist=medical_examination_data[15],
                        other_doctors=medical_examination_data[16],
                        blood_test=medical_examination_data[17],
                        urine_analysis=medical_examination_data[18],
                        feces_analysis=medical_examination_data[19],
                        general_diagnosis=medical_examination_data[20],
                        physical_development=medical_examination_data[21],
                        mental_development=medical_examination_data[22],
                        health_group=medical_examination_data[23],
                        sport_group=medical_examination_data[24],
                        med_and_ped_conclusion=medical_examination_data[25],
                        recommendations=medical_examination_data[26]
                )

        @classmethod
        def serialization_ongoing_medical_supervision(cls, oms_data: tuple) -> OngoingMedicalSupervision:
                return OngoingMedicalSupervision(
                        medcard_num=oms_data[0],
                        examination_date=oms_data[1],
                        examination_data=oms_data[2],
                        diagnosis=oms_data[3],
                        prescription=oms_data[4],
                        doctor=oms_data[5]
                )

        @classmethod
        def serialization_screening(cls, screening_data: tuple) -> Screening:
                return Screening(
                        medcard_num = screening_data[0],
                        age = screening_data[1],
                        questionnaire_test = screening_data[2],
                        height = screening_data[3],
                        weight = screening_data[4],
                        physical_development = screening_data[5],
                        blood_pressures = screening_data[6],
                        carriage = screening_data[7],
                        foot_condition = screening_data[8],
                        sight_od = screening_data[9],
                        sight_os = screening_data[10],
                        visual_acuity = screening_data[11],
                        malinovsky_test = screening_data[12],
                        binocular_vision = screening_data[13],
                        hearing_acuteness = screening_data[14],
                        dynammetry_left = screening_data[15],
                        dynammetry_right = screening_data[16],
                        physical_fitness = screening_data[17],
                        protein_in_urine = screening_data[18],
                        glucose_in_urine = screening_data[19],
                        biological_age = screening_data[20],
                        speech_defects = screening_data[21],
                        kern_test = screening_data[22],
                        neurotic_disorders = screening_data[23],
                        thinking_and_speech_disorders = screening_data[24],
                        motor_development_disorders = screening_data[25],
                        attention_and_memory_disorders = screening_data[26],
                        social_contacts_disorders = screening_data[27],
                        diseases_for_year = screening_data[28]
                )
