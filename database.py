from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings as s


engine = create_engine(
    f"sqlite:///medical_record.db"
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
