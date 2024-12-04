from sqlalchemy import BigInteger, String, Boolean, ForeignKey, DateTime, text, func, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_session, async_sessionmaker, create_async_engine

from typing import Annotated


int_pk = Annotated[int, mapped_column(primary_key=True)]

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Permission(Base):
    __tablename__ = 'permissions'

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(32))

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(32))
    email_confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_subscribed: Mapped[bool] = mapped_column(Boolean, default=False)
    permission: Mapped[int] = mapped_column(ForeignKey('permissions.id',ondelete='RESTRICT'),default=1)


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int_pk]
    group_name: Mapped[str] = mapped_column(String(8))

class TimeTable(Base):
    __tablename__ = 'timetables'

    id: Mapped[int_pk]
    course: Mapped[int] = mapped_column(nullable=False)
    week: Mapped[DateTime] = mapped_column(Date, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc',now())"))


class Png(Base):
    __tablename__ = 'pngs'

    photo_id: Mapped[int] = mapped_column(primary_key=True)
    timetable_id: Mapped[int] = mapped_column(ForeignKey('timetables.id', ondelete='RESTRICT'))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc',now())"))

class GroupLink(Base):
    __tablename__ = 'grouplinks'

    id: Mapped[int_pk]   
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
