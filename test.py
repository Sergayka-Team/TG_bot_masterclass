import asyncio

# import executor
from aiogram import Bot, Router, Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold, italic
from aiogram.utils import executor
from aiogram.dispatcher import dispatcher
from aiogram.enums import ParseMode

import json
import logging
import sys

with open('./data/config.json') as file:
    config = json.load(file)

# bot = Bot(token=config['BOT_TOKEN'], parse_mode=ParseMode.HTML)
# bot = Bot(token=config['BOT_TOKEN'])
router = Router()
bot = Bot(token=config['BOT_TOKEN'])
dp = Dispatcher()
dp.include_router(router)


@router.message(commands=['start'])
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!'
                         f'Доброе пожаловать на мастер-класс {italic("Создай своего ТГ-бота")}')


# @router.message(commands=['help'])
# async def command_help_handler(message: Message) -> None:
#     await message.answer(f'')
    # pass


# async def main():
#     bot = Bot(token=config['BOT_TOKEN'], parse_mode=ParseMode.HTML)
#     await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # await dp.start_polling(bot)
    executor.start_polling(bot, skip_updates=True)
    # asyncio.run(main())
