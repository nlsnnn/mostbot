from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from database.queries import orm_get_command_reponse, orm_add_command


class ResponseExists(BaseFilter):
    async def __call__(self, msg: Message, session: AsyncSession) -> Any:
        text = await orm_get_command_reponse(
            session,
            'start'
        )

        if not text:
            await orm_add_command(
                session,
                'start',
                "<b>Привет! Я бот помощник.</b>\n\nНапиши сообщение и я отправлю его админу 😉"
            )