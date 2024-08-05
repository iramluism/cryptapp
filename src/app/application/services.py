import abc
from typing import Any

from injector import inject

from app.domain import repositories


class Service(abc.ABC):
    @abc.abstractmethod
    async def execute(self, *args, **kwargs) -> Any:
        pass


class CollectAndProcessCryptoDataService(Service):
    @inject
    def __init__(self, crypto_repository: repositories.ICryptoRepository) -> None:
        self._crypto_repository = crypto_repository

    async def execute(self) -> Any:
        cryptos = await self._crypto_repository.collect()

        return cryptos
