from pydantic import BaseModel


class OrderEntry(BaseModel):
    px: float
    qty: float
    num: int


class CryptoEntries(BaseModel):
    entries: list[OrderEntry]
    average_value: float = 0.0
    grater_value: OrderEntry = None
    lesser_value: OrderEntry = None
    total_qty: float = 0.0
    total_px: float = 0.0
