from sqlalchemy.ext.asyncio import AsyncSession

from db.base import Base


async def init_db(session: AsyncSession) -> None:
    async with session.begin() as conn:
        await conn.run_sync(Base.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )
