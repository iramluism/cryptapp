import abc
from typing import Any

from injector import inject

from app.domain import repositories
from app.domain import services as domain_services
from app.domain.object_values import CryptoEntries


class Service(abc.ABC):
    @abc.abstractmethod
    async def execute(self, *args, **kwargs) -> Any:
        pass


class CollectAndProcessCryptoDataService(Service):
    @inject
    def __init__(
        self,
        crypto_repository: repositories.ICryptoRepository,
        process_crypto_entries_service: domain_services.ProcessCyptoEntriesService,
    ) -> None:
        self._crypto_repository = crypto_repository
        self._process_crypto_entries_srv = process_crypto_entries_service

    async def execute(self) -> Any:
        cryptos = await self._crypto_repository.collect()

        for crypto in cryptos:
            crypto.bids = await self._process_crypto_entries_srv.execute(crypto.bids)
            crypto.asks = await self._process_crypto_entries_srv.execute(crypto.asks)

            await self._crypto_repository.save(crypto)

        return cryptos


class GetCryptoBidsService(Service):
    @inject
    def __init__(self, crypto_repository: repositories.ICryptoRepository) -> None:
        self._crypto_repository = crypto_repository

    async def execute(self, symbol: str) -> CryptoEntries:
        return await self._crypto_repository.get_bids(symbol)


class GetCryptoAsksService(Service):
    @inject
    def __init__(self, crypto_repository: repositories.ICryptoRepository) -> None:
        self._crypto_repository = crypto_repository

    async def execute(self, symbol: str) -> CryptoEntries:
        return await self._crypto_repository.get_asks(symbol)
