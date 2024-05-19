from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.gg_injection import GammaGlobulinInjectionService
from models.medical_record.gg_injection import GammaGlobulinInjection, GammaGlobulinInjectionCreate, GammaGlobulinInjectionUpdate, GammaGlobulinInjectionPK
from tables import GammaGlobulinInjection as GammaGlobulinInjectionTable


@fixture
def gamma_globulin_injection_service(mocker):
  session = mocker.Mock()
  return GammaGlobulinInjectionService(session=session)


@fixture
def db_gamma_globulin_injection():
    return GammaGlobulinInjection(
        medcard_num=123,
        vac_date='2023-01-01',
        reason='reason',
        serial='serial',
        dose='0.5',
        reaction='Немедленная',
        doctor='doctor'
    )

@fixture
def gamma_globulin_injection_pk():
    return GammaGlobulinInjectionPK(
        medcard_num=123,
        vac_date='2023-01-01'
    )


def test_get_valid(gamma_globulin_injection_service, db_gamma_globulin_injection, gamma_globulin_injection_pk):
    gamma_globulin_injection_service.session.query().filter_by().first.return_value = db_gamma_globulin_injection
    gamma_globulin_injection = gamma_globulin_injection_service._get(**gamma_globulin_injection_pk.dict())

    assert gamma_globulin_injection == db_gamma_globulin_injection


def test_get_invalid(gamma_globulin_injection_service, gamma_globulin_injection_pk):
    gamma_globulin_injection_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        gamma_globulin_injection_service._get(**gamma_globulin_injection_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_gamma_globulin_injections_by_medcard_num(gamma_globulin_injection_service, db_gamma_globulin_injection):
    gamma_globulin_injection_service.session.query().filter_by().order_by().all.return_value = [db_gamma_globulin_injection, db_gamma_globulin_injection]

    gamma_globulin_injectiones = gamma_globulin_injection_service.get_gamma_globulin_injections_by_medcard_num(medcard_num=123)

    assert gamma_globulin_injectiones == [db_gamma_globulin_injection, db_gamma_globulin_injection]


def test_get_gamma_globulin_injection_by_pk(gamma_globulin_injection_service, db_gamma_globulin_injection, gamma_globulin_injection_pk, mocker):
    mocker.patch.object(gamma_globulin_injection_service, '_get', return_value=db_gamma_globulin_injection)

    gamma_globulin_injection = gamma_globulin_injection_service.get_gamma_globulin_injection_by_pk(gamma_globulin_injection_pk)

    assert gamma_globulin_injection == db_gamma_globulin_injection


def test_add_new_gamma_globulin_injection(gamma_globulin_injection_service, db_gamma_globulin_injection, mocker):
    gamma_globulin_injection_create = GammaGlobulinInjectionCreate(**db_gamma_globulin_injection.dict())
    
    gamma_globulin_injection_service.session.add.return_value = db_gamma_globulin_injection
    mock_gamma_globulin_injection = mocker.MagicMock(spec=GammaGlobulinInjectionTable)

    mock_add = mocker.patch.object(gamma_globulin_injection_service.session, 'add')
    mocker.patch('services.medical_record.gg_injection.GammaGlobulinInjection', return_value=mock_gamma_globulin_injection)
    gamma_globulin_injection = gamma_globulin_injection_service.add_new_gamma_globulin_injection(gamma_globulin_injection_create)

    mock_add.assert_called_once_with(mock_gamma_globulin_injection)
    gamma_globulin_injection_service.session.commit.assert_called_once()
    
    assert gamma_globulin_injection == mock_gamma_globulin_injection


def test_update_gamma_globulin_injection(gamma_globulin_injection_service, db_gamma_globulin_injection, mocker):
    gamma_globulin_injection_update_data = GammaGlobulinInjectionUpdate(**db_gamma_globulin_injection.dict(), prev_vac_date=db_gamma_globulin_injection.vac_date)
    gamma_globulin_injection_update_data.vac_date = '2024-01-01'
    updated_gamma_globulin_injection = db_gamma_globulin_injection
    updated_gamma_globulin_injection.vac_date = gamma_globulin_injection_update_data.vac_date
    mocker.patch.object(gamma_globulin_injection_service, '_get', return_value=db_gamma_globulin_injection)

    gamma_globulin_injection = gamma_globulin_injection_service.update_gamma_globulin_injection(gamma_globulin_injection_update_data)
    gamma_globulin_injection_service.session.commit.assert_called_once()

    assert gamma_globulin_injection == updated_gamma_globulin_injection


def test_delete_gamma_globulin_injection(gamma_globulin_injection_service, db_gamma_globulin_injection, gamma_globulin_injection_pk, mocker):
    gamma_globulin_injection = GammaGlobulinInjectionTable(**db_gamma_globulin_injection.dict())
    mocker.patch.object(gamma_globulin_injection_service, '_get', return_value=gamma_globulin_injection)

    mock_delete = mocker.patch.object(gamma_globulin_injection_service.session, 'delete')

    gamma_globulin_injection_service.delete_gamma_globulin_injection(gamma_globulin_injection_pk)
    
    mock_delete.asassert_called_once_withs(gamma_globulin_injection)
    gamma_globulin_injection_service.session.commit.assert_called_once()
