from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.spa_treatment import SpaTreatmentService
from models.medical_record.spa_treatment import SpaTreatment, SpaTreatmentCreate, SpaTreatmentUpdate, SpaTreatmentPK
from tables import SpaTreatment as SpaTreatmentTable


@fixture
def spa_treatment_service(mocker):
  session = mocker.Mock()
  return SpaTreatmentService(session=session)


@fixture
def db_spa_treatment():
    return SpaTreatment(
        medcard_num=123,
        start_date='2023-01-01',
        end_date='2023-03-01',
        diagnosis='diagnosis',
        founding_specialization='founding_specialization',
        climatic_zone='climatic_zone'
    )

@fixture
def spa_treatment_pk():
    return SpaTreatmentPK(
        medcard_num=123,
        start_date='2023-01-01'
    )


def test_get_valid(spa_treatment_service, db_spa_treatment, spa_treatment_pk):
    spa_treatment_service.session.query().filter_by().first.return_value = db_spa_treatment
    spa_treatment = spa_treatment_service._get(**spa_treatment_pk.dict())

    assert spa_treatment == db_spa_treatment


def test_get_invalid(spa_treatment_service, spa_treatment_pk):
    spa_treatment_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        spa_treatment_service._get(**spa_treatment_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_spa_treatments_by_medcard_num(spa_treatment_service, db_spa_treatment):
    spa_treatment_service.session.query().filter_by().order_by().all.return_value = [db_spa_treatment, db_spa_treatment]

    spa_treatments = spa_treatment_service.get_spa_treatments_by_medcard_num(medcard_num=123)

    assert spa_treatments == [db_spa_treatment, db_spa_treatment]


def test_get_spa_treatment_by_pk(spa_treatment_service, db_spa_treatment, spa_treatment_pk, mocker):
    mocker.patch.object(spa_treatment_service, '_get', return_value=db_spa_treatment)

    spa_treatment = spa_treatment_service.get_spa_treatment_by_pk(spa_treatment_pk)

    assert spa_treatment == db_spa_treatment


def test_add_new_spa_treatment(spa_treatment_service, db_spa_treatment, mocker):
    spa_treatment_create = SpaTreatmentCreate(**db_spa_treatment.dict())
    
    spa_treatment_service.session.add.return_value = db_spa_treatment
    mock_spa_treatment = mocker.MagicMock(spec=SpaTreatmentTable)

    mock_add = mocker.patch.object(spa_treatment_service.session, 'add')
    mocker.patch('services.medical_record.spa_treatment.SpaTreatment', return_value=mock_spa_treatment)
    spa_treatment = spa_treatment_service.add_new_spa_treatment(spa_treatment_create)

    mock_add.assert_called_once_with(mock_spa_treatment)
    spa_treatment_service.session.commit.assert_called_once()
    
    assert spa_treatment == mock_spa_treatment


def test_update_spa_treatment(spa_treatment_service, db_spa_treatment, mocker):
    spa_treatment_update_data = SpaTreatmentUpdate(**db_spa_treatment.dict(), 
                                                   prev_start_date=db_spa_treatment.start_date
                                                   )
    spa_treatment_update_data.start_date = '2024-01-01'
    updated_spa_treatment = db_spa_treatment
    updated_spa_treatment.start_date = spa_treatment_update_data.start_date
    mocker.patch.object(spa_treatment_service, '_get', return_value=db_spa_treatment)

    spa_treatment = spa_treatment_service.update_spa_treatment(spa_treatment_update_data)
    spa_treatment_service.session.commit.assert_called_once()

    assert spa_treatment == updated_spa_treatment


def test_delete_spa_treatment(spa_treatment_service, db_spa_treatment, spa_treatment_pk, mocker):
    spa_treatment = SpaTreatmentTable(**db_spa_treatment.dict())
    mocker.patch.object(spa_treatment_service, '_get', return_value=spa_treatment)

    mock_delete = mocker.patch.object(spa_treatment_service.session, 'delete')

    spa_treatment_service.delete_spa_treatment(spa_treatment_pk)
    
    mock_delete.asassert_called_once_withs(spa_treatment)
    spa_treatment_service.session.commit.assert_called_once()
