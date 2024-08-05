from typing import Optional

from pydantic import BaseModel

from app.domain.object_values import CryptoEntries


class Aggregate(BaseModel):
    pass


class Crypto(Aggregate):
    symbol: Optional[str] = None
    bids: Optional[CryptoEntries] = None
    asks: Optional[CryptoEntries] = None
