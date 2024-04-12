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
    UserCreate
)

from services.auth import AuthService

from settings import settings

from tables import Child, Kindergarten, User


def check_user_access_to_medcard(user: User, medcard_num: int, session: Session = Depends(get_session)) -> bool:
    
    return True


class UserService():
    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.encrypt(password + settings.password_salt)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        

    def get_all_users(self) -> list[User]:
        return (
            self.session
            .query(User)
            .all()
        )
