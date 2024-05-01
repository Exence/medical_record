import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


BaseTable = declarative_base()

class Child(BaseTable):
    __tablename__ = 'childrens'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    kindergarten_num = sa.Column(sa.Integer)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)
    birthday = sa.Column(sa.Date)
    sex = sa.Column(sa.String)
    group_num = sa.Column(sa.Integer)
    address = sa.Column(sa.String)
    clinic_id = sa.Column(sa.Integer, sa.ForeignKey('clinics.id', ondelete='RESTRICT'))
    edu_type = sa.Column(sa.String, default='ДДУ')
    entering_date = sa.Column(sa.Date)
    father_id = sa.Column(sa.Integer, sa.ForeignKey('parents.id', ondelete='SET NULL'), nullable=True)
    mother_id = sa.Column(sa.Integer, sa.ForeignKey('parents.id', ondelete='SET NULL'), nullable=True)
    family_characteristics = sa.Column(sa.String)
    family_microclimate = sa.Column(sa.String)
    rest_and_class_opportunities = sa.Column(sa.String)
    case_history = sa.Column(sa.String, nullable=True)

    father = relationship("Parent", foreign_keys="[Child.father_id]", primaryjoin="Parent.id == Child.father_id")
    mother = relationship("Parent", foreign_keys="[Child.mother_id]", primaryjoin="Parent.id == Child.mother_id")
    clinic = relationship("Clinic", foreign_keys="[Child.clinic_id]", primaryjoin="Clinic.id == Child.clinic_id")


class ChildWithParents(BaseTable):
    __tablename__ = 'childrens_with_parents_view'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    kindergarten_num = sa.Column(sa.Integer)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)
    birthday = sa.Column(sa.Date)
    sex = sa.Column(sa.String)
    group_num = sa.Column(sa.Integer)
    address = sa.Column(sa.String)
    clinic_name = sa.Column(sa.String)
    edu_type = sa.Column(sa.String)
    entering_date = sa.Column(sa.Date)
    father_surname = sa.Column(sa.String)
    father_name = sa.Column(sa.String)
    father_patronymic = sa.Column(sa.String)
    father_birthday_year = sa.Column(sa.Integer)
    father_education = sa.Column(sa.String)
    father_phone_num = sa.Column(sa.BigInteger)
    mother_surname = sa.Column(sa.String)
    mother_name = sa.Column(sa.String)
    mother_patronymic = sa.Column(sa.String)
    mother_birthday_year = sa.Column(sa.Integer)
    mother_education = sa.Column(sa.String)
    mother_phone_num = sa.Column(sa.BigInteger)
    family_characteristics = sa.Column(sa.String)
    family_microclimate = sa.Column(sa.String)
    rest_and_class_opportunities = sa.Column(sa.String)
    case_history = sa.Column(sa.String, nullable=True)


class Allergy(BaseTable):
    __tablename__ = 'allergyes'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    allergen = sa.Column(sa.String, primary_key=True)
    allergy_type = sa.Column(sa.String)
    start_age = sa.Column(sa.Integer)
    reaction_type = sa.Column(sa.String)
    diagnosis_date = sa.Column(sa.Date)
    note = sa.Column(sa.String, nullable=True)


class Clinic(BaseTable):
    __tablename__ = 'clinics'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String) 


class Deworming(BaseTable):
    __tablename__ = 'dewormings'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    deworming_date = sa.Column(sa.Date, primary_key=True)
    result = sa.Column(sa.String)


class Dispensary(BaseTable):
    __tablename__ = 'dispensaryes'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    start_date = sa.Column(sa.Date, primary_key=True)
    diagnosis = sa.Column(sa.String)
    specialist = sa.Column(sa.String)
    end_date = sa.Column(sa.Date, nullable=True)
    end_reason = sa.Column(sa.String, nullable=True)


class ExtraClass(BaseTable):
    __tablename__ = 'extra_classes'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    classes_type = sa.Column(sa.String, primary_key=True)
    age = sa.Column(sa.Integer, primary_key=True)
    hours_on_week = sa.Column(sa.Integer)


class GammaGlobulinInjection(BaseTable):
    __tablename__ = 'gamma_globulin_injections'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    vac_date = sa.Column(sa.Date, primary_key=True)
    reason = sa.Column(sa.String)
    serial = sa.Column(sa.String)
    dose = sa.Column(sa.Numeric(10,2))
    reaction = sa.Column(sa.String)
    doctor = sa.Column(sa.String)


class Hospitalization(BaseTable):
    __tablename__ = 'hospitalizations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    start_date = sa.Column(sa.Date, primary_key=True)
    end_date = sa.Column(sa.Date, nullable=True)
    diagnosis = sa.Column(sa.String)
    founding = sa.Column(sa.String)


class Kindergarten(BaseTable):
    __tablename__ = 'kindergartens'

    number = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class MantouxTest(BaseTable):
    __tablename__ = 'mantoux_tests'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    check_date = sa.Column(sa.Date, primary_key=True)
    result = sa.Column(sa.String)


class MedicalCertificate(BaseTable):
    __tablename__ = 'medical_certificates'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    disease = sa.Column(sa.String, primary_key=True)
    cert_date = sa.Column(sa.Date, primary_key=True)
    start_date = sa.Column(sa.Date)
    end_date = sa.Column(sa.Date)
    infection_contact = sa.Column(sa.Boolean)
    sport_exemption_date = sa.Column(sa.Date, nullable=True)
    vac_exemption_date = sa.Column(sa.Date, nullable=True)
    doctor = sa.Column(sa.String)


class MedicalExamination(BaseTable):
    __tablename__ = 'medical_examinations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    period = sa.Column(sa.String, primary_key=True)
    examination_date = sa.Column(sa.Date)
    age = sa.Column(sa.Integer, nullable=True)
    height = sa.Column(sa.Numeric(5,2))
    weight = sa.Column(sa.Numeric(5,2))
    complaints = sa.Column(sa.String, nullable=True)
    pediatrician = sa.Column(sa.String, nullable=True)
    orthopaedist = sa.Column(sa.String, nullable=True)
    ophthalmologist = sa.Column(sa.String, nullable=True)
    otolaryngologist = sa.Column(sa.String, nullable=True)
    dermatologist = sa.Column(sa.String, nullable=True)
    neurologist = sa.Column(sa.String, nullable=True)
    speech_therapist = sa.Column(sa.String, nullable=True)
    denta_surgeon = sa.Column(sa.String, nullable=True)
    psychologist = sa.Column(sa.String, nullable=True)
    other_doctors = sa.Column(sa.String, nullable=True)
    blood_test = sa.Column(sa.String, nullable=True)
    urine_analysis = sa.Column(sa.String, nullable=True)
    feces_analysis = sa.Column(sa.String, nullable=True)
    general_diagnosis = sa.Column(sa.String, nullable=True)
    physical_development = sa.Column(sa.String, nullable=True)
    mental_development = sa.Column(sa.String, nullable=True)
    health_group = sa.Column(sa.String)
    sport_group = sa.Column(sa.String)
    med_and_ped_conclusion = sa.Column(sa.String, nullable=True)
    recommendations = sa.Column(sa.String, nullable=True)


class OngoingMedicalSupervision(BaseTable):
    __tablename__ = 'ongoing_medical_supervisions'
    medcard_num = sa.Column(sa.Integer, primary_key=True)
    examination_date = sa.Column(sa.Date, primary_key=True)
    examination_data = sa.Column(sa.String)
    diagnosis = sa.Column(sa.String)
    prescription = sa.Column(sa.String, nullable=True)
    doctor = sa.Column(sa.String)


class OralSanation(BaseTable):
    __tablename__ = 'oral_sanations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    sanation_date = sa.Column(sa.Date, primary_key=True)
    dental_result = sa.Column(sa.String)
    sanation_result = sa.Column(sa.String)


class Parent(BaseTable):
    __tablename__ = 'parents'

    id = sa.Column(sa.Integer, primary_key=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)
    birthday_year = sa.Column(sa.Integer)
    education = sa.Column(sa.String)
    phone_num = sa.Column(sa.BigInteger)


class PastIllness(BaseTable):
    __tablename__ = 'past_illnesses'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    start_date = sa.Column(sa.Date, primary_key=True)
    diagnosis = sa.Column(sa.String, primary_key=True)
    end_date = sa.Column(sa.Date)


class PrevaccinationCheckup(BaseTable):
    __tablename__ = 'prevaccination_checkups'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    examination_date = sa.Column(sa.Date, primary_key=True)
    vac_name_id = sa.Column(sa.Integer)
    age = sa.Column(sa.Integer, nullable=True)
    diagnosis = sa.Column(sa.String)
    report = sa.Column(sa.String)
    no_vac_date = sa.Column(sa.Date, nullable=True)
    doctor = sa.Column(sa.String)


class PrevaccinationCheckupView(BaseTable):
    __tablename__ = 'prevaccination_checkups_view'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    examination_date = sa.Column(sa.Date, primary_key=True)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer, nullable=True)
    diagnosis = sa.Column(sa.String)
    report = sa.Column(sa.String)
    no_vac_date = sa.Column(sa.Date, nullable=True)
    doctor = sa.Column(sa.String)


class Screening(BaseTable):
    __tablename__ = 'screenings'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    
    age = sa.Column(sa.Integer)
    questionnaire_test = sa.Column(sa.String)
    height = sa.Column(sa.Numeric(5,2))
    weight = sa.Column(sa.Numeric(5,2))
    physical_development = sa.Column(sa.String, nullable=True)
    blood_pressures = sa.Column(sa.String, nullable=True)
    carriage = sa.Column(sa.String, nullable=True)
    foot_condition = sa.Column(sa.String, nullable=True)
    sight_od = sa.Column(sa.Numeric(5,2), nullable=True)
    sight_os = sa.Column(sa.Numeric(5,2), nullable=True)
    visual_acuity = sa.Column(sa.String, nullable=True)
    malinovsky_test = sa.Column(sa.String, nullable=True)
    binocular_vision = sa.Column(sa.String, nullable=True)
    hearing_acuteness = sa.Column(sa.String, nullable=True)
    dynammetry_left = sa.Column(sa.Numeric(5,2), nullable=True)
    dynammetry_right = sa.Column(sa.Numeric(5,2), nullable=True)
    physical_fitness = sa.Column(sa.String, nullable=True)
    protein_in_urine = sa.Column(sa.String, nullable=True)
    glucose_in_urine = sa.Column(sa.String, nullable=True)
    biological_age = sa.Column(sa.String, nullable=True)
    speech_defects = sa.Column(sa.Boolean, nullable=True)
    kern_test = sa.Column(sa.Integer, nullable=True)
    neurotic_disorders = sa.Column(sa.Boolean, nullable=True)
    thinking_and_speech_disorders = sa.Column(sa.Boolean, nullable=True)
    motor_development_disorders = sa.Column(sa.Boolean, nullable=True)
    attention_and_memory_disorders = sa.Column(sa.Boolean, nullable=True)
    social_contacts_disorders = sa.Column(sa.Boolean, nullable=True)
    diseases_for_year = sa.Column(sa.Integer, nullable=True)


class SpaTreatment(BaseTable):
    __tablename__ = 'spa_treatments'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    start_date = sa.Column(sa.Date, primary_key=True)
    end_date = sa.Column(sa.Date, nullable=True)
    diagnosis = sa.Column(sa.String)
    founding_specialization = sa.Column(sa.String)
    climatic_zone = sa.Column(sa.String)


class TuberculosisVaccination(BaseTable):
    __tablename__ = 'tuberculosis_vaccinations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    vac_date = sa.Column(sa.Date, primary_key=True)
    serial = sa.Column(sa.String)
    dose = sa.Column(sa.Numeric(5,2))
    doctor = sa.Column(sa.String)


class User(BaseTable):
    __tablename__ = 'users'

    kindergarten_num = sa.Column(sa.Integer, primary_key=True)
    kindergarten_name = sa.Column(sa.String) 
    password_hash = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)


class VacName(BaseTable):
    __tablename__ = 'vac_names'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    vac_type = sa.Column(sa.String)


class Vaccination(BaseTable):
    __tablename__ = 'vaccinations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    vac_name_id = sa.Column(sa.Integer, primary_key=True)
    vac_type = sa.Column(sa.String, primary_key=True)
    vac_date = sa.Column(sa.Date)    
    serial = sa.Column(sa.String)
    dose = sa.Column(sa.Numeric(5,2))
    introduction_method = sa.Column(sa.String)
    reaction = sa.Column(sa.String)
    doctor = sa.Column(sa.String)


class ProfVaccination(BaseTable):
    __tablename__ = 'prof_vaccinations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    vac_name_id = sa.Column(sa.Integer, primary_key=True)
    vac_name = sa.Column(sa.String)
    vac_type = sa.Column(sa.String, primary_key=True)
    vac_date = sa.Column(sa.Date)
    serial = sa.Column(sa.String)
    dose = sa.Column(sa.Numeric(5,2))
    introduction_method = sa.Column(sa.String)
    reaction = sa.Column(sa.String)
    doctor = sa.Column(sa.String)


class EpidVaccination(BaseTable):
    __tablename__ = 'epid_vaccinations'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    vac_name_id = sa.Column(sa.Integer, primary_key=True)
    vac_name = sa.Column(sa.String)
    vac_type = sa.Column(sa.String, primary_key=True)
    vac_date = sa.Column(sa.Date)
    serial = sa.Column(sa.String)
    dose = sa.Column(sa.Numeric(5,2))
    introduction_method = sa.Column(sa.String)
    reaction = sa.Column(sa.String)
    doctor = sa.Column(sa.String)


class VisitSpecialistControl(BaseTable):
    __tablename__ = 'visit_specialist_controls'

    medcard_num = sa.Column(sa.Integer, primary_key=True)
    start_dispanser_date = sa.Column(sa.Date, primary_key=True)
    assigned_date = sa.Column(sa.Date, primary_key=True)
    fact_date = sa.Column(sa.Date, nullable=True)
