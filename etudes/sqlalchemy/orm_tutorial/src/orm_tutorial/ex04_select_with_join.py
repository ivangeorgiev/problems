from sqlalchemy import select

from orm_tutorial.db import engine, get_session
from orm_tutorial.models import Address, User

engine.echo = False

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)

with get_session() as session:
    sandy_address = session.scalars(stmt).one()
    print(sandy_address)

print("----- Using Scalars")
stmt1 = select(User).join(Address)
with get_session() as session:
    for user in session.scalars(stmt1):
        print(user)

print("----- Using Execute")
stmt1 = select(User).join(Address)
with get_session() as session:
    for (user,) in session.execute(stmt1):
        print(user)

print("----- Using Query")
with get_session() as session:
    for user in session.query(User).join(Address):
        print(user)
