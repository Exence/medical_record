from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings as s


engine = create_engine(
    f"postgresql://{s.db_user}:{s.db_password}@{s.db_host}:{s.db_port}/{s.db_name}"
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
