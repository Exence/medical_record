from pytest import (
    fixture,
    raises,
)
from datetime import datetime, timedelta, UTC
from fastapi import HTTPException, status
from jose import jwt

from auth import AuthService
from settings import settings
from user import UserService
from models.user import User
from pydantic import BaseModel


class PasswordData(BaseModel):
    valid_password: str
    invalid_password: str
    valid_password_hash: str


@fixture
def auth_service(mocker):
    session = mocker.Mock()
    user_service = UserService(session=session)
    return AuthService(session=session, user_service=user_service)

@fixture
def password_data(auth_service):
    valid_password = 'password'
    invalid_password = 'invalid_password'
    valid_password_hash = auth_service.user_service.get_hashed_password(password=valid_password) 
    return PasswordData(valid_password=valid_password,
                        invalid_password=invalid_password,
                        valid_password_hash=valid_password_hash)

@fixture 
def user_data(password_data):
    return {
            'password_hash': password_data.valid_password_hash,
            'kindergarten_num': 1,
            'kindergarten_name': 'kindergarten_name',
            'surname': 'surname',
            'name': 'name',
            'patronymic': 'patronymic'
        }

@fixture
def db_user(user_data):
    return User(**user_data)


def test_verify_password(auth_service, password_data):
    assert auth_service.verify_password(password_data.valid_password, password_data.valid_password_hash) is True
    assert auth_service.verify_password('invalid_password', password_data.valid_password_hash) is False


def test_validate_token_valid(auth_service, mocker, user_data, db_user):
    mocker.patch('auth.jwt.decode', return_value={'user': user_data})
    user = auth_service.validate_token('token')
    assert user == db_user
    

def test_validate_token_invalid(auth_service):
    with raises(HTTPException) as excp:
        auth_service.validate_token('incorrect token')
    assert excp.value.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_token(auth_service, user_data, db_user):
    expected_exp = datetime.now(UTC) + timedelta(settings.jwt_expiration)
    token = auth_service.create_token(db_user)
    decoded_token = jwt.decode(token.access_token, settings.jwt_secret,
                               algorithms=[settings.jwt_algorithm])
    assert decoded_token['sub'] == str(db_user.kindergarten_num)
    assert decoded_token['user'] == user_data
    assert 'iat' in decoded_token
    assert 'nbf' in decoded_token
    assert decoded_token['exp'] >= int(expected_exp.timestamp())


def test_authenticate_user_new_user(auth_service, mocker, db_user):
    auth_service.session.query().first.return_value = None
    mock_user_service = mocker.Mock()
    mock_user_service.add_new_user.return_value = db_user
    
    auth_service.user_service = mock_user_service

    token = auth_service.authenticate_user('password')
    user = auth_service.validate_token(token.access_token)
    
    assert user == db_user


def test_authenticate_user_existing_user(auth_service, mocker, db_user):
    auth_service.session.query().first.return_value = db_user

    token = auth_service.authenticate_user('password')
    user = auth_service.validate_token(token.access_token)
    
    assert user == db_user


def test_authenticate_user_invalid_password(auth_service, mocker, db_user):
    with raises(HTTPException) as excp:
        auth_service.session.query().first.return_value = db_user
        
        auth_service.authenticate_user('invalid_password')
    assert excp.value.status_code == status.HTTP_401_UNAUTHORIZED
