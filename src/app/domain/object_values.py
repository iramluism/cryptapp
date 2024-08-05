from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import computed_field
from pydantic import Field


class OrderEntry(BaseModel):
    px: float
    qty: float
    num: int

    @computed_field
    @property
    def value(self) -> float:
        return self.px * self.qty


class CryptoEntries(BaseModel):
    entries: List[OrderEntry] = Field(default_factory=list)
    average_value: float = 0.0
    greater_value: Optional[OrderEntry] = None
    lesser_value: Optional[OrderEntry] = None
    total_qty: float = 0.0
    total_px: float = 0.0
    total_value: float = 0.0
    count: int = 0
