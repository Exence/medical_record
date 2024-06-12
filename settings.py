import os
import sys
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings


prod = getattr(sys, 'frozen', False)

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    db_host: str = '127.0.0.1'
    db_port: int = 5432
    db_name: str = 'medical_record'
    db_user:str = 'postgres'
    db_password: str = 'postgres'
    jwt_secret: str = '1a4bccfd79f46d1bfd356c2b08e75a0f9f2aff06e451a00148ef065b761aac92'
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = '3600'
    password_salt: str = '$2b$12$KGJpwa5KtHjiiM/bs0h2Ge'
    # Значение текущей директории для PyInstaller и для обычной среды
    current_path: str = sys._MEIPASS if prod else os.path.dirname(__file__)


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

templates_path = os.path.join(settings.current_path, "templates")
templates = Jinja2Templates(directory=templates_path)
