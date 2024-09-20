import asyncio
import os
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    url=f"sqlite+aiosqlite:///db.sqlite3",
    echo=False
)

async_session_factory = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

async def listening(token):
    async with async_engine.connect() as session:
        while True:
            print('New loop')
            query = f"""SELECT is_active FROM bot_bot WHERE token = '{token}'"""
            is_active = await session.execute(text(query))
            is_active_res = is_active.scalar()
            print(f'{is_active_res=}')

            if not is_active_res:
                print('OK im EXIT')
                os._exit(0)

            await asyncio.sleep(10)
