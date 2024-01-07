import secrets

from sanic.config import Config as _Config


class Config(_Config):
    LOCAL: bool = True
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = secrets.token_urlsafe(64)

    MODULE_NAMES: tuple[str, ...] = (
        "app.category",
        "app.client",
        "app.comment",
        "app.group",
        "app.log",
        "app.permission",
        "app.post",
        "app.tag",
        "app.user",
        "di.session",
        "middleware.redirect",
        "middleware.request_context",
    )

    SQLALCHEMY_DATABASE_URI = "postgresql+asyncpg://postgres:123456@127.0.0.1:5432/blogs"


class TaskerConfig:
    enable_utc: bool = True
    timezone: str = "Asia/Shanghai"


config = Config()
