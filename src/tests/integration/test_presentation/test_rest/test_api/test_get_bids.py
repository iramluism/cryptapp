import pytest

from tests import stubs


@pytest.mark.usefixtures("integration_test")
@pytest.mark.parametrize(
    "crypto,expected_response",
    [
        (
            stubs.get_crypto(
                symbol="BTCUSD",
                bids=stubs.get_crypto_entries(
                    entries=[
                        stubs.get_order_entry(
                            px=49765.77, qty=0.08333333, num=844440551224212
                        ),
                        stubs.get_order_entry(
                            px=49765.77, qty=0.08333333, num=844440551224212
                        ),
                    ],
                    average_value=0.0,
                    greater_value=stubs.get_order_entry(
                        px=49765.77, qty=0.08333333, num=844440551224212
                    ),
                    lesser_value=stubs.get_order_entry(
                        px=49765.77, qty=0.08333333, num=844440551224212
                    ),
                    total_qty=0.0,
                    total_px=0.0,
                    total_value=0.0,
                    count=0,
                ),
            ),
            {
                "bids": {
                    "average_value": 0.0,
                    "greater_value": {
                        "num": 844440551224212,
                        "px": 49765.77,
                        "qty": 0.08333333,
                        "value": 4147.1473341141,
                    },
                    "lesser_value": {
                        "num": 844440551224212,
                        "px": 49765.77,
                        "qty": 0.08333333,
                        "value": 4147.1473341141,
                    },
                    "total_qty": 0.0,
                    "total_px": 0.0,
                }
            },
        )
    ],
    indirect=["crypto"],
)
def test_get_bids(crypto, expected_response, rest_api):
    response = rest_api.get(f"/crypto/{crypto.symbol}/bids")
    assert response.status_code == 200
    assert response.json() == expected_response
