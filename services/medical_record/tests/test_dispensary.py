from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.dispensary import DispensaryService
from models.medical_record.dispensary import Dispensary, DispensaryCreate, DispensaryUpdate, DispensaryPK
from tables import Dispensary as DispensaryTable


@fixture
def dispensary_service(mocker):
  session = mocker.Mock()
  return DispensaryService(session=session)


@fixture
def db_dispensary():
    return Dispensary(
        id=123,
        medcard_num=321,
        start_date='2023-01-01',
        diagnosis='diagnosis',
        specialist='specialist'
    )


@fixture
def dispensary_pk():
    return DispensaryPK(id=123)


def test_get_valid(dispensary_service, db_dispensary, dispensary_pk):
    dispensary_service.session.query().filter_by().first.return_value = db_dispensary
    dispensary = dispensary_service._get(**dispensary_pk.dict())

    assert dispensary == db_dispensary


def test_get_invalid(dispensary_service):
    dispensary_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        dispensary_service._get(id=123)
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_allergies_by_medcard_num(dispensary_service, db_dispensary):
    dispensary_service.session.query().filter_by().order_by().all.return_value = [db_dispensary, db_dispensary]

    allergies = dispensary_service.get_dispensaries_by_medcard_num(medcard_num=321)

    assert allergies == [db_dispensary, db_dispensary]


def test_get_dispensary_by_pk(dispensary_service, db_dispensary, dispensary_pk, mocker):
    mocker.patch.object(dispensary_service, '_get', return_value=db_dispensary)

    dispensary = dispensary_service.get_dispensary_by_pk(dispensary_pk)

    assert dispensary == db_dispensary


def test_add_new_dispensary(dispensary_service, db_dispensary, mocker):
    dispensary_create = DispensaryCreate(**db_dispensary.dict())
    
    dispensary_service.session.add.return_value = db_dispensary
    mock_dispensary = mocker.MagicMock(spec=DispensaryTable)

    mock_add = mocker.patch.object(dispensary_service.session, 'add')
    mocker.patch('services.medical_record.dispensary.Dispensary', return_value=mock_dispensary)
    dispensary = dispensary_service.add_new_dispensary(dispensary_create)

    mock_add.assert_called_once_with(mock_dispensary)
    dispensary_service.session.commit.assert_called_once()
    
    assert dispensary == mock_dispensary


def test_update_dispensary(dispensary_service, db_dispensary, mocker):
    dispensary_update_data = DispensaryUpdate(**db_dispensary.dict())
    dispensary_update_data.diagnosis = 'new diagnosis'
    updated_dispensary = db_dispensary
    updated_dispensary.diagnosis = dispensary_update_data.diagnosis
    mocker.patch.object(dispensary_service, '_get', return_value=db_dispensary)

    dispensary = dispensary_service.update_dispensary(dispensary_update_data)
    dispensary_service.session.commit.assert_called_once()

    assert dispensary == updated_dispensary


def test_delete_dispensary(dispensary_service, db_dispensary, dispensary_pk, mocker):
    dispensary = DispensaryTable(**db_dispensary.dict())
    mocker.patch.object(dispensary_service, '_get', return_value=dispensary)

    mock_delete = mocker.patch.object(dispensary_service.session, 'delete')

    dispensary_service.delete_dispensary(dispensary_pk)
    
    mock_delete.asassert_called_once_withs(dispensary)
    dispensary_service.session.commit.assert_called_once()
