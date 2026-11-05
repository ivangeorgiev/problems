from sqlalchemy.orm import Session

from orm_tutorial import ex02_create_objects  # noqa
from orm_tutorial.ex01_create import engine
from orm_tutorial.models import Base


def get_session() -> Session:
    return Session(engine)


__all__ = [
    "Base",
    "engine",
    "get_session",
]
