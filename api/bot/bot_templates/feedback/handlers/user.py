from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from database.queries import orm_add_command, orm_get_command_reponse, orm_add_user, orm_edit_command_response

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
async def feedback(msg: Message):

    await msg.reply("Твое сообщение отправлено админу!")