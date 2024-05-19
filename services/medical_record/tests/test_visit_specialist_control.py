from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.visit_specialist_control import VisitSpecialistControlService
from models.medical_record.visit_specialist_control import VisitSpecialistControl, VisitSpecialistControlCreate, VisitSpecialistControlUpdate, VisitSpecialistControlPK
from tables import VisitSpecialistControl as VisitSpecialistControlTable


@fixture
def visit_specialist_control_service(mocker):
  session = mocker.Mock()
  return VisitSpecialistControlService(session=session)


@fixture
def db_visit_specialist_control():
    return VisitSpecialistControl(
        dispensary_id=123,
        assigned_date='2023-01-01'
    )

@fixture
def visit_specialist_control_pk():
    return VisitSpecialistControlPK(
        dispensary_id=123,
        assigned_date='2023-01-01'
    )


def test_get_valid(visit_specialist_control_service, db_visit_specialist_control, visit_specialist_control_pk):
    visit_specialist_control_service.session.query().filter_by().first.return_value = db_visit_specialist_control
    visit_specialist_control = visit_specialist_control_service._get(**visit_specialist_control_pk.dict())

    assert visit_specialist_control == db_visit_specialist_control


def test_get_invalid(visit_specialist_control_service, visit_specialist_control_pk):
    visit_specialist_control_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        visit_specialist_control_service._get(**visit_specialist_control_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_visit_specialist_controls_by_medcard_num(visit_specialist_control_service, db_visit_specialist_control):
    visit_specialist_control_service.session.query().filter_by().order_by().all.return_value = [db_visit_specialist_control, db_visit_specialist_control]

    visit_specialist_controls = visit_specialist_control_service.get_visit_specialist_controls_by_medcard_num(medcard_num=123)

    assert visit_specialist_controls == [db_visit_specialist_control, db_visit_specialist_control]


def test_get_visit_specialist_control_by_pk(visit_specialist_control_service, db_visit_specialist_control, visit_specialist_control_pk, mocker):
    mocker.patch.object(visit_specialist_control_service, '_get', return_value=db_visit_specialist_control)

    visit_specialist_control = visit_specialist_control_service.get_visit_specialist_control_by_pk(visit_specialist_control_pk)

    assert visit_specialist_control == db_visit_specialist_control


def test_add_new_visit_specialist_control(visit_specialist_control_service, db_visit_specialist_control, mocker):
    visit_specialist_control_create = VisitSpecialistControlCreate(**db_visit_specialist_control.dict())
    
    visit_specialist_control_service.session.add.return_value = db_visit_specialist_control
    mock_visit_specialist_control = mocker.MagicMock(spec=VisitSpecialistControlTable)

    mock_add = mocker.patch.object(visit_specialist_control_service.session, 'add')
    mocker.patch('services.medical_record.visit_specialist_control.VisitSpecialistControl', return_value=mock_visit_specialist_control)
    visit_specialist_control = visit_specialist_control_service.add_new_visit_specialist_control(visit_specialist_control_create)

    mock_add.assert_called_once_with(mock_visit_specialist_control)
    visit_specialist_control_service.session.commit.assert_called_once()
    
    assert visit_specialist_control == mock_visit_specialist_control


def test_update_visit_specialist_control(visit_specialist_control_service, db_visit_specialist_control, mocker):
    visit_specialist_control_update_data = VisitSpecialistControlUpdate(**db_visit_specialist_control.dict(),
                                                                        prev_assigned_date=db_visit_specialist_control.assigned_date)
    visit_specialist_control_update_data.fact_date = '2023-01-01'
    updated_visit_specialist_control = db_visit_specialist_control
    updated_visit_specialist_control.fact_date = visit_specialist_control_update_data.fact_date
    mocker.patch.object(visit_specialist_control_service, '_get', return_value=db_visit_specialist_control)

    visit_specialist_control = visit_specialist_control_service.update_visit_specialist_control(visit_specialist_control_update_data)
    visit_specialist_control_service.session.commit.assert_called_once()

    assert visit_specialist_control == updated_visit_specialist_control


def test_delete_visit_specialist_control(visit_specialist_control_service, db_visit_specialist_control, visit_specialist_control_pk, mocker):
    visit_specialist_control = VisitSpecialistControlTable(**db_visit_specialist_control.dict())
    mocker.patch.object(visit_specialist_control_service, '_get', return_value=visit_specialist_control)

    mock_delete = mocker.patch.object(visit_specialist_control_service.session, 'delete')

    visit_specialist_control_service.delete_visit_specialist_control(visit_specialist_control_pk)
    
    mock_delete.asassert_called_once_withs(visit_specialist_control)
    visit_specialist_control_service.session.commit.assert_called_once()
