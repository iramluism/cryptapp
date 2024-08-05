import json
from typing import List

from app.domain.aggregates import Crypto
from app.domain.aggregates import CryptoEntries
from app.domain.repositories import ICryptoRepository
from app.infrastructure.repositories.data_source import DataSource


class CryptoRepository(ICryptoRepository):
    def __init__(self, data_source: DataSource) -> None:
        self._blockchain_api_provider = data_source.blockchain_api_provider

        self._cache = data_source.cache
        self._symbols_cache_key = "symbols"

    async def _collect_symbols(self):
        symbols = self._blockchain_api_provider.get_symbols()

        crypto_symbols = []
        for symbol, properties in symbols.items():
            if properties.get("status") != "open":
                continue

            self._cache.add_to_set(self._symbols_cache_key, symbol)
            crypto_symbols.append(symbol)

        return crypto_symbols

    async def _collect_l3_orders(self, symbols):
        cryptos = []

        for symbol in symbols:
            l3_order_book = self._blockchain_api_provider.get_l3_order_book(symbol)
            crypto = Crypto(
                symbol=symbol,
                bids=CryptoEntries(entries=l3_order_book.get("bids")),
                asks=CryptoEntries(entries=l3_order_book.get("asks")),
            )
            cryptos.append(crypto)

        return cryptos

    async def collect(self) -> List[Crypto]:
        symbols = await self._collect_symbols()
        cryptos = await self._collect_l3_orders(symbols)

        return cryptos

    async def _get_symbols_cache_key(self, symbol):
        return f"crypto_symbol_{symbol}"

    async def save(self, crypto: Crypto):
        key = await self._get_symbols_cache_key(crypto.symbol)

        crypto_data = crypto.model_dump()

        self._cache.save_map(
            key,
            {
                "symbol": crypto.symbol,
                "bids": json.dumps(crypto_data.get("bids") or []),
                "asks": json.dumps(crypto_data.get("asks") or []),
            },
        )

    async def get(self, symbol):
        pass

    async def get_bids(self, symbol) -> CryptoEntries:
        key = await self._get_symbols_cache_key(symbol)
        bids = self._cache.get_map_value(key, "bids")

        bids_data = json.loads(bids)
        entries = CryptoEntries(**bids_data)

        return entries
