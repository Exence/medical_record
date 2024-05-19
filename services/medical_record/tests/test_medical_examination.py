from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.medical_examination import MedicalExaminationService
from models.medical_record.medical_examination import MedicalExamination, MedicalExaminationCreate, MedicalExaminationUpdate, MedicalExaminationPK
from tables import MedicalExamination as MedicalExaminationTable


@fixture
def medical_examination_service(mocker):
  session = mocker.Mock()
  return MedicalExaminationService(session=session)


@fixture
def db_medical_examination():
    return MedicalExamination(
        medcard_num=123,
        period='Перед школой',
        examination_date='2023-01-01',
        height=150,
        weight=45.5,
        health_group='I',
        sport_group='Основная'
    )

@fixture
def medical_examination_pk():
    return MedicalExaminationPK(
        medcard_num=123,
        period='Перед школой'
    )


def test_get_valid(medical_examination_service, db_medical_examination, medical_examination_pk):
    medical_examination_service.session.query().filter_by().first.return_value = db_medical_examination
    medical_examination = medical_examination_service._get(**medical_examination_pk.dict())

    assert medical_examination == db_medical_examination


def test_get_invalid(medical_examination_service, medical_examination_pk):
    medical_examination_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        medical_examination_service._get(**medical_examination_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_medical_examinations_by_medcard_num(medical_examination_service, db_medical_examination):
    medical_examination_service.session.query().filter_by().order_by().all.return_value = [db_medical_examination, db_medical_examination]

    medical_examinationes = medical_examination_service.get_medical_examinations_by_medcard_num(medcard_num=123)

    assert medical_examinationes == [db_medical_examination, db_medical_examination]


def test_get_medical_examination_by_pk(medical_examination_service, db_medical_examination, medical_examination_pk, mocker):
    mocker.patch.object(medical_examination_service, '_get', return_value=db_medical_examination)

    medical_examination = medical_examination_service.get_medical_examination_by_pk(medical_examination_pk)

    assert medical_examination == db_medical_examination


def test_add_new_medical_examination(medical_examination_service, db_medical_examination, mocker):
    medical_examination_create = MedicalExaminationCreate(**db_medical_examination.dict())
    
    medical_examination_service.session.add.return_value = db_medical_examination
    mock_medical_examination = mocker.MagicMock(spec=MedicalExaminationTable)

    mock_add = mocker.patch.object(medical_examination_service.session, 'add')
    mocker.patch('services.medical_record.medical_examination.MedicalExamination', return_value=mock_medical_examination)
    medical_examination = medical_examination_service.add_new_medical_examination(medical_examination_create)

    mock_add.assert_called_once_with(mock_medical_examination)
    medical_examination_service.session.commit.assert_called_once()
    
    assert medical_examination == mock_medical_examination


def test_update_medical_examination(medical_examination_service, db_medical_examination, mocker):
    medical_examination_update_data = MedicalExaminationUpdate(**db_medical_examination.dict(),
                                                               prev_period='Перед школой'
                                      )
    medical_examination_update_data.examination_date = '2024-01-01'
    updated_medical_examination = db_medical_examination
    updated_medical_examination.examination_date = medical_examination_update_data.examination_date
    mocker.patch.object(medical_examination_service, '_get', return_value=db_medical_examination)

    medical_examination = medical_examination_service.update_medical_examination(medical_examination_update_data)
    medical_examination_service.session.commit.assert_called_once()

    assert medical_examination == updated_medical_examination


def test_delete_medical_examination(medical_examination_service, db_medical_examination, medical_examination_pk, mocker):
    medical_examination = MedicalExaminationTable(**db_medical_examination.dict())
    mocker.patch.object(medical_examination_service, '_get', return_value=medical_examination)

    mock_delete = mocker.patch.object(medical_examination_service.session, 'delete')

    medical_examination_service.delete_medical_examination(medical_examination_pk)
    
    mock_delete.asassert_called_once_withs(medical_examination)
    medical_examination_service.session.commit.assert_called_once()
