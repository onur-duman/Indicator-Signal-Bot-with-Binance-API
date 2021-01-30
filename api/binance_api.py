from binance.client import Client
from api.api_base import ApiBase
from models.crypto_currency import CryptoCurrency


class Binance(ApiBase):
    client = ""
    def __init__(self, api_key="Key", api_secret="Secret"):
        if api_key != "Key" and api_secret != "Secret":
            Binance().connect_to_api(api_key, api_secret)
        else:
            self.api_key = api_key
            self.api_secret = api_secret

    def connect_to_api(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(self.api_key, api_secret)

    def get_api_key(self):
        print("Your Api Key: {}".format(self.api_key))

    def get_api_secret(self):
        print("Your Api Secret: {}".format(self.api_secret))

    def get_crypto_currency(self, symbol, interval, limit):
        klines = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        crypto_currency = CryptoCurrency(symbol, interval, limit)

        for kline in klines:
            crypto_currency.open_values.append(float(kline[1]))
            crypto_currency.high_values.append(float(kline[2]))
            crypto_currency.low_values.append(float(kline[3]))
            crypto_currency.close_values.append(float(kline[4]))

        return crypto_currency


