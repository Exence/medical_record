from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.tub_vac import TuberculosisVaccinationService
from models.medical_record.tub_vac import TuberculosisVaccination, TuberculosisVaccinationCreate, TuberculosisVaccinationUpdate, TuberculosisVaccinationPK
from tables import TuberculosisVaccination as TuberculosisVaccinationTable


@fixture
def tuberculosis_vaccination_service(mocker):
  session = mocker.Mock()
  return TuberculosisVaccinationService(session=session)


@fixture
def db_tuberculosis_vaccination():
    return TuberculosisVaccination(
        medcard_num=123,
        vac_date='2023-01-01',
        serial='serial',
        dose=20.5,
        doctor='doctor'
    )

@fixture
def tuberculosis_vaccination_pk():
    return TuberculosisVaccinationPK(
        medcard_num=123,
        vac_date='2023-01-01'
    )


def test_get_valid(tuberculosis_vaccination_service, db_tuberculosis_vaccination, tuberculosis_vaccination_pk):
    tuberculosis_vaccination_service.session.query().filter_by().first.return_value = db_tuberculosis_vaccination
    tuberculosis_vaccination = tuberculosis_vaccination_service._get(**tuberculosis_vaccination_pk.dict())

    assert tuberculosis_vaccination == db_tuberculosis_vaccination


def test_get_invalid(tuberculosis_vaccination_service, tuberculosis_vaccination_pk):
    tuberculosis_vaccination_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        tuberculosis_vaccination_service._get(**tuberculosis_vaccination_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_tuberculosis_vaccinations_by_medcard_num(tuberculosis_vaccination_service, db_tuberculosis_vaccination):
    tuberculosis_vaccination_service.session.query().filter_by().order_by().all.return_value = [db_tuberculosis_vaccination, db_tuberculosis_vaccination]

    tuberculosis_vaccinationes = tuberculosis_vaccination_service.get_tuberculosis_vaccinations_by_medcard_num(medcard_num=123)

    assert tuberculosis_vaccinationes == [db_tuberculosis_vaccination, db_tuberculosis_vaccination]


def test_get_tuberculosis_vaccination_by_pk(tuberculosis_vaccination_service, db_tuberculosis_vaccination, tuberculosis_vaccination_pk, mocker):
    mocker.patch.object(tuberculosis_vaccination_service, '_get', return_value=db_tuberculosis_vaccination)

    tuberculosis_vaccination = tuberculosis_vaccination_service.get_tuberculosis_vaccination_by_pk(tuberculosis_vaccination_pk)

    assert tuberculosis_vaccination == db_tuberculosis_vaccination


def test_add_new_tuberculosis_vaccination(tuberculosis_vaccination_service, db_tuberculosis_vaccination, mocker):
    tuberculosis_vaccination_create = TuberculosisVaccinationCreate(**db_tuberculosis_vaccination.dict())
    
    tuberculosis_vaccination_service.session.add.return_value = db_tuberculosis_vaccination
    mock_tuberculosis_vaccination = mocker.MagicMock(spec=TuberculosisVaccinationTable)

    mock_add = mocker.patch.object(tuberculosis_vaccination_service.session, 'add')
    mocker.patch('services.medical_record.tub_vac.TuberculosisVaccination', return_value=mock_tuberculosis_vaccination)
    tuberculosis_vaccination = tuberculosis_vaccination_service.add_new_tuberculosis_vaccination(tuberculosis_vaccination_create)

    mock_add.assert_called_once_with(mock_tuberculosis_vaccination)
    tuberculosis_vaccination_service.session.commit.assert_called_once()
    
    assert tuberculosis_vaccination == mock_tuberculosis_vaccination


def test_update_tuberculosis_vaccination(tuberculosis_vaccination_service, db_tuberculosis_vaccination, mocker):
    tuberculosis_vaccination_update_data = TuberculosisVaccinationUpdate(**db_tuberculosis_vaccination.dict(),
                                                                         prev_vac_date=db_tuberculosis_vaccination.vac_date)
    tuberculosis_vaccination_update_data.vac_date = '2024-01-01'
    updated_tuberculosis_vaccination = db_tuberculosis_vaccination
    updated_tuberculosis_vaccination.vac_date = tuberculosis_vaccination_update_data.vac_date
    mocker.patch.object(tuberculosis_vaccination_service, '_get', return_value=db_tuberculosis_vaccination)

    tuberculosis_vaccination = tuberculosis_vaccination_service.update_tuberculosis_vaccination(tuberculosis_vaccination_update_data)
    tuberculosis_vaccination_service.session.commit.assert_called_once()

    assert tuberculosis_vaccination == updated_tuberculosis_vaccination


def test_delete_tuberculosis_vaccination(tuberculosis_vaccination_service, db_tuberculosis_vaccination, tuberculosis_vaccination_pk, mocker):
    tuberculosis_vaccination = TuberculosisVaccinationTable(**db_tuberculosis_vaccination.dict())
    mocker.patch.object(tuberculosis_vaccination_service, '_get', return_value=tuberculosis_vaccination)

    mock_delete = mocker.patch.object(tuberculosis_vaccination_service.session, 'delete')

    tuberculosis_vaccination_service.delete_tuberculosis_vaccination(tuberculosis_vaccination_pk)
    
    mock_delete.asassert_called_once_withs(tuberculosis_vaccination)
    tuberculosis_vaccination_service.session.commit.assert_called_once()
