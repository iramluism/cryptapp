import os

from fastapi.testclient import TestClient
import pytest
import redis


@pytest.fixture
def settings():
    from simple_settings import settings

    yield settings


@pytest.fixture
def integration_test():
    os.environ["SIMPLE_SETTINGS"] = "tests.integration.settings"


@pytest.fixture
def rest_api():
    from app.presentation.rest.api import create_app

    app = create_app()
    yield TestClient(app)


@pytest.fixture
def redis_cli(settings):
    client = redis.Redis(
        host=settings.REDIS_SERVER_HOST,
        port=settings.REDIS_SERVER_PORT,
        db=settings.REDIS_CACHE_DB,
    )
    yield client
    # client.flushdb()


@pytest.fixture
def populate_symbols(request, redis_cli):
    symbols = request.param

    for symbol in symbols:
        redis_cli.sadd("symbols", symbol)

    return symbols


@pytest.fixture
def symbol(request, redis_cli):
    symbol = request.param
    redis_cli.sadd("symbols", symbol)
    return symbol


@pytest.fixture
def crypto(request, redis_cli):
    crypto = request.param

    key = f"crypto_symbol_{crypto.symbol}"

    redis_cli.hmset(
        key,
        mapping={
            "symbol": crypto.symbol,
            "bids": crypto.bids.model_dump_json(),
            "asks": crypto.asks.model_dump_json(),
        },
    )

    yield crypto
