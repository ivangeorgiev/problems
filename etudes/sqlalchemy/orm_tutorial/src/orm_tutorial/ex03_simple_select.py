from sqlalchemy import select

from orm_tutorial.db import engine, get_session
from orm_tutorial.models import User

engine.echo = True

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

with get_session() as session:
    for user in session.scalars(stmt):
        print(user)
