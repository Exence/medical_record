from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.past_illness import PastIllnessService
from models.medical_record.past_illness import PastIllness, PastIllnessCreate, PastIllnessUpdate, PastIllnessPK
from tables import PastIllness as PastIllnessTable


@fixture
def past_illness_service(mocker):
  session = mocker.Mock()
  return PastIllnessService(session=session)


@fixture
def db_past_illness():
    return PastIllness(
        medcard_num=123,
        start_date='2023-01-01',
        diagnosis='diagnosis',
        end_date='2023-03-01'
    )

@fixture
def past_illness_pk():
    return PastIllnessPK(
        medcard_num=123,
        start_date='2023-01-01',
        diagnosis='diagnosis'
    )


def test_get_valid(past_illness_service, db_past_illness, past_illness_pk):
    past_illness_service.session.query().filter_by().first.return_value = db_past_illness
    past_illness = past_illness_service._get(**past_illness_pk.dict())

    assert past_illness == db_past_illness


def test_get_invalid(past_illness_service, past_illness_pk):
    past_illness_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        past_illness_service._get(**past_illness_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_past_illnesses_by_medcard_num(past_illness_service, db_past_illness):
    past_illness_service.session.query().filter_by().order_by().all.return_value = [db_past_illness, db_past_illness]

    past_illnesses = past_illness_service.get_past_illnesses_by_medcard_num(medcard_num=123)

    assert past_illnesses == [db_past_illness, db_past_illness]


def test_get_past_illness_by_pk(past_illness_service, db_past_illness, past_illness_pk, mocker):
    mocker.patch.object(past_illness_service, '_get', return_value=db_past_illness)

    past_illness = past_illness_service.get_past_illness_by_pk(past_illness_pk)

    assert past_illness == db_past_illness


def test_add_new_past_illness(past_illness_service, db_past_illness, mocker):
    past_illness_create = PastIllnessCreate(**db_past_illness.dict())
    
    past_illness_service.session.add.return_value = db_past_illness
    mock_past_illness = mocker.MagicMock(spec=PastIllnessTable)

    mock_add = mocker.patch.object(past_illness_service.session, 'add')
    mocker.patch('services.medical_record.past_illness.PastIllness', return_value=mock_past_illness)
    past_illness = past_illness_service.add_new_past_illness(past_illness_create)

    mock_add.assert_called_once_with(mock_past_illness)
    past_illness_service.session.commit.assert_called_once()
    
    assert past_illness == mock_past_illness


def test_update_past_illness(past_illness_service, db_past_illness, mocker):
    past_illness_update_data = PastIllnessUpdate(**db_past_illness.dict(),
                                                 prev_diagnosis=db_past_illness.diagnosis,
                                                 prev_start_date=db_past_illness.start_date
                                      )
    past_illness_update_data.diagnosis = 'new diagnosis'
    past_illness_update_data.start_date = '2024-01-01'
    updated_past_illness = db_past_illness
    updated_past_illness.diagnosis = past_illness_update_data.diagnosis
    updated_past_illness.start_date = past_illness_update_data.start_date
    mocker.patch.object(past_illness_service, '_get', return_value=db_past_illness)

    past_illness = past_illness_service.update_past_illness(past_illness_update_data)
    past_illness_service.session.commit.assert_called_once()

    assert past_illness == updated_past_illness


def test_delete_past_illness(past_illness_service, db_past_illness, past_illness_pk, mocker):
    past_illness = PastIllnessTable(**db_past_illness.dict())
    mocker.patch.object(past_illness_service, '_get', return_value=past_illness)

    mock_delete = mocker.patch.object(past_illness_service.session, 'delete')

    past_illness_service.delete_past_illness(past_illness_pk)
    
    mock_delete.asassert_called_once_withs(past_illness)
    past_illness_service.session.commit.assert_called_once()
