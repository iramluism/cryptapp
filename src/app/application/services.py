import abc
from typing import Any


class Service(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass


class CollectAndProcessCryptoDataService(Service):
    def execute(self) -> Any:
        pass
