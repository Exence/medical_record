import os
import sys
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    db_host: str = '127.0.0.1'
    db_port: int = 5432
    db_name: str = 'medical_record'
    db_user:str = 'postgres'
    db_password: str = 'postgres'
    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int
    password_salt: str
    # Значение текущей директории для PyInstaller и для обычной среды
    current_path: str = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

templates_path = os.path.join(settings.current_path, "templates")
templates = Jinja2Templates(directory=templates_path)
