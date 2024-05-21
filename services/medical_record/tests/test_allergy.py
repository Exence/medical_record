from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.allergy import AllergyService
from models.medical_record.allergy import Allergy, AllergyCreate, AllergyUpdate, AllergyPK
from tables import Allergy as AllergyTable


@fixture
def allergy_service(mocker):
  session = mocker.Mock()
  return AllergyService(session=session)


@fixture
def db_allergy():
    return Allergy(
        medcard_num=1,
        allergen='allergen',
        allergy_type='Вакцинальная',
        start_age=2,
        reaction_type='Немедленная',
        diagnosis_date='2023-01-01'
    )


@fixture
def allergy_pk():
    return AllergyPK(
        medcard_num=123,
        allergen='allergen'
    )


def test_get_valid(allergy_service, db_allergy, allergy_pk):
    allergy_service.session.query().filter_by().first.return_value = db_allergy
    allergy = allergy_service._get(**allergy_pk.dict())

    assert allergy == db_allergy


def test_get_invalid(allergy_service, allergy_pk):
    allergy_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        allergy_service._get(**allergy_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_allergies_by_medcard_num(allergy_service, db_allergy):
    allergy_service.session.query().filter_by().order_by().all.return_value = [db_allergy, db_allergy]

    allergies = allergy_service.get_allergies_by_medcard_num(medcard_num=123)

    assert allergies == [db_allergy, db_allergy]


def test_get_allergy_by_pk(allergy_service, db_allergy, allergy_pk, mocker):
    mocker.patch.object(allergy_service, '_get', return_value=db_allergy)

    allergy = allergy_service.get_allergy_by_pk(allergy_pk)

    assert allergy == db_allergy

def test_add_new_allergy(allergy_service, db_allergy, mocker):
    allergy_create = AllergyCreate(**db_allergy.dict())
    
    allergy_service.session.add.return_value = db_allergy
    mock_allergy = mocker.MagicMock(spec=AllergyTable)

    mock_add = mocker.patch.object(allergy_service.session, 'add')
    mocker.patch('services.medical_record.allergy.Allergy', return_value=mock_allergy)
    allergy = allergy_service.add_new_allergy(allergy_create)

    mock_add.assert_called_once_with(mock_allergy)
    allergy_service.session.commit.assert_called_once()
    
    assert allergy == mock_allergy


def test_update_allergy(allergy_service, db_allergy, mocker):
    allergy_update_data = AllergyUpdate(**db_allergy.dict(), prev_allergen=db_allergy.allergen)
    allergy_update_data.allergen = 'new allergen'
    updated_allergy = db_allergy
    updated_allergy.allergen = allergy_update_data.allergen
    mocker.patch.object(allergy_service, '_get', return_value=db_allergy)

    allergy = allergy_service.update_allergy(allergy_update_data)
    allergy_service.session.commit.assert_called_once()

    assert allergy == updated_allergy


def test_delete_allergy(allergy_service, db_allergy, allergy_pk, mocker):
    allergy = AllergyTable(**db_allergy.dict())
    mocker.patch.object(allergy_service, '_get', return_value=allergy)

    mock_delete = mocker.patch.object(allergy_service.session, 'delete')

    allergy_service.delete_allergy(allergy_pk)
    
    mock_delete.asassert_called_once_withs(allergy)
    allergy_service.session.commit.assert_called_once()
