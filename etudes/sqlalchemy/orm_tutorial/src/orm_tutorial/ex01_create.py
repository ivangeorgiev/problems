from sqlalchemy import create_engine

from orm_tutorial.models import Base

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)
