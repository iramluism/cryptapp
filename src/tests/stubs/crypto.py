from app.domain.aggregates import Crypto

CRYPTO = {
    "symbol": "BTCUSD",
    "bids": {"entries": []},
    "asks": {"entries": []},
}


def get_crypto(**values):
    crypto = CRYPTO.copy()
    crypto.update(values)
    return Crypto(**crypto)
