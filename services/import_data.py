from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from models.base_table_name import TableBaseModel

from services.catalogs.clinic import ClinicService
from services.medical_record.dispensary import DispensaryService
from services.medical_record.medical_record import MedicalRecordService
from services.medical_record.parent import ParentService
from services.medical_record.visit_specialist_control import VisitSpecialistControlService

from models.catalogs.clinic import ClinicCreate
from models.medical_record.child import ChildCreate
from models.medical_record.dispensary import DispensaryCreate
from models.medical_record.parent import ParentCreate
from models.medical_record.visit_specialist_control import VisitSpecialistControlCreate



def create_obj_generator_from_ws(ws: Worksheet, tab_name: str):
    enum_table = {
        "TableBaseModel": TableBaseModel
    }
    obj_gen = ws.values
    headers = next(obj_gen)
    for data in obj_gen:
        data_as_dict = dict(zip(headers, data))
        obj = enum_table["TableBaseModel"][tab_name].value(**data_as_dict)
        yield obj


def import_from_xlsx(filename: str,
                     kindergarten_num: int,
                     medcard_service: MedicalRecordService,
                     clinic_service: ClinicService,
                     parent_service: ParentService,
                     dispensary_service: DispensaryService,
                     visit_s_control_service: VisitSpecialistControlService,
                     ):
    wb = load_workbook(filename=filename)
    service_tabs = ['Child', 'Clinic', 'Parent', 'VacName', 'Dispensary']

    ws = wb["Child"]
    child_gen = create_obj_generator_from_ws(ws=ws, tab_name="Child")
    child = next(child_gen)
    child.kindergarten_num = kindergarten_num

    # Clinic
    ws = wb["Clinic"]
    clinics_gen = create_obj_generator_from_ws(ws=ws, tab_name="Clinic")
    clinic = next(clinics_gen)
    db_clinic = clinic_service.get_clinic_by_name(name=clinic.name)
    if db_clinic:
        child.clinic_id  = db_clinic.id
    else:
        clinic = clinic_service.add_new_clinic(clinic_data=ClinicCreate(name=clinic.name))
        child.clinic_id = clinic.id

    child.medcard_num = medcard_service.add_new_medcard(child_data=ChildCreate(**child.dict())).medcard_num
    
    
    # Parent
    ws = wb["Parent"]
    parent_gen = create_obj_generator_from_ws(ws=ws, tab_name="Parent")
    if child.father_id:
        father = next(parent_gen)
        db_father = parent_service.get_paren_by_full_data(parent_data=father)
        if db_father:
            child.father_id = db_father.id
        else:
            father = parent_service.add_new_parent(medcard_num=child.medcard_num, parent_data=ParentCreate(**father.dict(), parent_type='father'))
            child.father_id = father.id

    if child.mother_id:
        mother = next(parent_gen)
        db_mother = parent_service.get_paren_by_full_data(parent_data=mother)
        if db_mother:
            child.mother_id = db_mother.id
        else:
            mother = parent_service.add_new_parent(medcard_num=child.medcard_num, parent_data=ParentCreate(**mother.dict(), parent_type='mother'))
            child.mother_id = mother.id

    # Dispensary
    visit_ws = wb["VisitSpecialistControl"]
    visit_s_control_gen = create_obj_generator_from_ws(ws=visit_ws, tab_name="VisitSpecialistControl")
    visit_s_control_list = list(visit_s_control_gen)
    ws = wb["Dispensary"]
    dispensaryes_gen = create_obj_generator_from_ws(ws=ws, tab_name="Dispensary")
    for dispensary in dispensaryes_gen:
        old_dispensary_id = dispensary.id
        dispensary.medcard_num = child.medcard_num
        dispensary = dispensary_service.add_new_dispensary(dispensary_data=DispensaryCreate(**dispensary.dict()))
        
        for visit_s_control in visit_s_control_list:
            if visit_s_control.dispensary_id == old_dispensary_id:
                visit_s_control.dispensary_id = dispensary.id
                visit_s_control_service.add_new_visit_specialist_control(visit_specialist_control_data=VisitSpecialistControlCreate(**visit_s_control.dict()))
                visit_s_control_list.remove(visit_s_control)


    for tab_name in wb.sheetnames:
        if tab_name not in service_tabs:
            ws = wb[tab_name]
            headers = next(ws.values)
            data = list()
            for value in ws.values:
                data.append(dict(zip(headers, value)))
                

            