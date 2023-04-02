from typing import Any

from database import (
      execute_read_query_first,
      )
from models.user import (
    User,
)


def serialization_user(connection: Any, user_data: tuple) -> User:
            query = f"SELECT name FROM kindergartens WHERE number = {user_data[6]}"
            kindergarten_name = execute_read_query_first(connection, query)[0]
            
            return User (
                login = user_data[0],
                surname = user_data[1],
                name = user_data[2],
                patronymic = user_data[3],
                password_hash = user_data[4],
                access_level = user_data[5],
                kindergarten_num = user_data[6],
                kindergarten_name = kindergarten_name
            )
