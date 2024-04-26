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
    User as UserModel,
    UserCreate,
    UserPK,
    UserUpdate
)

from settings import settings

from tables import User


def check_user_access_to_medcard(user: User, medcard_num: int, session: Session = Depends(get_session)) -> bool:
    
    return True


class UserService():
    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.encrypt(password + settings.password_salt)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, kindergarten_num: int) -> User:
        return (self.session
        .query(User)
        .filter_by(kindergarten_num=kindergarten_num)
        .first()
        )
    
    def add_new_user(self):
        
        DEFAULT_USER = User(
            kindergarten_num=1,
            kindergarten_name='Детский сад №1',
            surname='Иванова',
            name='Ирина',
            patronymic='Игоревна',
            password_hash=self.get_hashed_password('1111')
        )
        self.session.add(DEFAULT_USER)
        self.session.commit()
        return DEFAULT_USER

    def get_all_users(self) -> list[User]:
        return (
            self.session
            .query(User)
            .all()
        )
    
    def update_user(self, current_data: UserModel, updated_data: UserModel) -> UserModel:
        user = self._get(current_data.kindergarten_num)
        for key, value in updated_data.dict().items():
            setattr(user, key, value)
        self.session.commit()
        user_dict = {column.name: getattr(user, column.name) for column in user.__table__.columns}
        return UserModel(**user_dict)
    
    def change_password(self, user: UserModel, new_password: str) -> UserModel:
        new_password_hash = self.get_hashed_password(new_password)
        db_user = self._get(user.kindergarten_num)
        db_user.password_hash = new_password_hash
        user.password_hash = new_password_hash
        self.session.commit()
        return user

