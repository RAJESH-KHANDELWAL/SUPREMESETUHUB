"""
Global Business Ecosystem
Database Connection
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.supreme.supreme_ecosystem.supreme_business_ecosystem.global_business_ecosystem.config.settings import settings


engine = create_engine(
    settings.DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
    if settings.DATABASE_URL.startswith("sqlite")
    else {}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
