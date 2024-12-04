from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from app.schedule.handler.handler import get_schedule
from app.schedule.downloader import timecalc

from app.database.requests import *

import asyncio

from app.core import dictionary
admin_router = Router()


@admin_router.message(Command('download'))
async def download_current_week(message: Message, bot: Bot):
    week = timecalc.get_current_week()
    first_day_week = timecalc.get_first_day_current_week()
    for course in range(1,2):
        photo_id = []
        pngs = get_schedule(course, week)
        await bot.send_message(message.from_user.id, f'Расписание за {week} для {course}-ого курса\n{first_day_week}\n\n Список загружаемых png: {pngs}')
        for png in pngs:
            photo = FSInputFile(png)
            photo_message = await bot.send_photo(message.from_user.id, photo=photo)
            photo_id.append(photo_message.photo[-1].file_id)
        db = DataBase()
        await db.add_timetable(course = course, week = first_day_week)
        tt_id = await db.get_timetable_id()
        await db.add_pngs(ids = pngs, timetable_id=tt_id)
