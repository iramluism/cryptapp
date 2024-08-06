import pytest

from tests import stubs


@pytest.mark.usefixtures("integration_test")
@pytest.mark.parametrize(
    "crypto,expected_response",
    [
        (
            stubs.get_crypto(
                symbol="BTC-USD",
                bids=stubs.get_crypto_entries(
                    count=500, total_qty=45.0, total_value=150000.00
                ),
                asks=stubs.get_crypto_entries(
                    count=500, total_qty=500.0, total_value=450000.0
                ),
            ),
            {
                "BTC-USD": {
                    "bids": {"count": 500, "qty": 45.0, "value": 150000.00},
                    "asks": {"count": 500, "qty": 500.0, "value": 450000.0},
                }
            },
        )
    ],
    indirect=["crypto"],
)
def test_get_crypto(crypto, expected_response, rest_api):
    response = rest_api.get(f"/cryptos/{crypto.symbol}")

    assert response.status_code == 200
    assert response.json() == expected_response


def test_not_found_crypto(rest_api):
    response = rest_api.get("/cryptos/INVALID")

    expected_response = {"status": 404001, "message": "CRYPTO_NOT_FOUND"}

    assert response.json() == expected_response
    assert response.status_code == 404
