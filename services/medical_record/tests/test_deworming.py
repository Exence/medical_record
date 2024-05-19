from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.deworming import DewormingService
from models.medical_record.deworming import Deworming, DewormingCreate, DewormingUpdate, DewormingPK
from tables import Deworming as DewormingTable


@fixture
def deworming_service(mocker):
  session = mocker.Mock()
  return DewormingService(session=session)


@fixture
def db_deworming():
    return Deworming(
        medcard_num=123,
        deworming_date='2023-01-01',
        result='Отрицательно'
    )

@fixture
def deworming_pk():
    return DewormingPK(
        medcard_num=123,
        deworming_date='2023-01-01'
    )


def test_get_valid(deworming_service, db_deworming, deworming_pk):
    deworming_service.session.query().filter_by().first.return_value = db_deworming
    deworming = deworming_service._get(**deworming_pk.dict())

    assert deworming == db_deworming


def test_get_invalid(deworming_service, deworming_pk):
    deworming_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        deworming_service._get(**deworming_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_dewormings_by_medcard_num(deworming_service, db_deworming):
    deworming_service.session.query().filter_by().order_by().all.return_value = [db_deworming, db_deworming]

    dewormings = deworming_service.get_dewormings_by_medcard_num(medcard_num=123)

    assert dewormings == [db_deworming, db_deworming]


def test_get_deworming_by_pk(deworming_service, db_deworming, deworming_pk, mocker):
    mocker.patch.object(deworming_service, '_get', return_value=db_deworming)

    deworming = deworming_service.get_deworming_by_pk(deworming_pk)

    assert deworming == db_deworming


def test_add_new_deworming(deworming_service, db_deworming, mocker):
    deworming_create = DewormingCreate(**db_deworming.dict())
    
    deworming_service.session.add.return_value = db_deworming
    mock_deworming = mocker.MagicMock(spec=DewormingTable)

    mock_add = mocker.patch.object(deworming_service.session, 'add')
    mocker.patch('services.medical_record.deworming.Deworming', return_value=mock_deworming)
    deworming = deworming_service.add_new_deworming(deworming_create)

    mock_add.assert_called_once_with(mock_deworming)
    deworming_service.session.commit.assert_called_once()
    
    assert deworming == mock_deworming


def test_update_deworming(deworming_service, db_deworming, mocker):
    deworming_update_data = DewormingUpdate(**db_deworming.dict(), prev_deworming_date=db_deworming.deworming_date)
    deworming_update_data.deworming_date = '2024-01-01'
    updated_deworming = db_deworming
    updated_deworming.deworming_date = deworming_update_data.deworming_date
    mocker.patch.object(deworming_service, '_get', return_value=db_deworming)

    deworming = deworming_service.update_deworming(deworming_update_data)
    deworming_service.session.commit.assert_called_once()

    assert deworming == updated_deworming


def test_delete_deworming(deworming_service, db_deworming, deworming_pk, mocker):
    deworming = DewormingTable(**db_deworming.dict())
    mocker.patch.object(deworming_service, '_get', return_value=deworming)

    mock_delete = mocker.patch.object(deworming_service.session, 'delete')

    deworming_service.delete_deworming(deworming_pk)
    
    mock_delete.asassert_called_once_withs(deworming)
    deworming_service.session.commit.assert_called_once()
