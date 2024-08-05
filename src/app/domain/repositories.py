import abc
from typing import List

from app.domain.aggregates import Crypto


class IDataSource:
    pass


class ICryptoRepository(abc.ABC):
    def __ini__(self, data_source: IDataSource) -> None:
        self.data_source = data_source

    def collect(self) -> List[Crypto]:
        raise NotImplementedError()

    def save(self, crypto: Crypto) -> None:
        raise NotImplementedError()

    def get(self, symbol: str) -> Crypto:
        raise NotImplementedError()
