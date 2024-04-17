import asyncio

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold, hitalic

from Bot import config
from keyboards.inline_keyboards import get_start_config

router = Router()


@router.message(Command("start"))
async def handler_start_command(message: Message) -> None:
    name = config["PROJECT_NAME"]
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!\n'
                         f'Добро пожаловать на мастер-класс {hitalic(name)}!',
                         reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await message.answer('Раз ты пришел сюда, то хочешь создать такого же бота как и я!\n'
                         'Тебе интересно как он сделан?', reply_markup=get_start_config())


@router.message(Command("help"))
async def handler_help_command(message: Message) -> None:
    await message.answer(f'Хуй я тебе а не помогу')


@router.message(Command("test"))
async def handler_test_command(message: Message) -> None:
    await message.answer('Тест пройден')


