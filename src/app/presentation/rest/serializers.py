from pydantic import BaseModel

from app.domain.aggregates import Crypto


class CryptoData(BaseModel):
    average_value: float
    grater_value: dict
    lesser_value: dict
    total_qty: float
    total_px: float


class BidsCryptoEntriesResponse(BaseModel):
    bids: CryptoData


class AsksCryptoEntriesResponse(BaseModel):
    asks: CryptoData


class GenericCryptoData(BaseModel):
    count: int
    qty: float
    value: float


class Serializer:
    async def to_dict(self, obj) -> dict:
        return obj


class BidsEntriesSerializer(Serializer):
    async def to_dict(self, obj) -> dict:
        bids_entries_output = {
            "bids": {
                "average_value": obj.average_value,
                "grater_value": obj.grater_value.dict(),
                "lesser_value": obj.lesser_value.dict(),
                "total_qty": obj.total_qty,
                "total_px": obj.total_px,
            }
        }

        output = BidsCryptoEntriesResponse(**bids_entries_output)
        return output


class AsksEntriesSerializer(Serializer):
    async def to_dict(self, obj) -> dict:
        asks_entries_output = {
            "asks": {
                "average_value": obj.average_value,
                "grater_value": obj.grater_value.dict(),
                "lesser_value": obj.lesser_value.dict(),
                "total_qty": obj.total_qty,
                "total_px": obj.total_px,
            }
        }

        output = AsksCryptoEntriesResponse(**asks_entries_output)
        return output


class GenericCryptoDataSerializer(Serializer):
    async def to_dict(self, obj: Crypto) -> dict:
        output = {
            obj.symbol: {
                "bids": {
                    "count": obj.bids.count,
                    "qty": obj.bids.total_qty,
                    "value": obj.bids.total_value,
                },
                "asks": {
                    "count": obj.asks.count,
                    "qty": obj.asks.total_qty,
                    "value": obj.asks.total_value,
                },
            }
        }

        return output
