from app.domain.repositories import ICryptoRepository
from app.domain.repositories import IDataSource


class DataSource(IDataSource):
    blockchain_api_provider = None


class CryptoRepository(ICryptoRepository):
    def __init__(self, data_source: DataSource) -> None:
        self.blockchain_api_provider = data_source.blockchain_api_provider

    def collect(self):
        pass

    def save(self, crypto):
        pass

    def get(self, symbol):
        pass
