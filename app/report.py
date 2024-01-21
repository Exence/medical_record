from datetime import date
from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from models.auth import Token
from models.json import JsonForm
from models.tub_diagnostic import TubDiagnostic
from models.user import User
from models.vaccination import VacReport
from services.auth import (
    AuthService,
    get_current_user,
)

from services.report import ReportService
from services.vac_name import VacNameService


router = APIRouter(
    prefix='/reports',
    tags=['Reports']
)
templates = Jinja2Templates(directory="templates")


@router.get('/tuberculin/{start_date}/{end_date}')
def get_tub_diagnostic_report(start_date: date, end_date: date, request: Request, service: ReportService = Depends(), user: User = Depends(get_current_user)):
    tub_positive_childrens = service.get_childrens_by_mantoux_test_result(
        user, 'Положительно', start_date, end_date)
    tub_doubtful_childrens = service.get_childrens_by_mantoux_test_result(
        user, 'Сомнительно', start_date, end_date)
    tub_negative_childrens = service.get_childrens_by_mantoux_test_result(
        user, 'Отрицательно', start_date, end_date)
    positive = len(tub_positive_childrens)
    doubtful = len(tub_doubtful_childrens)
    negative = len(tub_negative_childrens)
    absolute = positive + doubtful + negative
    tub_diagnostic = TubDiagnostic(start_date=start_date,
                                   end_date=end_date,
                                   absolute=absolute,
                                   positive_count=positive,
                                   doubtful_count=doubtful,
                                   negative_count=negative)
    return templates.TemplateResponse(
        "/reports/tub/index.html", {"request": request,
                                    "tub_positive_childrens": tub_positive_childrens,
                                    "tub_doubtful_childrens": tub_doubtful_childrens,
                                    "tub_negative_childrens": tub_negative_childrens,
                                    "tub_diagnostic": tub_diagnostic
                                    }
    )


@router.post('/vac_report')
def get_vac_report(request: Request,
                   form_data: VacReport = Depends(VacReport.as_form),
                   report_service: ReportService = Depends(),
                   vac_name_service: VacNameService = Depends(),
                   user: User = Depends(get_current_user)):
    vaccinated_childrens = report_service.get_childrens_by_vaccine(
        user, form_data)
    vac_name = vac_name_service.get_vac_name_by_pk({id: form_data.vac_name_id})
    vaccination = {
        "vac_name": vac_name.name,
        "vac_type": form_data.vac_type,
        "absolute": len(vaccinated_childrens)
    }

    return templates.TemplateResponse(
        "/reports/vac/index.html", {"request": request,
                                    "vaccinated_childrens": vaccinated_childrens,
                                    "vaccination": vaccination
                                    }
    )
