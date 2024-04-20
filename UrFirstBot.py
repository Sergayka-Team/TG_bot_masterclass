import asyncio
import json

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold, hitalic
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    CallbackQuery

with open('./data/config.json') as file:
    config = json.load(file)

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.username}! '
                         f'Очень рад тебя видеть!')


@router.message(F.text == "Как дела?")
async def how_are_u(message: Message):
    await message.answer(
        text='Все хорошо! Спасибо! А у тебя?',
        reply_markup=inline_keyboard()
    )


def inline_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='Хорошо', callback_data='norm'),
            InlineKeyboardButton(text='Плохо', callback_data='ploxo')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


@router.callback_query(lambda callback: callback.data == 'norm')
async def norm(callback: CallbackQuery):
    await callback.answer(cache_time=3)

    await callback.message.answer(
        text='Вот и хорошо!'
    )


@router.callback_query(lambda callback: callback.data == 'ploxo')
async def ploxo(callback: CallbackQuery):
    await callback.answer(
        text='Неправильный ответ!',
        show_alert=True
    )


async def main():
    token = config['BOT_TOKEN']
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
