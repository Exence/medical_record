from datetime import date
from fastapi import (
    APIRouter,
    Form,
    HTTPException,
    Depends,
    Response,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from settings import templates
from fastapi.responses import RedirectResponse

from models.reports.tub_diagnostic import TubDiagnostic
from models.reports.dew_diagnostic import DewDiagnostic
from models.reports.annual import AgeType
from models.user import User
from models.medical_record.vaccination import VacReport
from services.auth import (
    AuthService,
    get_current_user,
)

from services.report import ReportService
from services.catalogs.vac_name import VacNameService


router = APIRouter(
    prefix='/reports',
    tags=['Reports']
)



@router.get('/tuberculin/{start_date}/{end_date}')
def get_tub_diagnostic_report(start_date: date, end_date: date, request: Request, service: ReportService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
        
    tub_positive_children = service.get_children_by_mantoux_test_result(
        'Положительно', start_date, end_date)
    tub_doubtful_children = service.get_children_by_mantoux_test_result(
        'Сомнительно', start_date, end_date)
    tub_negative_children = service.get_children_by_mantoux_test_result(
        'Отрицательно', start_date, end_date)
    positive = len(tub_positive_children)
    doubtful = len(tub_doubtful_children)
    negative = len(tub_negative_children)
    absolute = positive + doubtful + negative
    tub_diagnostic = TubDiagnostic(start_date=start_date,
                                end_date=end_date,
                                absolute=absolute,
                                positive_count=positive,
                                doubtful_count=doubtful,
                                negative_count=negative)
    return templates.TemplateResponse(
        "/reports/tub/index.html", {"request": request,
                                    "tub_positive_children": tub_positive_children,
                                    "tub_doubtful_children": tub_doubtful_children,
                                    "tub_negative_children": tub_negative_children,
                                    "tub_diagnostic": tub_diagnostic
                                    }
    )


@router.get('/deworming/{start_date}/{end_date}')
def get_deworming_report(start_date: date, end_date: date, request: Request, service: ReportService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    dew_positive_children = service.        get_children_by_deworming_result(
        'Положительно', start_date, end_date)
    dew_negative_children = service.        get_children_by_deworming_result(
        'Отрицательно', start_date, end_date)
    positive = len(dew_positive_children)
    negative = len(dew_negative_children)
    absolute = positive + negative
    dew_diagnostic = DewDiagnostic(start_date=start_date,
                                end_date=end_date,
                                absolute=absolute,
                                positive_count=positive,
                                negative_count=negative)
    return templates.TemplateResponse(
        "/reports/dew/index.html", {"request": request,
                                    "dew_positive_children": dew_positive_children,
                                    "dew_negative_children": dew_negative_children,
                                    "dew_diagnostic": dew_diagnostic
                                    }
    )


@router.post('/vac_report')
def get_vac_report(request: Request,
                   form_data: VacReport = Depends(VacReport.as_form),
                   report_service: ReportService = Depends(),
                   vac_name_service: VacNameService = Depends(),
                   user: User = Depends(get_current_user)):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    vaccinated_children = report_service.get_children_by_vaccine(form_data)
    vac_name = vac_name_service.get_vac_name_by_id(form_data.vac_name_id)
    vaccination = {
        "vac_name": vac_name.name,
        "vac_type": form_data.vac_type,
        "absolute": len(vaccinated_children)
    }

    return templates.TemplateResponse(
        "/reports/vac/index.html", {"request": request,
                                    "vaccinated_children": vaccinated_children,
                                    "vaccination": vaccination
                                    }
    )
    

@router.post('/annual')
def get_annual_report(request: Request,
                      age_type: AgeType =Form(),
                      year: int = Form(),
                      report_service: ReportService = Depends()):
    try:
        access_token=str(request.cookies.get("access_token")).replace("bearer ","")
        get_current_user(access_token=access_token) 
    except HTTPException as e:
        if e.status_code == 401:
            return RedirectResponse('/')
    report = report_service.get_annual_report_by_age_type(age_type=age_type, year=year)
    return templates.TemplateResponse(
        "/reports/annual/index.html", {"request": request,
                                    "report": report 
                                    }
    )
