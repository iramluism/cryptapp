from dataclasses import dataclass
from typing import Optional

from app.domain.repositories import IDataSource
from app.infrastructure.providers.blockchain import BlockChainApiProvider


@dataclass
class DataSource(IDataSource):
    blockchain_api_provider: Optional[BlockChainApiProvider] = None
