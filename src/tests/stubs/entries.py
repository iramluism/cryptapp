import copy

from app.domain.object_values import CryptoEntries
from app.domain.object_values import OrderEntry

ORDER_ENTRY = {
    "px": 49765.77,
    "qty": 0.08333333,
    "num": 844440551224212,
}


CRYPTO_ENTRIES = {
    "entries": [],
    "average_value": 0.0,
    "greater_value": None,
    "lesser_value": None,
    "total_qty": 0.0,
    "total_px": 0.0,
    "total_value": 0.0,
    "count": 0,
}


def get_crypto_entries(**values):
    crypto_entries = copy.deepcopy(CRYPTO_ENTRIES)
    crypto_entries.update(values)
    return CryptoEntries(**crypto_entries)


def get_order_entry(**values):
    order_entry = copy.deepcopy(ORDER_ENTRY)
    order_entry.update(values)
    return OrderEntry(**order_entry)
