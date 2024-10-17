from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)

session = Session()
