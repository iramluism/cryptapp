import pytest

from tests import stubs


@pytest.mark.usefixtures("integration_test")
@pytest.mark.parametrize(
    "crypto,expected_response",
    [
        (
            stubs.get_crypto(
                symbol="BTCUSD",
                asks=stubs.get_crypto_entries(
                    entries=[
                        stubs.get_order_entry(
                            px=4500.50, qty=0.085, num=844440551224212  # value:382.5425
                        ),
                        stubs.get_order_entry(
                            px=4900.80, qty=0.090, num=844440551224212  # value:441.072
                        ),
                        stubs.get_order_entry(
                            px=4890.70, qty=0.084, num=844440551224212  # value:410.7648
                        ),
                    ],
                    average_value=411.477766667,
                    greater_value=stubs.get_order_entry(
                        px=4900.80, qty=0.090, num=844440551224212  # value:441.072
                    ),
                    lesser_value=stubs.get_order_entry(
                        px=4500.50, qty=0.085, num=844440551224212  # value:382.5425
                    ),
                    total_qty=0.259,
                    total_px=14292,
                    total_value=1234.4333,
                    count=3,
                ),
            ),
            {
                "asks": {
                    "average_value": 411.477766667,
                    "greater_value": {
                        "num": 844440551224212,
                        "px": 4900.8,
                        "qty": 0.09,
                        "value": 441.072,
                    },
                    "lesser_value": {
                        "num": 844440551224212,
                        "px": 4500.5,
                        "qty": 0.085,
                        "value": 382.5425,
                    },
                    "total_qty": 0.259,
                    "total_px": 14292.0,
                }
            },
        )
    ],
    indirect=["crypto"],
)
def test_get_asks(crypto, expected_response, rest_api):
    response = rest_api.get(f"/cryptos/{crypto.symbol}/asks")
    assert response.status_code == 200
    assert response.json() == expected_response


def test_not_found_crypto(rest_api):
    response = rest_api.get("/cryptos/INVALID/asks")

    expected_response = {"status": 404001, "message": "CRYPTO_NOT_FOUND"}

    assert response.json() == expected_response
    assert response.status_code == 404
