from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from orm_tutorial import db
from orm_tutorial.models import Address, User

async_engine = create_async_engine("sqlite+aiosqlite://", echo=True)


async def create_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.create_all)


async def populate_data() -> None:
    async with AsyncSession(async_engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        await session.commit()


async def main() -> None:
    await create_tables()
    await populate_data()
    async with AsyncSession(async_engine) as session:
        stmt = select(User)
        for user in await session.scalars(stmt):
            print(user)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
