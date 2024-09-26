from aiogram import Bot, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from database.queries import orm_add_command, orm_get_command_reponse, orm_add_user, orm_edit_command_response, orm_get_users
from services import send_message

router = Router()


@router.message(CommandStart())
async def start(msg: Message, session: AsyncSession):
    user = msg.from_user

    await orm_add_user(
        session,
        user.id,
        user.full_name
    )

    await orm_add_command(
        session,
        'start',
        '<b>Привет! Я бот помощник.</b>\n\nНапиши сообщение и я отправлю его админу 😉'
    )

    text = await orm_get_command_reponse(
        session,
        'start'
    )

    await msg.answer(text)


@router.message()
async def feedback(msg: Message, bot_token):
    r = send_message(msg.text, msg.from_user.full_name, msg.chat.id, bot_token)

    if r:
        await msg.reply("Твое сообщение отправлено админу!")
    else:
        await msg.reply("Произошла ошибка! Сообщение не было доставлено")


async def sender(bot: Bot, session: AsyncSession, message: str):
    users = await orm_get_users(session)

    for user in users:
        await bot.send_message(user, message)
        print('Sended')
