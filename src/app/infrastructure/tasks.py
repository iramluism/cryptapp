from celery import Celery
from injector import Inject
from simple_settings import settings

from app.application.services import CollectAndProcessCryptoDataService
from app.infrastructure.setup import setup_celery_app
from app.infrastructure.setup import setup_task

broker = "redis://{host}:{port}/{db}".format(
    host=settings.REDIS_SERVER_HOST,
    port=settings.REDIS_SERVER_PORT,
    db=settings.MESSAGE_BROKER_DB,
)

app = Celery("tasks", broker=broker)
setup_celery_app(app)


@app.task(name="collect_and_process_crypto_task")
@setup_task
async def collect_and_process_crypto_data(
    service: Inject[CollectAndProcessCryptoDataService],
):
    await service.execute()


app.conf.beat_schedule = {
    "collect-and-process-crypto-every-30-seconds": {
        "task": "collect_and_process_crypto_task",
        "schedule": settings.CRYPTO_DATA_COLLECTOR_INTERVAL,
    },
}
