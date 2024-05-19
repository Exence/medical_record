from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.screening import ScreeningService
from models.medical_record.screening import Screening, ScreeningCreate, ScreeningUpdate, ScreeningPK
from tables import Screening as ScreeningTable


@fixture
def screening_service(mocker):
  session = mocker.Mock()
  return ScreeningService(session=session)


@fixture
def db_screening():
    return Screening(
        medcard_num=123,
        examination_date='2023-01-01',
        age=2,
        questionnaire_test='Норма',
        height=150,
        weight=45.5
    )

@fixture
def screening_pk():
    return ScreeningPK(
        medcard_num=123,
        examination_date='2023-01-01'
    )


def test_get_valid(screening_service, db_screening, screening_pk):
    screening_service.session.query().filter_by().first.return_value = db_screening
    screening = screening_service._get(**screening_pk.dict())

    assert screening == db_screening


def test_get_invalid(screening_service, screening_pk):
    screening_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        screening_service._get(**screening_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_screenings_by_medcard_num(screening_service, db_screening):
    screening_service.session.query().filter_by().order_by().all.return_value = [db_screening, db_screening]

    screenings = screening_service.get_screenings_by_medcard_num(medcard_num=123)

    assert screenings == [db_screening, db_screening]


def test_get_screening_by_pk(screening_service, db_screening, screening_pk, mocker):
    mocker.patch.object(screening_service, '_get', return_value=db_screening)

    screening = screening_service.get_screening_by_pk(screening_pk)

    assert screening == db_screening


def test_add_new_screening(screening_service, db_screening, mocker):
    screening_create = ScreeningCreate(**db_screening.dict())
    
    screening_service.session.add.return_value = db_screening
    mock_screening = mocker.MagicMock(spec=ScreeningTable)

    mock_add = mocker.patch.object(screening_service.session, 'add')
    mocker.patch('services.medical_record.screening.Screening', return_value=mock_screening)
    screening = screening_service.add_new_screening(screening_create)

    mock_add.assert_called_once_with(mock_screening)
    screening_service.session.commit.assert_called_once()
    
    assert screening == mock_screening


def test_update_screening(screening_service, db_screening, mocker):
    screening_update_data = ScreeningUpdate(**db_screening.dict(), 
                                            prev_examination_date=db_screening.examination_date)
    screening_update_data.examination_date = '2024-01-01'
    updated_screening = db_screening
    updated_screening.examination_date = screening_update_data.examination_date
    mocker.patch.object(screening_service, '_get', return_value=db_screening)

    screening = screening_service.update_screening(screening_update_data)
    screening_service.session.commit.assert_called_once()

    assert screening == updated_screening


def test_delete_screening(screening_service, db_screening, screening_pk, mocker):
    screening = ScreeningTable(**db_screening.dict())
    mocker.patch.object(screening_service, '_get', return_value=screening)

    mock_delete = mocker.patch.object(screening_service.session, 'delete')

    screening_service.delete_screening(screening_pk)
    
    mock_delete.asassert_called_once_withs(screening)
    screening_service.session.commit.assert_called_once()
