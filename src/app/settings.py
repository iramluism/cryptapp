from decouple import config

from app.domain import repositories as i_repositories
from app.infrastructure import repositories

DEPENDENCIES = {i_repositories.ICryptoRepository: repositories.CryptoRepository}

REPOSITORY_DATA_SOURCE = {
    "name": "app.infrastructure.repositories.data_source.DataSource",
    "sources": {
        "blockchain_api_provider": "app.infrastructure.providers.blockchain.BlockChainApiProvider",  # noqa: E501
        "cache": "app.infrastructure.repositories.cache.Cache",
    },
}


REDIS_SERVER_HOST = config("REDIS_SERVER_HOST", default="localhost")
REDIS_SERVER_PORT = config("REDIS_SERVER_PORT", default=6379)
MESSAGE_BROKER_DB = config("MESSAGE_BROKER_DB", default=0)
REDIS_CACHE_DB = config("CACHE_DB", default=1)


SIMPLE_SETTINGS = {
    "OVERRIDE_BY_ENV": True,
    "CONFIGURE_LOGGING": True,
}
