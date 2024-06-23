from os import path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlite3 import Connection as SQLite3Connection

from settings import settings as s


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        print('turning on foreign keys ...')
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON;')
        cursor.close()

current_dir = path.dirname(path.abspath(__file__))
db_path = path.join(current_dir, "medical_record.db")
engine = create_engine(
    f"sqlite:///{db_path}"
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
