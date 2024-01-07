from sanic import Sanic, Request
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import async_session

app = Sanic.get_app()


def get_db_session(request: Request) -> AsyncSession:
    return request.app.ctx.session


@app.before_server_start
async def setup_db(_app: Sanic, _):
    _app.ctx.session = async_session()
    _app.ext.add_dependency(AsyncSession, get_db_session)
