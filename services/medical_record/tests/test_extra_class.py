from pytest import (
    fixture,
    raises,
)

from fastapi import HTTPException, status
from services.medical_record.extra_class import ExtraClassService
from models.medical_record.extra_class import ExtraClass, ExtraClassCreate, ExtraClassUpdate, ExtraClassPK
from tables import ExtraClass as ExtraClassTable


@fixture
def extra_class_service(mocker):
  session = mocker.Mock()
  return ExtraClassService(session=session)


@fixture
def db_extra_class():
    return ExtraClass(
        medcard_num=1,
        classes_type='Музыка',
        age=2,
        hours_on_week=10
    )

@fixture
def extra_class_pk():
    return ExtraClassPK(
        medcard_num=123,
        classes_type='classes_type',
        age=2
    )


def test_get_valid(extra_class_service, db_extra_class, extra_class_pk):
    extra_class_service.session.query().filter_by().first.return_value = db_extra_class
    extra_class = extra_class_service._get(**extra_class_pk.dict())

    assert extra_class == db_extra_class


def test_get_invalid(extra_class_service, extra_class_pk):
    extra_class_service.session.query().filter_by().first.return_value = None
    with raises(HTTPException) as excp:
        extra_class_service._get(**extra_class_pk.dict())
    assert excp.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_extra_classes_by_medcard_num(extra_class_service, db_extra_class):
    extra_class_service.session.query().filter_by().order_by().all.return_value = [db_extra_class, db_extra_class]

    extra_classes = extra_class_service.get_extra_classes_by_medcard_num(medcard_num=123)

    assert extra_classes == [db_extra_class, db_extra_class]


def test_get_extra_class_by_pk(extra_class_service, db_extra_class, extra_class_pk, mocker):
    mocker.patch.object(extra_class_service, '_get', return_value=db_extra_class)

    extra_class = extra_class_service.get_extra_class_by_pk(extra_class_pk)

    assert extra_class == db_extra_class


def test_add_new_extra_class(extra_class_service, db_extra_class, mocker):
    extra_class_create = ExtraClassCreate(**db_extra_class.dict())
    
    extra_class_service.session.add.return_value = db_extra_class
    mock_extra_class = mocker.MagicMock(spec=ExtraClassTable)

    mock_add = mocker.patch.object(extra_class_service.session, 'add')
    mocker.patch('services.medical_record.extra_class.ExtraClass', return_value=mock_extra_class)
    extra_class = extra_class_service.add_new_extra_class(extra_class_create)

    mock_add.assert_called_once_with(mock_extra_class)
    extra_class_service.session.commit.assert_called_once()
    
    assert extra_class == mock_extra_class


def test_update_extra_class(extra_class_service, db_extra_class, mocker):
    extra_class_update_data = ExtraClassUpdate(**db_extra_class.dict(), prev_classes_type=db_extra_class.classes_type, prev_age=2)
    extra_class_update_data.classes_type = 'new classes_type'
    extra_class_update_data.age = 3
    updated_extra_class = db_extra_class
    updated_extra_class.classes_type = extra_class_update_data.classes_type
    updated_extra_class.age = extra_class_update_data.age

    mocker.patch.object(extra_class_service, '_get', return_value=db_extra_class)

    extra_class = extra_class_service.update_extra_class(extra_class_update_data)
    extra_class_service.session.commit.assert_called_once()

    assert extra_class == updated_extra_class


def test_delete_extra_class(extra_class_service, db_extra_class, extra_class_pk, mocker):
    extra_class = ExtraClassTable(**db_extra_class.dict())
    mocker.patch.object(extra_class_service, '_get', return_value=extra_class)

    mock_delete = mocker.patch.object(extra_class_service.session, 'delete')

    extra_class_service.delete_extra_class(extra_class_pk)
    
    mock_delete.asassert_called_once_withs(extra_class)
    extra_class_service.session.commit.assert_called_once()
