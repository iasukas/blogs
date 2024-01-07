from orjson import dumps, loads
from sanic import Sanic

from core.setting import config
from libs.module import setup_modules
from libs.request import Request


def create_app():
    app = Sanic(
        __name__,
        config=config,
        dumps=dumps,
        loads=loads,
        request_class=Request
    )

    setup_modules(app)

    return app
