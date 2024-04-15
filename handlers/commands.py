from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hitalic

from Bot import config

router = Router()


@router.message(Command("start"))
async def handler_start_command(message: Message) -> None:
    name = config["PROJECT_NAME"]
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!'
                         f'Доброе пожаловать на мастер-класс {hitalic(name)}')


@router.message(Command("help"))
async def handler_help_command(message: Message) -> None:
    await message.answer(f'Хуй я тебе а не помогу')


@router.message(Command("test"))
async def handler_test_command(message: Message) -> None:
    await message.answer('Тест пройден')


