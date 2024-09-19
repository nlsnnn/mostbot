from sqlalchemy import select, update, insert, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import User, UserCommand


async def orm_add_user(
        session: AsyncSession,
        tg_id: int,
        name: str | None = None
):
    query = select(User).where(User.tg_id==tg_id)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            User(tg_id=tg_id, name=name)
        )
        await session.commit()


async def orm_get_command_reponse(
        session: AsyncSession,
        command: str
):
    query = select(UserCommand.response).where(UserCommand.command==command)
    res = await session.execute(query)
    return res.scalar()


async def orm_add_command(
        session: AsyncSession,
        command: str,
        response: str
):
    query = select(UserCommand).where(UserCommand.command==command)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            UserCommand(command=command, response=response)
        )
        await session.commit()


async def orm_edit_command_response(
        session: AsyncSession,
        command: str,
        new_response: str
):
    query = (update(UserCommand).where(UserCommand.command==command).values(response=new_response))
    await session.execute(query)
    await session.commit()