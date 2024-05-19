from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.vaccination import VaccinationService
from models.medical_record.vaccination import Vaccination, VaccinationCreate, VaccinationUpdate, VaccinationPK
from tables import Vaccination as VaccinationTable


@fixture
def vaccination_service(mocker):
  session = mocker.Mock()
  return VaccinationService(session=session)


@fixture
def db_vaccination():
    return Vaccination(
        medcard_num=123,
        vac_name_id=1,
        vac_type='Вакцинация I',
        vac_date='2023-01-01',
        serial='serial',
        dose=20.5,
        introduction_method='introduction_method',
        reaction='Немедленная',
        doctor='doctor'
    )

@fixture
def vaccination_pk():
    return VaccinationPK(
        medcard_num=123,
        vac_name_id=1,
        vac_type='Вакцинация I'
    )


def test_get_valid(vaccination_service, db_vaccination, vaccination_pk):
    vaccination_service.session.query().filter_by().first.return_value = db_vaccination
    vaccination = vaccination_service._get(**vaccination_pk.dict())

    assert vaccination == db_vaccination


def test_get_invalid(vaccination_service, vaccination_pk):
    vaccination_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        vaccination_service._get(**vaccination_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_vaccinations_by_medcard_num(vaccination_service, db_vaccination):
    vaccination_service.session.query().filter_by().order_by().all.return_value = [db_vaccination, db_vaccination]

    vaccinations = vaccination_service.get_vaccinations_by_medcard_num(medcard_num=123)

    assert vaccinations == [db_vaccination, db_vaccination]


def test_get_vaccination_by_pk(vaccination_service, db_vaccination, vaccination_pk, mocker):
    mocker.patch.object(vaccination_service, '_get', return_value=db_vaccination)

    vaccination = vaccination_service.get_vaccination_by_pk(vaccination_pk)

    assert vaccination == db_vaccination


def test_add_new_vaccination(vaccination_service, db_vaccination, mocker):
    vaccination_create = VaccinationCreate(**db_vaccination.dict())
    
    vaccination_service.session.add.return_value = db_vaccination
    mock_vaccination = mocker.MagicMock(spec=VaccinationTable)

    mock_add = mocker.patch.object(vaccination_service.session, 'add')
    mocker.patch('services.medical_record.vaccination.Vaccination', return_value=mock_vaccination)
    vaccination = vaccination_service.add_new_vaccination(vaccination_create)

    mock_add.assert_called_once_with(mock_vaccination)
    vaccination_service.session.commit.assert_called_once()
    
    assert vaccination == mock_vaccination


def test_update_vaccination(vaccination_service, db_vaccination, mocker):
    vaccination_update_data = VaccinationUpdate(**db_vaccination.dict(), 
                                                prev_vac_name_id=db_vaccination.vac_name_id,
                                                prev_vac_type=db_vaccination.vac_type)
    vaccination_update_data.vac_name_id = 2
    vaccination_update_data.vac_type='Вакцинация II'
    updated_vaccination = db_vaccination
    updated_vaccination.vac_name_id = vaccination_update_data.vac_name_id
    updated_vaccination.vac_type = vaccination_update_data.vac_type
    mocker.patch.object(vaccination_service, '_get', return_value=db_vaccination)

    vaccination = vaccination_service.update_vaccination(vaccination_update_data)
    vaccination_service.session.commit.assert_called_once()

    assert vaccination == updated_vaccination


def test_delete_vaccination(vaccination_service, db_vaccination, vaccination_pk, mocker):
    vaccination = VaccinationTable(**db_vaccination.dict())
    mocker.patch.object(vaccination_service, '_get', return_value=vaccination)

    mock_delete = mocker.patch.object(vaccination_service.session, 'delete')

    vaccination_service.delete_vaccination(vaccination_pk)
    
    mock_delete.asassert_called_once_withs(vaccination)
    vaccination_service.session.commit.assert_called_once()
