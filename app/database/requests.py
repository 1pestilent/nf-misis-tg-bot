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


    async def get_user(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(User).where(User.tg_id == user_id))
        return result.scalar()

    