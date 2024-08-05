from pydantic import BaseModel


class CryptoentriesResponse(BaseModel):
    average_value: float
    grater_value: dict
    lesser_value: dict
    total_qty: float
    total_px: float


class BidsCryptoEntries(BaseModel):
    bids: CryptoentriesResponse


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

        output = BidsCryptoEntries(**bids_entries_output)
        return output
