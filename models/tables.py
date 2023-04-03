from datetime import date
from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    validator,
)
import re


LETTER_MATCH_PATTERN_WITH_SPACE = re.compile(r"^[а-яА-Яa-zA-Z\- ]+$")
REACTION_MATCH_PATTERN = re.compile(r"^(Не|За)медленная$")

class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class MedicalCertificateBase(BaseModel):
    medcard_num: int = Field(...)
    disease: str = Field(..., max_length=250)
    cert_date: date = Field(...)
    start_date: date  = Field(...)
    end_date: date = Field(...)
    infection_contact: bool = Field(...)
    sport_exemption_date: date
    vac_exemption_date: date
    doctor: str = Field(..., max_length=200)

class MedicalCertificate(MedicalCertificateBase, OrmModel):
    pass

class MedicalCertificateCreate(MedicalCertificateBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class AllergyBase(BaseModel):
    medcard_num: int = Field(...)
    allergen: str = Field(...)
    allergy_type: str = Field(...)
    start_age: int = Field(...)
    reaction_type: str = Field(...)
    diagnosis_date: date = Field(...)
    note: str

class Allergy(AllergyBase, OrmModel):
    pass

class AllergyCreate(AllergyBase):
    @validator("allergy_type")
    def validate_allergy_type(cls, value):
        if not value in ['Вакцинальная',  'Лекарственная',  'Аллергические заболевания']:
            raise HTTPException(
                status_code=422, detail="Allergy type should be in ['Вакцинальная',  'Лекарственная',  'Аллергические заболевания']"
            )
        return value


class ExtraClassBase(BaseModel):
    medcard_num: int = Field(...)
    classes_type: str = Field(...)
    age: int = Field(...,gt=0, lt=8)
    hours_on_week: int = Field(...,gt=0, lt=40)

class ExtraClass(ExtraClassBase, OrmModel):
    pass

class ExtraClassCreate(ExtraClassBase):
    pass


class HospitalizationBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date
    diagnosis: int = Field(...)
    founding: str = Field(..., max_length=200)

class Hospitalization(HospitalizationBase, OrmModel):
    pass

class HospitalizationCreate(HospitalizationBase):
    pass


class SpaTreatmentBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date
    diagnosis: str = Field(...)
    founding_specialization:str = Field(..., max_length=200)
    climatic_zone: str = Field(..., max_length=200)

class SpaTreatment(SpaTreatmentBase, OrmModel):
    pass

class SpaTreatmentCreate(SpaTreatmentBase):
    pass


class SkipingByDiseaseBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    end_date: date
    diagnosis: int = Field(...)

class SkipingByDisease(SkipingByDiseaseBase, OrmModel):
    pass

class SkipingByDiseaseCreate(SkipingByDiseaseBase):
    pass


class DispensaryBase(BaseModel):
    medcard_num: int = Field(...)
    start_date: date = Field(...)
    diagnosis: str = Field(...)
    end_date: date
    end_reason: str

class Dispensary(DispensaryBase):
    pass

class DispensaryCreate(DispensaryBase):
    pass


class VisitSpecialistControlBase(BaseModel):
    medcard_num: int = Field(...)
    start_dispanser_date: date = Field(...)
    assigned_date: date = Field(...)
    fact_date: date

class VisitSpecialistControl(VisitSpecialistControlBase, OrmModel):
    pass

class VisitSpecialistControlCreate(VisitSpecialistControlBase):
    pass


class DewormingBase(BaseModel):
    medcard_num: int = Field(...)
    deworming_date: date = Field(...)
    result: str = Field(...)

class Deworming(DewormingBase, OrmModel):
    pass

class DewormingCreate(DewormingBase):
    pass


class OralSonationBase(BaseModel):
    medcard_num: int = Field(...)
    sanation_date: date = Field(...)
    dental_result: str = Field(...)
    sanation_result: str = Field(...)

class OralSonation(OralSonationBase, OrmModel):
    pass

class OralSonationCreate(OralSonationBase):
    pass


class PrevaccinationCheckupBase(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)
    age: int = Field(...)
    diagnosis: str = Field(...)
    report: str = Field(...)
    vac_name: str = Field(..., max_length=200)
    no_vac_date: date
    doctor: str = Field(..., max_length=200)

class PrevaccinationCheckup(PrevaccinationCheckupBase, OrmModel):
    pass

class PrevaccinationCheckupCreate(PrevaccinationCheckupBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class VaccinationBase(BaseModel):
    medcard_num: int = Field(...)
    vac_name: str = Field(..., max_length=200)
    vac_type: str = Field(..., max_length=16)
    vac_date: date = Field(...)
    serial: str = Field(..., max_length=90)
    dose: float = Field(...)
    introduction_method: str = Field(..., max_length=90)
    reaction: str = Field(...)
    doctor: str = Field(..., max_length=200)

class Vaccination(VaccinationBase, OrmModel):
    pass

class VaccinationCreate(VaccinationBase):
    @validator("vac_type")
    def validate_vac_type(cls, value):
        if not re.compile(r"(^Вакцинация ?I{1,3}$)|(^Ревакцинация ?I{1,3}?V{0,1}$)").match(value):
            raise HTTPException(
                status_code=422, detail="Vaccination type should be in 'Вакцинация I-III' or 'Ревакцинация I-IV'"
            )
        return value
    
    @validator("reaction")
    def validate_vac_type(cls, value):
        if not REACTION_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Reaction should be 'Немедленная' or 'Замедленная'"
            )
        return value
    
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class TuberculosisVaccinationBase(BaseModel):
    medcard_num: int = Field(...)
    vac_date: date = Field(...)
    serial: str = Field(..., max_length=90)
    dose: float = Field(...)
    doctor: str = Field(..., max_length=200)

class TuberculosisVaccination(TuberculosisVaccinationBase, OrmModel):
    pass

class TuberculosisVaccinationCreate(TuberculosisVaccinationBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class GammaGlobulinInjectionBase(BaseModel):
    medcard_num: int = Field(...)
    vac_date: date = Field(...)
    reason: str = Field(...)
    serial: str = Field(..., max_length=90)
    dose: float = Field(...)
    reaction: str = Field(...)
    doctor: str = Field(..., max_length=200)

class GammaGlobulinInjection(GammaGlobulinInjectionBase, OrmModel):
    pass

class GammaGlobulinInjectionCreate(GammaGlobulinInjectionBase):
    @validator("reaction")
    def validate_vac_type(cls, value):
        if not REACTION_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Reaction should be 'Немедленная' or 'Замедленная'"
            )
        return value
    
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class MantouxTestBase(BaseModel):
    medcard_num: int = Field(...)
    check_date: date = Field(...)
    result: str = Field(...)

class MantouxTest(MantouxTestBase, OrmModel):
    pass

class MantouxTestCreate(MantouxTestBase):
    pass


class MedicalExaminationBase(BaseModel):
    medcard_num: int = Field(...)
    period: str = Field(...)
    inspection_date: date = Field(...)
    age: int = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    complaints: str
    pediatrician: str
    orthopaedist: str
    ophthalmologist: str
    otolaryngologist: str
    dermatologist: str
    neurologist: str
    speech_therapist: str
    denta_surgeon: str
    psychologist: str
    other_doctors: str
    blood_test: str
    urine_analysis: str
    feces_analysis: str
    general_diagnosis: str
    physical_development: str
    mental_development: str
    health_group: str
    sport_group: str
    med_and_ped_conclusion: str
    recommendations: str
    doctor: str = Field(..., max_length=200)

class MedicalExamination(MedicalExaminationBase, OrmModel):
    pass

class MedicalExaminationCreate(MedicalExaminationBase):
    @validator("period")
    def validate_period(cls, value):
        if not value in ['Перед поступлением в ясли-сад, детский сад', 'За 1 год до школы', 'Перед школой']:
            raise HTTPException(
                status_code=422, detail="Period type should be in ['Перед поступлением в ясли-сад, детский сад', 'За 1 год до школы', 'Перед школой']"
            )
        return value
    
    @validator("health_group")
    def validate_health_group(cls, value):
        if not re.compile(r"^(I{1,3})$|^(IV)$").match(value):
            raise HTTPException(
                status_code=422, detail="Health group should be I-IV"
            )
        return value
    
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class OngoingMedicalSupervisionBase(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)
    examination_data: str = Field(...)
    diagnosis: str = Field(...)
    prescription: str
    doctor: str = Field(..., max_length=200)

class OngoingMedicalSupervision(OngoingMedicalSupervisionBase, OrmModel):
    pass

class OngoingMedicalSupervisionCreate(OngoingMedicalSupervisionBase):
    @validator("doctor")
    def validate_doctor(cls, value):
        if not LETTER_MATCH_PATTERN_WITH_SPACE.match(value):
            raise HTTPException(
                status_code=422, detail="Field doctor should contains only letters"
            )
        return value


class ScreeningBase(BaseModel):
    medcard_num: int = Field(...)
    examination_date: date = Field(...)
    age: int = Field(...)
    questionnaire_test: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    physical_development: str
    blood_pressures: str
    carriage: str
    foot_condition: str
    sight_od: float
    sight_os: float
    visual_acuity: str
    malinovsky_test: str
    binocular_vision: str
    hearing_acuteness: str
    dynammetry_left: float
    dynammetry_right: float
    physical_fitness: str
    protein_in_urine: str
    glucose_in_urine: str
    biological_age: str
    speech_defects: bool
    kern_test: bool
    neurotic_disorders: bool
    thinking_and_speech: bool
    motor_development: bool
    attention_and_memory: bool
    social_contacts: bool
    diseases_for_year: bool

class Screening(ScreeningBase, OrmModel):
    pass

class ScreeningCreate(ScreeningBase):
    @validator("questionnaire_test")
    def validate_questionnaire_test(cls, value):
        if not value in ['Норма', 'Отклонение']:
            raise HTTPException(
                status_code=422, detail="Questionnaire test should be in ['Норма', 'Отклонение']"
            )
        return value
    
    @validator("questionnaire_test")
    def validate_physical_development(cls, value):
        if not value in ['Нормальное', 'Низкий рост', 'Дефицит массы', 'Избыток массы']:
            raise HTTPException(
                status_code=422, detail="Physical development test should be in ['Нормальное', 'Низкий рост', 'Дефицит массы', 'Избыток массы']"
            )
        return value
    
    @validator("carriage")
    def validate_carriage(cls, value):
        if not value in ['Нормальная', 'Незначительные отклонения', 'Значительные нарушения']:
            raise HTTPException(
                status_code=422, detail="Carriage should be in ['Нормальная', 'Незначительные отклонения', 'Значительные нарушения']"
            )
        return value
    
    @validator("foot_condition")
    def validate_foot_condition(cls, value):
        if not value in ['Нормальная', 'Уплощена', 'Плоская']:
            raise HTTPException(
                status_code=422, detail="Foot condition should be in ['Нормальная', 'Уплощена', 'Плоская']"
            )
        return value
    
    @validator("visual_acuity")
    def validate_visual_acuity(cls, value):
        if not value in ['Нормальная', 'Снижена']:
            raise HTTPException(
                status_code=422, detail="Visual acuity should be in ['Нормальная', 'Снижена']"
            )
        return value
    
    @validator("malinovsky_test")
    def validate_malinovsky_test(cls, value):
        if not value in ['Нормальная', 'Предмиопия']:
            raise HTTPException(
                status_code=422, detail="Malinovsky test should be in ['Нормальная', 'Предмиопия']"
            )
        return value
    
    @validator("binocular_vision")
    def validate_binocular_vision(cls, value):
        if not value in ['Норма', 'Нарушение']:
            raise HTTPException(
                status_code=422, detail="Binocular vision should be in ['Норма', 'Нарушение']"
            )
        return value
    
    @validator("hearing_acuteness")
    def validate_hearing_acuteness(cls, value):
        if not value in ['Норма', 'Снижена']:
            raise HTTPException(
                status_code=422, detail="Hearing acuteness should be in ['Норма', 'Снижена']"
            )
        return value
    
    @validator("physical_fitness")
    def validate_physical_fitness(cls, value):
        if not value in ['Норма', 'Снижена', 'Повышена']:
            raise HTTPException(
                status_code=422, detail="Physical fitness should be in ['Норма', 'Снижена', 'Повышена']"
            )
        return value
    
    @validator("protein_in_urine")
    def validate_protein_in_urine(cls, value):
        if not value in ['Норма', 'Следы белка', 'Белок в моче']:
            raise HTTPException(
                status_code=422, detail="Protein in urine should be in ['Норма', 'Следы белка', 'Белок в моче']"
            )
        return value
    
    @validator("glucose_in_urine")
    def validate_glucose_in_urine(cls, value):
        if not value in ['Норма', 'Глюкоза в моче']:
            raise HTTPException(
                status_code=422, detail="Glucose in urine should be in ['Норма', 'Глюкоза в моче']"
            )
        return value
    
    @validator("biological_age")
    def validate_biological_age(cls, value):
        if not value in ['Соответствует', 'Опережает', 'Отстает']:
            raise HTTPException(
                status_code=422, detail="Biological age should be in ['Соответствует', 'Опережает', 'Отстает']"
            )
        return value
