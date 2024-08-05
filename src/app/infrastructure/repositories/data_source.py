from dataclasses import dataclass
from typing import Optional

from app.domain.repositories import IDataSource
from app.infrastructure.providers.blockchain import BlockChainApiProvider
from app.infrastructure.repositories.cache import Cache


@dataclass
class DataSource(IDataSource):
    blockchain_api_provider: Optional[BlockChainApiProvider] = None
    cache: Optional[Cache] = None
