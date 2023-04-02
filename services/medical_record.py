from pprint import pprint
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
from services.serialization import serialization_user

from settings import settings
from database import (
    get_connection,
    execute_insert_query,
    execute_read_query_first,
    execute_read_query_all,
)

class MedicalRecordService():
    def __init__(self, connection: Any = Depends(get_connection)):
        self.connection = connection

    def create_new_medcard(self, form_data, access_token):
        pprint(form_data)

    
