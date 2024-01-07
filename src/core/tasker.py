from celery import Celery

from core.setting import TaskerConfig

app = Celery(
    "tasker",
    broker="redis:",
    backend="redis:"
)

app.config_from_object(TaskerConfig)
