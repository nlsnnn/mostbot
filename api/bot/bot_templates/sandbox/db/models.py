from sqlalchemy import BigInteger, DateTime, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(150), nullable=True)


class UserCommand(Base):
    __tablename__ = 'command'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    command: Mapped[str] = mapped_column(String(20))
    response: Mapped[Text] = mapped_column(Text, nullable=True)


class UserMessage(Base):
    pass