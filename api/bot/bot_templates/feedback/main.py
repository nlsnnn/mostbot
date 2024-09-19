import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handlers.user import router as user_router
from database.db import async_main, async_session_factory
from middlewares.db import DataBaseSession


async def main(bot_token):
    print('Started feedback bot')

    await async_main()

    bot = Bot(bot_token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(user_router)

    dp.update.middleware(DataBaseSession(session_pool=async_session_factory))

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == '__main__':
    token = sys.argv[1]

    try:
        asyncio.run(main(token))
    except:
        print('Exiiiiit')