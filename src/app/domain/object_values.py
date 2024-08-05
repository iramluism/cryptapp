from pydantic import BaseModel


class OrderEntry(BaseModel):
    px: float
    qty: float
    num: int


class CryptoEntries(BaseModel):
    symbol: str
    entries: list[OrderEntry]
    average_value: float
    grater_value: OrderEntry
    lesser_value: OrderEntry
    total_qty: float
    total_px: float
