from fastapi import (
    Depends,
    HTTPException,
)
from passlib.hash import bcrypt
from typing import Any

from models.user import (
        User,
        CreateUserForm,
)

from services.auth import AuthService
from services.serialization import SerializationService

from settings import settings
from database import (
    get_connection,
    execute_data_query,
    execute_read_query_first,
    execute_read_query_all,
)


class UserService():
    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.encrypt(password + settings.password_salt)
    
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection
    
    def create_new_user(self, form_data: CreateUserForm, access_token: str) -> None:
        current_user = AuthService.validate_token(access_token)
        if not current_user.access_level in ['admin', 'db_admin']:
            raise HTTPException(
                status_code=403, detail="Forbidden"
            )
        try:
            form_data.password = self.get_hashed_password(form_data.password)
            form_data.login = form_data.login.lower()

            if form_data.access_level in ['admin', 'db_admin']:
                kindergarten_num = 0
            else:
                query = f"SELECT number FROM kindergartens WHERE name = '{form_data.kindergarten_name}'"
                kindergarten_num = execute_read_query_first(self.connection, query)[0]

            user = [(form_data.login, form_data.surname, form_data.name, form_data.patronymic, form_data.password, form_data.access_level, kindergarten_num)]
            print(user)
            insert_query = (
                f"INSERT INTO users (login, surname, name, patronymic, password_hash, access_level, kindergarten_num) VALUES %s"
            )
            execute_data_query(self.connection, insert_query, user)
            self.connection.commit()
            return True
        except:
            return False

    def get_all_users(self) -> list:
        query = f"SELECT * FROM users"
        selected_users = execute_read_query_all(self.connection, query)
        users = []
        for user in selected_users:
            users.append(SerializationService.serialization_user(self.connection, user))
        return users
