import pytest

from app.domain.object_values import CryptoEntries
from app.domain.object_values import OrderEntry
from app.domain.services import ProcessCyptoEntriesService

CRYPTO_ENTRIES = [
    OrderEntry(px=49765.77, qty=0.08333333, num=844440551224212),
    OrderEntry(px=49758.29, qty=0.16666666, num=844440551224281),
    OrderEntry(px=49501.0, qty=0.0015, num=844440549858481),
    OrderEntry(px=49338.17, qty=0.00422508, num=844440551224287),
    OrderEntry(px=49183.05, qty=0.03986878, num=844440551208819),
    OrderEntry(px=48000.0, qty=0.01643447, num=844440525542364),
]

TOTAL_QTY = sum([entry.qty for entry in CRYPTO_ENTRIES])
TOTAL_PX = sum([entry.px for entry in CRYPTO_ENTRIES])
TOTAL_VALUE = sum([entry.value for entry in CRYPTO_ENTRIES])
COUNT = len(CRYPTO_ENTRIES)
AVERAGE_VALUE = TOTAL_VALUE / COUNT
GREATER_VALUE = max(CRYPTO_ENTRIES, key=lambda entry: entry.value)
LESSER_VALUE = min(CRYPTO_ENTRIES, key=lambda entry: entry.value)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "crypto_entries,expected_processed_crypto_entries",
    [
        (
            CryptoEntries(entries=CRYPTO_ENTRIES),
            CryptoEntries(
                entries=CRYPTO_ENTRIES,
                average_value=AVERAGE_VALUE,
                grater_value=GREATER_VALUE,
                lesser_value=LESSER_VALUE,
                total_qty=TOTAL_QTY,
                total_px=TOTAL_PX,
                total_value=TOTAL_VALUE,
                count=COUNT,
            ),
        )
    ],
)
async def test_process_crypto_entries_service(
    crypto_entries, expected_processed_crypto_entries
):
    service = ProcessCyptoEntriesService()

    processed_crypto_entries = await service.execute(crypto_entries)

    assert processed_crypto_entries == expected_processed_crypto_entries
