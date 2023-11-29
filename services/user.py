from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from passlib.hash import bcrypt
from typing import Any

from models.user import (
        CreateUserForm,
        UserCreate
)

from services.auth import AuthService
from services.serialization import SerializationService

from settings import settings

from tables import Child, Kindergarten, User


def check_user_access_to_medcard(user: User, medcard_num: int, session: Session = Depends(get_session)) -> bool:
        if user.access_level == 'user':
            medcard = (
                session
                .query(Child)
                .filter_by(medcard_num=medcard_num)
                .first()
            )
            return medcard.kindergarten_num == user.kindergarten_num
        return True

class UserService():
    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.encrypt(password + settings.password_salt)
    
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def create_new_user(self, form_data: CreateUserForm, access_token: str) -> None:
        current_user = AuthService.validate_token(access_token)
        if not current_user.access_level in ['admin', 'db_admin']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        try:
            password_hash = self.get_hashed_password(form_data.password)
            form_data.login = form_data.login.lower()

            kindergarten_num = 0

            if not form_data.access_level in ['admin', 'db_admin']:
                kindergarten = (
                    self.session
                    .query(Kindergarten)
                    .filter_by(name=form_data.kindergarten_name)
                    .first()
                )
                kindergarten_num = kindergarten.number

            user = UserCreate()
            for field, value in form_data:
                if field != 'kindergarten_name' or field != 'password':
                    setattr(user, field, value)
            user.kindergarten_num = kindergarten_num
            user.password_hash = password_hash

            self.session.add(user)
            self.session.commit()
            return True
        except:
            return False

    def get_all_users(self) -> list[User]:
        return (
            self.session
            .query(User)
            .all()
        )
