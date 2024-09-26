import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handlers.user import router as user_router
from database.db import async_main, async_session_factory
from database.listen import task_listening
from middlewares.db import DataBaseSession
from database.global_db import listening


async def main(bot_token):
    print('Started feedback bot')

    await async_main()

    bot = Bot(bot_token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(user_router)

    dp.update.middleware(DataBaseSession(session_pool=async_session_factory))

    dp['bot_token'] = bot_token

    loop = asyncio.get_event_loop()
    loop.create_task(listening(bot_token))
    loop.create_task(task_listening(async_session_factory, bot))

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == '__main__':
    token = sys.argv[1]

    try:
        asyncio.run(main(token))
    except KeyboardInterrupt:
        print('KB Exit')
    except Exception as e:
        print('Exception exit')
        print(e)