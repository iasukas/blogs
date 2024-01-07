from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.setting import config

engine = create_async_engine(
    config.SQLALCHEMY_DATABASE_URI,
    echo=True,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
