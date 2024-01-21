from datetime import (
    datetime,
    timedelta,
)
from fastapi import (
    Cookie,
    Depends,
    HTTPException,
    status,
)
from jose import (
    jwt,
    JWTError,
)
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from settings import settings
from database import get_session

from models.auth import Token
from models.user import User as UserModel
from tables import User
from services.oauth2_scheme import OAuth2PasswordBearerWithCookie


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl='/sign-in')


def get_current_user(access_token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(access_token)


class AuthService():
    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        return bcrypt.verify(password + settings.password_salt, password_hash)

    @classmethod
    def validate_token(cls, token: str) -> UserModel:
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
            user = UserModel.parse_obj(user_data)
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

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def authenticate_user(self, login: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect login or password',
            headers={
                'WWW-Authenticate': 'bearer'
            },
        )
        user = (
            self.session
            .query(User)
            .filter_by(login=login.lower())
            .first()
        )

        user = UserModel(**user.__dict__)

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
