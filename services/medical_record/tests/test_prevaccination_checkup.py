from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.prevaccination_checkup import PrevaccinationCheckupService
from models.medical_record.prevaccination_checkup import PrevaccinationCheckup, PrevaccinationCheckupCreate, PrevaccinationCheckupUpdate, PrevaccinationCheckupPK
from tables import PrevaccinationCheckup as PrevaccinationCheckupTable


@fixture
def prevaccination_checkup_service(mocker):
  session = mocker.Mock()
  return PrevaccinationCheckupService(session=session)


@fixture
def db_prevaccination_checkup():
    return PrevaccinationCheckup(
        medcard_num=123,
        examination_date='2023-01-01',
        diagnosis='diagnosis',
        report='report',
        doctor='doctor',
        vac_name_id=1
    )

@fixture
def prevaccination_checkup_pk():
    return PrevaccinationCheckupPK(
        medcard_num=123,
        examination_date='2023-01-01'
    )


def test_get_valid(prevaccination_checkup_service, db_prevaccination_checkup, prevaccination_checkup_pk):
    prevaccination_checkup_service.session.query().filter_by().first.return_value = db_prevaccination_checkup
    prevaccination_checkup = prevaccination_checkup_service._get(**prevaccination_checkup_pk.dict())

    assert prevaccination_checkup == db_prevaccination_checkup


def test_get_invalid(prevaccination_checkup_service, prevaccination_checkup_pk):
    prevaccination_checkup_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        prevaccination_checkup_service._get(**prevaccination_checkup_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_prevaccination_checkups_by_medcard_num(prevaccination_checkup_service, db_prevaccination_checkup):
    prevaccination_checkup_service.session.query().filter_by().order_by().all.return_value = [db_prevaccination_checkup, db_prevaccination_checkup]

    prevaccination_checkupes = prevaccination_checkup_service.get_prevaccination_checkups_by_medcard_num(medcard_num=123)

    assert prevaccination_checkupes == [db_prevaccination_checkup, db_prevaccination_checkup]


def test_get_prevaccination_checkup_by_pk(prevaccination_checkup_service, db_prevaccination_checkup, prevaccination_checkup_pk, mocker):
    mocker.patch.object(prevaccination_checkup_service, '_get', return_value=db_prevaccination_checkup)

    prevaccination_checkup = prevaccination_checkup_service.get_prevaccination_checkup_by_pk(prevaccination_checkup_pk)

    assert prevaccination_checkup == db_prevaccination_checkup


def test_add_new_prevaccination_checkup(prevaccination_checkup_service, db_prevaccination_checkup, mocker):
    prevaccination_checkup_create = PrevaccinationCheckupCreate(**db_prevaccination_checkup.dict())
    
    prevaccination_checkup_service.session.add.return_value = db_prevaccination_checkup
    mock_prevaccination_checkup = mocker.MagicMock(spec=PrevaccinationCheckupTable)

    mock_add = mocker.patch.object(prevaccination_checkup_service.session, 'add')
    mocker.patch('services.medical_record.prevaccination_checkup.PrevaccinationCheckup', return_value=mock_prevaccination_checkup)
    prevaccination_checkup = prevaccination_checkup_service.add_new_prevaccination_checkup(prevaccination_checkup_create)

    mock_add.assert_called_once_with(mock_prevaccination_checkup)
    prevaccination_checkup_service.session.commit.assert_called_once()
    
    assert prevaccination_checkup == mock_prevaccination_checkup


def test_update_prevaccination_checkup(prevaccination_checkup_service, db_prevaccination_checkup, mocker):
    prevaccination_checkup_update_data = PrevaccinationCheckupUpdate(**db_prevaccination_checkup.dict(),
                                                                     prev_examination_date=db_prevaccination_checkup.examination_date
                                      )
    prevaccination_checkup_update_data.examination_date = '2024-01-01'
    updated_prevaccination_checkup = db_prevaccination_checkup
    updated_prevaccination_checkup.examination_date = prevaccination_checkup_update_data.examination_date
    mocker.patch.object(prevaccination_checkup_service, '_get', return_value=db_prevaccination_checkup)

    prevaccination_checkup = prevaccination_checkup_service.update_prevaccination_checkup(prevaccination_checkup_update_data)
    prevaccination_checkup_service.session.commit.assert_called_once()

    assert prevaccination_checkup == updated_prevaccination_checkup


def test_delete_prevaccination_checkup(prevaccination_checkup_service, db_prevaccination_checkup, prevaccination_checkup_pk, mocker):
    prevaccination_checkup = PrevaccinationCheckupTable(**db_prevaccination_checkup.dict())
    mocker.patch.object(prevaccination_checkup_service, '_get', return_value=prevaccination_checkup)

    mock_delete = mocker.patch.object(prevaccination_checkup_service.session, 'delete')

    prevaccination_checkup_service.delete_prevaccination_checkup(prevaccination_checkup_pk)
    
    mock_delete.asassert_called_once_withs(prevaccination_checkup)
    prevaccination_checkup_service.session.commit.assert_called_once()
