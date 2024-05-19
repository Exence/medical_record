from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.oral_sanation import OralSanationService
from models.medical_record.oral_sanation import OralSanation, OralSanationCreate, OralSanationUpdate, OralSanationPK
from tables import OralSanation as OralSanationTable


@fixture
def oral_sanation_service(mocker):
  session = mocker.Mock()
  return OralSanationService(session=session)


@fixture
def db_oral_sanation():
    return OralSanation(
        medcard_num=123,
        sanation_date='2023-01-01',
        dental_result='dental_result',
        sanation_result='sanation_result'
    )

@fixture
def oral_sanation_pk():
    return OralSanationPK(
        medcard_num=123,
        sanation_date='2023-01-01'
    )


def test_get_valid(oral_sanation_service, db_oral_sanation, oral_sanation_pk):
    oral_sanation_service.session.query().filter_by().first.return_value = db_oral_sanation
    oral_sanation = oral_sanation_service._get(**oral_sanation_pk.dict())

    assert oral_sanation == db_oral_sanation


def test_get_invalid(oral_sanation_service, oral_sanation_pk):
    oral_sanation_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        oral_sanation_service._get(**oral_sanation_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_oral_sanations_by_medcard_num(oral_sanation_service, db_oral_sanation):
    oral_sanation_service.session.query().filter_by().order_by().all.return_value = [db_oral_sanation, db_oral_sanation]

    oral_sanationes = oral_sanation_service.get_oral_sanations_by_medcard_num(medcard_num=123)

    assert oral_sanationes == [db_oral_sanation, db_oral_sanation]


def test_get_oral_sanation_by_pk(oral_sanation_service, db_oral_sanation, oral_sanation_pk, mocker):
    mocker.patch.object(oral_sanation_service, '_get', return_value=db_oral_sanation)

    oral_sanation = oral_sanation_service.get_oral_sanation_by_pk(oral_sanation_pk)

    assert oral_sanation == db_oral_sanation


def test_add_new_oral_sanation(oral_sanation_service, db_oral_sanation, mocker):
    oral_sanation_create = OralSanationCreate(**db_oral_sanation.dict())
    
    oral_sanation_service.session.add.return_value = db_oral_sanation
    mock_oral_sanation = mocker.MagicMock(spec=OralSanationTable)

    mock_add = mocker.patch.object(oral_sanation_service.session, 'add')
    mocker.patch('services.medical_record.oral_sanation.OralSanation', return_value=mock_oral_sanation)
    oral_sanation = oral_sanation_service.add_new_oral_sanation(oral_sanation_create)

    mock_add.assert_called_once_with(mock_oral_sanation)
    oral_sanation_service.session.commit.assert_called_once()
    
    assert oral_sanation == mock_oral_sanation


def test_update_oral_sanation(oral_sanation_service, db_oral_sanation, mocker):
    oral_sanation_update_data = OralSanationUpdate(**db_oral_sanation.dict(),
                                                   prev_sanation_date=db_oral_sanation.sanation_date
                                      )
    oral_sanation_update_data.sanation_date = '2024-01-01'
    updated_oral_sanation = db_oral_sanation
    updated_oral_sanation.sanation_date = oral_sanation_update_data.sanation_date
    mocker.patch.object(oral_sanation_service, '_get', return_value=db_oral_sanation)

    oral_sanation = oral_sanation_service.update_oral_sanation(oral_sanation_update_data)
    oral_sanation_service.session.commit.assert_called_once()

    assert oral_sanation == updated_oral_sanation


def test_delete_oral_sanation(oral_sanation_service, db_oral_sanation, oral_sanation_pk, mocker):
    oral_sanation = OralSanationTable(**db_oral_sanation.dict())
    mocker.patch.object(oral_sanation_service, '_get', return_value=oral_sanation)

    mock_delete = mocker.patch.object(oral_sanation_service.session, 'delete')

    oral_sanation_service.delete_oral_sanation(oral_sanation_pk)
    
    mock_delete.asassert_called_once_withs(oral_sanation)
    oral_sanation_service.session.commit.assert_called_once()
