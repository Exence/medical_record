from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.hospitalization import HospitalizationService
from models.medical_record.hospitalization import Hospitalization, HospitalizationCreate, HospitalizationUpdate, HospitalizationPK
from tables import Hospitalization as HospitalizationTable


@fixture
def hospitalization_service(mocker):
  session = mocker.Mock()
  return HospitalizationService(session=session)


@fixture
def db_hospitalization():
    return Hospitalization(
        medcard_num=123,
        start_date='2023-01-01',
        diagnosis='diagnosis',
        founding='founding'
    )

@fixture
def hospitalization_pk():
    return HospitalizationPK(
        medcard_num=123,
        start_date='2023-01-01'
    )


def test_get_valid(hospitalization_service, db_hospitalization, hospitalization_pk):
    hospitalization_service.session.query().filter_by().first.return_value = db_hospitalization
    hospitalization = hospitalization_service._get(**hospitalization_pk.dict())

    assert hospitalization == db_hospitalization


def test_get_invalid(hospitalization_service, hospitalization_pk):
    hospitalization_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        hospitalization_service._get(**hospitalization_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_hospitalizations_by_medcard_num(hospitalization_service, db_hospitalization):
    hospitalization_service.session.query().filter_by().order_by().all.return_value = [db_hospitalization, db_hospitalization]

    hospitalizationes = hospitalization_service.get_hospitalizations_by_medcard_num(medcard_num=123)

    assert hospitalizationes == [db_hospitalization, db_hospitalization]


def test_get_hospitalization_by_pk(hospitalization_service, db_hospitalization, hospitalization_pk, mocker):
    mocker.patch.object(hospitalization_service, '_get', return_value=db_hospitalization)

    hospitalization = hospitalization_service.get_hospitalization_by_pk(hospitalization_pk)

    assert hospitalization == db_hospitalization


def test_add_new_hospitalization(hospitalization_service, db_hospitalization, mocker):
    hospitalization_create = HospitalizationCreate(**db_hospitalization.dict())
    
    hospitalization_service.session.add.return_value = db_hospitalization
    mock_hospitalization = mocker.MagicMock(spec=HospitalizationTable)

    mock_add = mocker.patch.object(hospitalization_service.session, 'add')
    mocker.patch('services.medical_record.hospitalization.Hospitalization', return_value=mock_hospitalization)
    hospitalization = hospitalization_service.add_new_hospitalization(hospitalization_create)

    mock_add.assert_called_once_with(mock_hospitalization)
    hospitalization_service.session.commit.assert_called_once()
    
    assert hospitalization == mock_hospitalization


def test_update_hospitalization(hospitalization_service, db_hospitalization, mocker):
    hospitalization_update_data = HospitalizationUpdate(**db_hospitalization.dict(), 
                                                        prev_start_date=db_hospitalization.start_date
                                                        )
    hospitalization_update_data.start_date = '2024-01-01'
    updated_hospitalization = db_hospitalization
    updated_hospitalization.start_date = hospitalization_update_data.start_date
    mocker.patch.object(hospitalization_service, '_get', return_value=db_hospitalization)

    hospitalization = hospitalization_service.update_hospitalization(hospitalization_update_data)
    hospitalization_service.session.commit.assert_called_once()

    assert hospitalization == updated_hospitalization


def test_delete_hospitalization(hospitalization_service, db_hospitalization, hospitalization_pk, mocker):
    hospitalization = HospitalizationTable(**db_hospitalization.dict())
    mocker.patch.object(hospitalization_service, '_get', return_value=hospitalization)

    mock_delete = mocker.patch.object(hospitalization_service.session, 'delete')

    hospitalization_service.delete_hospitalization(hospitalization_pk)
    
    mock_delete.asassert_called_once_withs(hospitalization)
    hospitalization_service.session.commit.assert_called_once()
