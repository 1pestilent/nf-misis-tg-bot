from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database.models import *

import os
from dotenv import load_dotenv

class DataBase():
    def __init__(self):
        self.connect = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        self.async_engine = create_async_engine(self.connect)
        self.Session = async_sessionmaker(bind=self.async_engine, class_= AsyncSession)

    async def create_db(self):
        async with self.async_engine.begin() as connect:
            await connect.run_sync(Base.metadata.create_all)

    async def add_groups(self, groups):
        async with self.Session() as session:
            async with session.begin():
                for group_name in groups:
                    group = Group(group_name=group_name)
                    session.add(group)
            await session.commit()

    async def get_group_id(self, group_name):
        async with self.Session() as session:
            async with session.begin(): 
                result = await session.execute(select(Group).filter(Group.group_name == group_name))
                group = result.scalars().first()
                return group.id if group else None

    async def get_user(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(User).where(User.tg_id == user_id))
        return result.scalar()
    
    async def get_user_id(self, telegram_id):
        async with self.Session() as request:
            result = await request.execute(select(User.id).where(User.tg_id == telegram_id))
        return result.scalar_one_or_none()
            
    async def add_user(self, telegram_id, username, useremail):
        async with self.Session() as session:
            try:
                new_user = User(
                    tg_id=telegram_id,
                    name=username,
                    email=useremail,
                    is_subscribed=False
                )
                session.add(new_user)
                await session.commit()
            except Exception as e:
                print(f'Ошибка при добавлении пользователя: {e}')

    
    async def create_group_link(self, user, group):
        async with self.Session() as request:
            new_link = GroupLink(
                user_id = user,
                group_id = group)
            request.add(new_link)
            await request.commit()
    