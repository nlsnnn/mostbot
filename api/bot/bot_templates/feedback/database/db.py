import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from database.models import Base


bot_path = os.path.dirname(__file__)
db_path = os.path.join(bot_path, 'db.sqlite3')

async_engine = create_async_engine(
    url=f"sqlite+aiosqlite:///{db_path}",
    echo=False
)

async_session_factory = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
