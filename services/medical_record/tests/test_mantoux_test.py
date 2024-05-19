from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.mantoux_test import MantouxTestService
from models.medical_record.mantoux_test import MantouxTest, MantouxTestCreate, MantouxTestUpdate, MantouxTestPK
from tables import MantouxTest as MantouxTestTable


@fixture
def mantoux_test_service(mocker):
  session = mocker.Mock()
  return MantouxTestService(session=session)


@fixture
def db_mantoux_test():
    return MantouxTest(
        medcard_num=123,
        check_date='2023-01-01',
        result='Отрицательно'
    )

@fixture
def mantoux_test_pk():
    return MantouxTestPK(
        medcard_num=123,
        check_date='2023-01-01'
    )


def test_get_valid(mantoux_test_service, db_mantoux_test, mantoux_test_pk):
    mantoux_test_service.session.query().filter_by().first.return_value = db_mantoux_test
    mantoux_test = mantoux_test_service._get(**mantoux_test_pk.dict())

    assert mantoux_test == db_mantoux_test


def test_get_invalid(mantoux_test_service, mantoux_test_pk):
    mantoux_test_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        mantoux_test_service._get(**mantoux_test_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_mantoux_tests_by_medcard_num(mantoux_test_service, db_mantoux_test):
    mantoux_test_service.session.query().filter_by().order_by().all.return_value = [db_mantoux_test, db_mantoux_test]

    mantoux_testes = mantoux_test_service.get_mantoux_tests_by_medcard_num(medcard_num=123)

    assert mantoux_testes == [db_mantoux_test, db_mantoux_test]


def test_get_mantoux_test_by_pk(mantoux_test_service, db_mantoux_test, mantoux_test_pk, mocker):
    mocker.patch.object(mantoux_test_service, '_get', return_value=db_mantoux_test)

    mantoux_test = mantoux_test_service.get_mantoux_test_by_pk(mantoux_test_pk)

    assert mantoux_test == db_mantoux_test


def test_add_new_mantoux_test(mantoux_test_service, db_mantoux_test, mocker):
    mantoux_test_create = MantouxTestCreate(**db_mantoux_test.dict())
    
    mantoux_test_service.session.add.return_value = db_mantoux_test
    mock_mantoux_test = mocker.MagicMock(spec=MantouxTestTable)

    mock_add = mocker.patch.object(mantoux_test_service.session, 'add')
    mocker.patch('services.medical_record.mantoux_test.MantouxTest', return_value=mock_mantoux_test)
    mantoux_test = mantoux_test_service.add_new_mantoux_test(mantoux_test_create)

    mock_add.assert_called_once_with(mock_mantoux_test)
    mantoux_test_service.session.commit.assert_called_once()
    
    assert mantoux_test == mock_mantoux_test


def test_update_mantoux_test(mantoux_test_service, db_mantoux_test, mocker):
    mantoux_test_update_data = MantouxTestUpdate(**db_mantoux_test.dict(), prev_check_date=db_mantoux_test.check_date)
    mantoux_test_update_data.check_date = '2024-01-01'
    updated_mantoux_test = db_mantoux_test
    updated_mantoux_test.check_date = mantoux_test_update_data.check_date
    mocker.patch.object(mantoux_test_service, '_get', return_value=db_mantoux_test)

    mantoux_test = mantoux_test_service.update_mantoux_test(mantoux_test_update_data)
    mantoux_test_service.session.commit.assert_called_once()

    assert mantoux_test == updated_mantoux_test


def test_delete_mantoux_test(mantoux_test_service, db_mantoux_test, mantoux_test_pk, mocker):
    mantoux_test = MantouxTestTable(**db_mantoux_test.dict())
    mocker.patch.object(mantoux_test_service, '_get', return_value=mantoux_test)

    mock_delete = mocker.patch.object(mantoux_test_service.session, 'delete')

    mantoux_test_service.delete_mantoux_test(mantoux_test_pk)
    
    mock_delete.asassert_called_once_withs(mantoux_test)
    mantoux_test_service.session.commit.assert_called_once()
