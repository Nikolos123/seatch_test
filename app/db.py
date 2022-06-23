"""Модуль для описания соединений с базой данных."""
from typing import Iterator

from app.config import Settings, get_settings
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


def get_db_session(settings: Settings = Depends(get_settings)) -> Iterator[Session]:
    """Возвращает соединений с основной базой данных проекта."""
    engine = create_engine(url=settings.PERSISTENCE_DSN)
    session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    session = session_local()
    try:
        yield session
    finally:
        session.close()
