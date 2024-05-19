from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.medical_certificate import MedicalCertificateService
from models.medical_record.medical_certificate import MedicalCertificate, MedicalCertificateCreate, MedicalCertificateUpdate, MedicalCertificatePK
from tables import MedicalCertificate as MedicalCertificateTable


@fixture
def medical_certificate_service(mocker):
  session = mocker.Mock()
  return MedicalCertificateService(session=session)


@fixture
def db_medical_certificate():
    return MedicalCertificate(
        medcard_num=123,
        disease='disease',
        cert_date='2023-01-01',
        start_date='2023-01-01',
        end_date='2023-01-05',
        infection_contact=False,
        doctor='doctor'
    )

@fixture
def medical_certificate_pk():
    return MedicalCertificatePK(
        medcard_num=123,
        disease='disease',
        cert_date='2023-01-01'
    )


def test_get_valid(medical_certificate_service, db_medical_certificate, medical_certificate_pk):
    medical_certificate_service.session.query().filter_by().first.return_value = db_medical_certificate
    medical_certificate = medical_certificate_service._get(**medical_certificate_pk.dict())

    assert medical_certificate == db_medical_certificate


def test_get_invalid(medical_certificate_service, medical_certificate_pk):
    medical_certificate_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        medical_certificate_service._get(**medical_certificate_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_medical_certificates_by_medcard_num(medical_certificate_service, db_medical_certificate):
    medical_certificate_service.session.query().filter_by().order_by().all.return_value = [db_medical_certificate, db_medical_certificate]

    medical_certificatees = medical_certificate_service.get_medical_certificates_by_medcard_num(medcard_num=123)

    assert medical_certificatees == [db_medical_certificate, db_medical_certificate]


def test_get_medical_certificate_by_pk(medical_certificate_service, db_medical_certificate, medical_certificate_pk, mocker):
    mocker.patch.object(medical_certificate_service, '_get', return_value=db_medical_certificate)

    medical_certificate = medical_certificate_service.get_medical_certificate_by_pk(medical_certificate_pk)

    assert medical_certificate == db_medical_certificate


def test_add_new_medical_certificate(medical_certificate_service, db_medical_certificate, mocker):
    medical_certificate_create = MedicalCertificateCreate(**db_medical_certificate.dict())
    
    medical_certificate_service.session.add.return_value = db_medical_certificate
    mock_medical_certificate = mocker.MagicMock(spec=MedicalCertificateTable)

    mock_add = mocker.patch.object(medical_certificate_service.session, 'add')
    mocker.patch('services.medical_record.medical_certificate.MedicalCertificate', return_value=mock_medical_certificate)
    medical_certificate = medical_certificate_service.add_new_medical_certificate(medical_certificate_create)

    mock_add.assert_called_once_with(mock_medical_certificate)
    medical_certificate_service.session.commit.assert_called_once()
    
    assert medical_certificate == mock_medical_certificate


def test_update_medical_certificate(medical_certificate_service, db_medical_certificate, mocker):
    medical_certificate_update_data = MedicalCertificateUpdate(**db_medical_certificate.dict(),
                                                               prev_disease=db_medical_certificate.disease,
                                                               prev_cert_date=db_medical_certificate.cert_date
                                      )
    medical_certificate_update_data.disease = 'new disease'
    medical_certificate_update_data.cert_date = '2024-01-01'
    updated_medical_certificate = db_medical_certificate
    updated_medical_certificate.disease = medical_certificate_update_data.disease
    updated_medical_certificate.cert_date = medical_certificate_update_data.cert_date
    mocker.patch.object(medical_certificate_service, '_get', return_value=db_medical_certificate)

    medical_certificate = medical_certificate_service.update_medical_certificate(medical_certificate_update_data)
    medical_certificate_service.session.commit.assert_called_once()

    assert medical_certificate == updated_medical_certificate


def test_delete_medical_certificate(medical_certificate_service, db_medical_certificate, medical_certificate_pk, mocker):
    medical_certificate = MedicalCertificateTable(**db_medical_certificate.dict())
    mocker.patch.object(medical_certificate_service, '_get', return_value=medical_certificate)

    mock_delete = mocker.patch.object(medical_certificate_service.session, 'delete')

    medical_certificate_service.delete_medical_certificate(medical_certificate_pk)
    
    mock_delete.asassert_called_once_withs(medical_certificate)
    medical_certificate_service.session.commit.assert_called_once()
