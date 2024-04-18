import asyncio

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold, hitalic

from Bot import config
from keyboards.inline_keyboards import get_start_config
from keyboards.reply_keyboard import get_main_menu

router = Router()


@router.message(Command("start"))
async def handler_start_command(message: Message) -> None:
    name = config["PROJECT_NAME"]
    await message.answer(f'Привет, дорогой участник!\n'
                         f'Добро пожаловать на мастер-класс {hitalic(name)}!',
                         reply_markup=ReplyKeyboardRemove())

    await message.answer_sticker(r'CAACAgIAAxkBAAJRN2YgWjx5l-UInM-uzN3Tt62FvIi8AAI2FgACcmugS6XaTV2HP2QpNAQ')

    await asyncio.sleep(2)

    await message.answer('Раз ты пришел сюда, то хочешь создать такого же бота как и я!\n'
                         'Тебе интересно как он сделан?', reply_markup=get_start_config())


@router.message(Command("help"))
async def handler_help_command(message: Message) -> None:
    await message.answer(f'В этом разделе я тебе помогу создать твоего собственного бота!🤓\n'
                         f'Давай с тобой перейдем к @BotFather')


@router.message(Command("test"))
async def handler_test_command(message: Message) -> None:
    await message.answer('Тут мы будем с тобой проверять различные типы данных, '
                         'которые есть в телеграмме!\n'
                         '...а их ооооочень много!..')

    await message.answer('Попробуй отправить какой-то стикер')


@router.message(Command("menu"))
async def handler_menu_command(message: Message) -> None:
    await message.answer(text='Ты вернулся в главное меню!',
                         reply_markup=get_main_menu())
