import abc

import pandas as pd

from app.domain.object_values import CryptoEntries
from app.domain.object_values import OrderEntry


class DomainService(abc.ABC):
    @abc.abstractmethod
    async def execute(self, *args, **kwargs):
        pass


class ProcessCyptoEntriesService(DomainService):
    async def execute(self, crypto_entries: CryptoEntries):
        entries_data = [
            {
                "px": entry.px,
                "qty": entry.qty,
                "num": entry.num,
                "value": entry.value,
            }
            for entry in crypto_entries.entries
        ]

        df = pd.DataFrame.from_dict(entries_data)

        total_qty = df["qty"].sum()
        total_px = df["px"].sum()
        average_value = df["value"].mean()
        greater_value = df.loc[df["value"].idxmax()]
        lesser_value = df.loc[df["value"].idxmin()]

        return CryptoEntries(
            entries=crypto_entries.entries,
            average_value=average_value,
            grater_value=OrderEntry(
                px=greater_value["px"],
                qty=greater_value["qty"],
                num=greater_value["num"],
            ),
            lesser_value=OrderEntry(
                px=lesser_value["px"],
                qty=lesser_value["qty"],
                num=lesser_value["num"],
            ),
            total_qty=total_qty,
            total_px=total_px,
        )
