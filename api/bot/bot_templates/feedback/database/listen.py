import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Task
from database.queries import orm_edit_command_response
from handlers.user import sender


async def task_listening(async_session_factory: AsyncSession, bot):
    async with async_session_factory() as session:
        while True:
            print('New loop (TASK LISTENING)')
            query = select(Task).where(Task.is_done==0)

            tasks = await session.execute(query)
            tasks_res: list[Task] = tasks.scalars().all()
            if tasks_res:
                for task in tasks_res:
                    if task.type == 'sender':
                        await sender(bot, session, task.message)
                        task.is_done = 1
                        await session.commit()

                    elif task.type == 'edit_command':
                        command, new_msg = task.command, task.new_response
                        await orm_edit_command_response(
                            session, command, new_msg
                        )
                        task.is_done = 1
                        await session.commit()

            await asyncio.sleep(10)