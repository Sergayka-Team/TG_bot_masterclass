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

###############################################################################

















###############################################################################
async def main():
    token = config['BOT_TOKEN']
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
