from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.DATABASE_URL)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)

session = Session()
