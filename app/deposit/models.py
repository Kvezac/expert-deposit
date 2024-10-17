from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Deposit(Base):
    __tablename__: str = "deposits"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    periods: Mapped[int]
    amount: Mapped[int]
    rate: Mapped[int]
