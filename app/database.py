from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import get_settings
from functools import lru_cache

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@lru_cache
def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    init_db()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()