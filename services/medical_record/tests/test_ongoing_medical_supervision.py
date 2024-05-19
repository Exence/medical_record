from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.ongoing_medical_supervision import OngoingMedicalSupervisionService
from models.medical_record.ongoing_medical_supervision import OngoingMedicalSupervision, OngoingMedicalSupervisionCreate, OngoingMedicalSupervisionUpdate, OngoingMedicalSupervisionPK
from tables import OngoingMedicalSupervision as OngoingMedicalSupervisionTable


@fixture
def ongoing_medical_supervision_service(mocker):
  session = mocker.Mock()
  return OngoingMedicalSupervisionService(session=session)


@fixture
def db_ongoing_medical_supervision():
    return OngoingMedicalSupervision(
        medcard_num=123,
        examination_date='2023-01-01',
        examination_data='examination_data',
        diagnosis='diagnosis',
        doctor='dictor'
    )

@fixture
def ongoing_medical_supervision_pk():
    return OngoingMedicalSupervisionPK(
        medcard_num=123,
        examination_date='2023-01-01'
    )


def test_get_valid(ongoing_medical_supervision_service, db_ongoing_medical_supervision, ongoing_medical_supervision_pk):
    ongoing_medical_supervision_service.session.query().filter_by().first.return_value = db_ongoing_medical_supervision
    ongoing_medical_supervision = ongoing_medical_supervision_service._get(**ongoing_medical_supervision_pk.dict())

    assert ongoing_medical_supervision == db_ongoing_medical_supervision


def test_get_invalid(ongoing_medical_supervision_service, ongoing_medical_supervision_pk):
    ongoing_medical_supervision_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        ongoing_medical_supervision_service._get(**ongoing_medical_supervision_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_ongoing_medical_supervisions_by_medcard_num(ongoing_medical_supervision_service, db_ongoing_medical_supervision):
    ongoing_medical_supervision_service.session.query().filter_by().order_by().all.return_value = [db_ongoing_medical_supervision, db_ongoing_medical_supervision]

    ongoing_medical_supervisiones = ongoing_medical_supervision_service.get_ongoing_medical_supervisions_by_medcard_num(medcard_num=123)

    assert ongoing_medical_supervisiones == [db_ongoing_medical_supervision, db_ongoing_medical_supervision]


def test_get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision_service, db_ongoing_medical_supervision, ongoing_medical_supervision_pk, mocker):
    mocker.patch.object(ongoing_medical_supervision_service, '_get', return_value=db_ongoing_medical_supervision)

    ongoing_medical_supervision = ongoing_medical_supervision_service.get_ongoing_medical_supervision_by_pk(ongoing_medical_supervision_pk)

    assert ongoing_medical_supervision == db_ongoing_medical_supervision


def test_add_new_ongoing_medical_supervision(ongoing_medical_supervision_service, db_ongoing_medical_supervision, mocker):
    ongoing_medical_supervision_create = OngoingMedicalSupervisionCreate(**db_ongoing_medical_supervision.dict())
    
    ongoing_medical_supervision_service.session.add.return_value = db_ongoing_medical_supervision
    mock_ongoing_medical_supervision = mocker.MagicMock(spec=OngoingMedicalSupervisionTable)

    mock_add = mocker.patch.object(ongoing_medical_supervision_service.session, 'add')
    mocker.patch('services.medical_record.ongoing_medical_supervision.OngoingMedicalSupervision', return_value=mock_ongoing_medical_supervision)
    ongoing_medical_supervision = ongoing_medical_supervision_service.add_new_ongoing_medical_supervision(ongoing_medical_supervision_create)

    mock_add.assert_called_once_with(mock_ongoing_medical_supervision)
    ongoing_medical_supervision_service.session.commit.assert_called_once()
    
    assert ongoing_medical_supervision == mock_ongoing_medical_supervision


def test_update_ongoing_medical_supervision(ongoing_medical_supervision_service, db_ongoing_medical_supervision, mocker):
    ongoing_medical_supervision_update_data = OngoingMedicalSupervisionUpdate(**db_ongoing_medical_supervision.dict(),
                                                                              prev_examination_date=db_ongoing_medical_supervision.examination_date
                                      )
    ongoing_medical_supervision_update_data.examination_date = '2024-01-01'
    updated_ongoing_medical_supervision = db_ongoing_medical_supervision
    updated_ongoing_medical_supervision.examination_date = ongoing_medical_supervision_update_data.examination_date
    mocker.patch.object(ongoing_medical_supervision_service, '_get', return_value=db_ongoing_medical_supervision)

    ongoing_medical_supervision = ongoing_medical_supervision_service.update_ongoing_medical_supervision(ongoing_medical_supervision_update_data)
    ongoing_medical_supervision_service.session.commit.assert_called_once()

    assert ongoing_medical_supervision == updated_ongoing_medical_supervision


def test_delete_ongoing_medical_supervision(ongoing_medical_supervision_service, db_ongoing_medical_supervision, ongoing_medical_supervision_pk, mocker):
    ongoing_medical_supervision = OngoingMedicalSupervisionTable(**db_ongoing_medical_supervision.dict())
    mocker.patch.object(ongoing_medical_supervision_service, '_get', return_value=ongoing_medical_supervision)

    mock_delete = mocker.patch.object(ongoing_medical_supervision_service.session, 'delete')

    ongoing_medical_supervision_service.delete_ongoing_medical_supervision(ongoing_medical_supervision_pk)
    
    mock_delete.asassert_called_once_withs(ongoing_medical_supervision)
    ongoing_medical_supervision_service.session.commit.assert_called_once()
