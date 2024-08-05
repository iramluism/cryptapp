from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import computed_field


class OrderEntry(BaseModel):
    px: float
    qty: float
    num: int

    @computed_field
    @property
    def value(self) -> float:
        return self.px * self.qty


class CryptoEntries(BaseModel):
    entries: Optional[List[OrderEntry]] = None
    average_value: float = 0.0
    grater_value: OrderEntry = None
    lesser_value: OrderEntry = None
    total_qty: float = 0.0
    total_px: float = 0.0
