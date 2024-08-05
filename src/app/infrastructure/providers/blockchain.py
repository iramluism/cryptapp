import requests


class BlockChainApiProvider:
    base_url = "https://api.blockchain.com/v3/exchange"

    def get_bids(self, symbol: str):
        raise NotImplementedError()

    def get_symbols(self):
        url = f"{self.base_url}/symbols"
        response = requests.get(url)
        return response.json()

    def get_l3_order_book(self, symbol: str):
        url = f"{self.base_url}/l3/{symbol}"
        response = requests.get(url)
        return response.json()
