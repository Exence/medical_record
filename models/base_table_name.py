from enum import Enum
from pydantic import BaseModel
from models.medical_record.child import Child
from models.medical_record.allergy import Allergy
from models.catalogs.clinic import Clinic
from models.medical_record.deworming import Deworming
from models.medical_record.dispensary import Dispensary
from models.medical_record.extra_class import ExtraClass
from models.medical_record.gg_injection import GammaGlobulinInjection
from models.medical_record.hospitalization import Hospitalization
from models.medical_record.mantoux_test import MantouxTest
from models.medical_record.medical_certificate import MedicalCertificate
from models.medical_record.medical_examination import MedicalExamination
from models.medical_record.ongoing_medical_supervision import OngoingMedicalSupervision
from models.medical_record.oral_sanation import OralSanation
from models.medical_record.parent import Parent
from models.medical_record.past_illness import PastIllness
from models.medical_record.prevaccination_checkup import PrevaccinationCheckup
from models.medical_record.screening import Screening
from models.medical_record.spa_treatment import SpaTreatment
from models.medical_record.tub_vac import TuberculosisVaccination
from models.catalogs.vac_name import VacName
from models.medical_record.vaccination import Vaccination
from models.medical_record.visit_specialist_control import VisitSpecialistControl

class BaseTableNameModel(str, Enum):
    Child = 'Child'
    Allergy = 'Allergy'
    Clinic = 'Clinic'
    Deworming = 'Deworming'
    Dispensary = 'Dispensary'
    ExtraClass = 'ExtraClass'
    GammaGlobulinInjection = 'GammaGlobulinInjection'
    Hospitalization = 'Hospitalization'
    MantouxTest = 'MantouxTest'
    MedicalCertificate = 'MedicalCertificate'
    MedicalExamination = 'MedicalExamination'
    OngoingMedicalSupervision = 'OngoingMedicalSupervision'
    OralSanation = 'OralSanation'
    Parent = 'Parent'
    PastIllness = 'PastIllness'
    PrevaccinationCheckup = 'PrevaccinationCheckup'
    Screening = 'Screening'
    SpaTreatment = 'SpaTreatment'
    TuberculosisVaccination = 'TuberculosisVaccination'
    VacName = 'VacName'
    Vaccination = 'Vaccination'
    VisitSpecialistControl = 'VisitSpecialistControl'

class TableBaseModel(Enum):
    Child = Child
    Allergy = Allergy
    Clinic = Clinic
    Deworming = Deworming
    Dispensary = Dispensary
    ExtraClass = ExtraClass
    GammaGlobulinInjection = GammaGlobulinInjection
    Hospitalization = Hospitalization
    MantouxTest = MantouxTest
    MedicalCertificate = MedicalCertificate
    MedicalExamination = MedicalExamination
    OngoingMedicalSupervision = OngoingMedicalSupervision
    OralSanation = OralSanation
    Parent = Parent
    PastIllness = PastIllness
    PrevaccinationCheckup = PrevaccinationCheckup
    Screening = Screening
    SpaTreatment = SpaTreatment
    TuberculosisVaccination = TuberculosisVaccination
    VacName = VacName
    Vaccination = Vaccination
    VisitSpecialistControl = VisitSpecialistControl
