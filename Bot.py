import asyncio
import logging
import json
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

from handlers import different_types, commands, callbacks

with open('./data/config.json') as file:
    config = json.load(file)


async def main() -> None:
    token = config['BOT_TOKEN']
    # session = AiohttpSession(proxy=config["PROXY"])

    # bot = Bot(token=token, session=session, parse_mode=ParseMode.HTML)
    bot = Bot(token=token, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_routers(commands.router,
                       callbacks.router,
                       different_types.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
