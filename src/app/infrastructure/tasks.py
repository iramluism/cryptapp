from celery import Celery
from infrastructure.setup import setup_celery_app
from simple_settings import settings

broker = (
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.MESSAGE_BROKER_DB}"
)
app = Celery("tasks", broker=broker)
setup_celery_app(app)
