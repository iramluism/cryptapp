# API Endpoints

## Index 
1. [Error Codes](#error-codes)
2. [Get Crypto](#get-cryptossymbol)
3. [Get Crypto Bids](#get-cryptossymbolbids)
4. [Get Crypto Asks](#get-cryptossymbolasks)


## Error Codes
| Message| Code | Description |
|-------|-------|-------|
| CRYPTO_NOT_FOUND | 404001 | Crypto not found on Database |



## `GET` /cryptos/{symbol}
**Description**: Get Generic values of a Crypto

**Body**: N/A

**Response**: JSON array containing the generic metrics of crypto
```json
{
    "XLM-EUR": {
        "bids": {
            "count": 9,
            "qty": 351617.6652582,
            "value": 1818.708341587065
        },
        "asks": {
            "count": 10,
            "qty": 29991.5386175,
            "value": 118950.21817563
        }
    }
}
```

# `GET` /cryptos/{symbol}/bids

**Description**: Get Bids of a Crypto

**Body**: N/A

**Response**: JSON array containing the generic metric of a crypto bids
```json
{
    "bids": {
        "average_value": 202.078704620785,
        "greater_value": {
            "px": 0.07001,
            "qty": 25128.0344345,
            "num": 844492091893745,
            "value": 1759.2136907593451
        },
        "lesser_value": {
            "px": 0.0001,
            "qty": 165.3948705,
            "num": 844492021683325,
            "value": 0.01653948705
        },
        "total_qty": 351617.6652582,
        "total_px": 0.26522
    }
}
```

# `GET` /cryptos/{symbol}/asks

**Description**: Get Asks of a Crypto

**Body**: N/A

**Response**: JSON array containing the generic metric of a crypto asks
```json
{
    "asks": {
        "average_value": 11895.021817563,
        "greater_value": {
            "px": 4.8,
            "qty": 20186.533024,
            "num": 844492082757311,
            "value": 96895.3585152
        },
        "lesser_value": {
            "px": 0.37809,
            "qty": 72.0,
            "num": 844492071754569,
            "value": 27.222479999999997
        },
        "total_qty": 29991.5386175,
        "total_px": 187.44809
    }
}
```
