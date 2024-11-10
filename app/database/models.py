from sqlalchemy import BigInteger, String, Boolean, ForeignKey, DateTime, text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_session, async_sessionmaker, create_async_engine

from typing import Annotated

from dotenv import load_dotenv
import os


engine = create_async_engine(f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
async_session = async_sessionmaker(engine)

int_pk = Annotated[int, mapped_column(primary_key=True)]

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk] 
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(32))
    is_subscribed: Mapped[bool] = mapped_column(Boolean, default=False)


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int_pk]
    group_name: Mapped[str] = mapped_column(String(8))


class TimeTable(Base):
    __tablename__ = 'timetables'

    id: Mapped[int_pk]   
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))
    pdf_path: Mapped[str] = mapped_column(String(256)) 
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc',now())"))


class GroupLink(Base):
    __tablename__ = 'grouplinks'

    id: Mapped[int_pk]   
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))
