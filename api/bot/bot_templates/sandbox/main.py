import asyncio
import sys
from aiogram import Bot, Dispatcher

from handlers.user import router


async def main_bot(bot_token):
    print('Starting bot (MAIN)')
    bot = Bot(bot_token)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    print(sys.argv)
    token = sys.argv[1]

    try:
        asyncio.run(main_bot(token))
    except KeyboardInterrupt:
        print('exit')