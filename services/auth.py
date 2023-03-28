from datetime import (
    datetime, 
    timedelta,
)
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from jose import (
    jwt,
    JWTError,
)
from passlib.hash import bcrypt
from pydantic import ValidationError

from settings import settings
from database import (
    get_connection,
    execute_read_query,
)
from models.auth import (
    Token,
    User,
    UserCreate,
) 
from typing import Any


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth')

def _serialization_user(user_data: list) -> User:
    return User (
        login = user_data[0],
        surname = user_data[1],
        name = user_data[2],
        patronymic = user_data[3],
        password_hash = user_data[4],
        access_level = user_data[5],
        kindergarten_num = user_data[6])


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(token)

class AuthService():
    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:        
        return bcrypt.verify(password + settings.password_salt, password_hash)

    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.encrypt(password + settings.password_salt)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')
        
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None
        
        return user

    @classmethod
    def create_token(cls, user_data: User) -> Token:
        now = datetime.utcnow()

        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(settings.jwt_expiration),
            'sub': str(user_data.login),
            'user': user_data.dict(),
        }

        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )

        return Token(access_token=token)

    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def register_new_user(self, user_data: UserCreate) -> Token:
        user_data.password_hash = self.get_hashed_password(user_data.password_hash)
        user = [(user_data.login, user_data.surname, user_data.name, user_data.patronymic, user_data.password_hash, user_data.access_level, user_data.kindergarten_num)]
        insert_query = (
        f"INSERT INTO users (login, surname, name, patronymic, password_hash, access_level, kindergarten_num) VALUES %s"
        )
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        cursor.execute(insert_query, user)
        return self.create_token(_serialization_user(user[0]))


    def authenticate_user(self, login: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect login or password',
            headers={
                'WWW-Authenticate': 'bearer'
            },
        )
        select_user = f"SELECT * FROM users WHERE login='{login}'"
        query_user = execute_read_query(self.connection, select_user)
        if not query_user:
            raise exception
        
        user = _serialization_user(query_user[0])
        
        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
