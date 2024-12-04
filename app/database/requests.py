from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database.models import *

import os
from time import sleep
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

    async def add_permissions(self, permissions):
        async with self.Session() as session:
            async with session.begin():
                for permission in permissions:
                    level = Permission(name=permission)
                    session.add(level)
            await session.commit()

    async def get_group_id(self, group_name):
        async with self.Session() as session:
            async with session.begin(): 
                result = await session.execute(select(Group).filter(Group.group_name == group_name))
                group = result.scalars().first()
                return group.id if group else None

    async def get_group_names_by_user_id(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(Group.group_name).join(GroupLink, Group.id == GroupLink.group_id).where(GroupLink.user_id == user_id))
        return result.scalar_one_or_none()

    async def get_permission_by_user_id(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(Permission.name).join(User, User.permission == Permission.id).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_user(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(User).where(User.id == user_id))
        return result.scalar()
    
    async def get_user_email(self, user_id):
        async with self.Session() as request:
            result = await request.execute(select(User.email).where(User.id == user_id))
        return result.scalar_one_or_none()
            
    async def add_user(self, telegram_id, username, useremail):
        async with self.Session() as session:
            try:
                new_user = User(
                    id=telegram_id,
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

    async def update_user_email(self, user, new_mail):
        async with self.Session() as request:
            result = await request.execute(select(User).where(User.id == user))
            user = result.scalar_one_or_none()

            if User.email == new_mail:
                return False
            else:
                user.email = new_mail
                user.email_confirmed = False
                await request.commit()
                return True
    
    async def update_email_confirm(self, user):
        async with self.Session() as request:
            result = await request.execute(select(User).where(User.id == user))
            user = result.scalar_one_or_none()

            user.email_confirmed = True
            await request.commit()

    async def check_email_subscribe(self, user):
            async with self.Session() as request:
                result = await request.execute(select(User.is_subscribed).where(User.id == user))
                subscribe = result.scalar_one_or_none()

                if subscribe:
                    return True
                else:
                    return False

    async def update_email_subscribe(self, user):
            async with self.Session() as request:
                result = await request.execute(select(User).where(User.id == user))
                user = result.scalar_one_or_none()
                
                if not user.is_subscribed:
                    user.is_subscribed = True
                else:
                    user.is_subscribed = False
            
                await request.commit()

    async def check_email_confirm(self, user):
        async with self.Session() as request:
            result = await request.execute(select(User.email_confirmed).where(User.id == user))
            confirm = result.scalar_one_or_none()

            if confirm:
                return True
            else:
                return False
    
    async def update_user_group(self, user, group_name):
        async with self.Session() as request:
            result = await request.execute(select(GroupLink).where(GroupLink.user_id == user))
            link = result.scalar_one_or_none()

            if link is None:
                return False
            else:
                await request.delete(link)
                group = await self.get_group_id(group_name)
                new_link = GroupLink(user_id = user, group_id = group)
                request.add(new_link)
                await request.commit()
                return True

    async def add_timetable(self, course, week):
        async with self.Session() as request:
            new_timetable = TimeTable(course=course, week=week)
            request.add(new_timetable)
            await request.commit()
            return True

    async def get_timetable_id(self):
        async with self.Session() as request:
            result = await request.execute(select(TimeTable.id).order_by(TimeTable.created_at.desc()).limit(1))
            return result.scalar_one_or_none()

    async def add_pngs(self, ids, timetable_id):
        async with self.Session() as request:
            try:
                for id in ids:
                    png = Png(photo_id=id,timetable_id=timetable_id)
                    request.add(png)
                await request.commit()
            except Exception as e:
                await request.rollback()



