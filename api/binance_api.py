from binance.client import Client
from api.api_base import ApiBase

class Binance(ApiBase):
    def __init__(self, api_key="Key", api_secret="Secret"):
        if api_key != "Key" and api_secret != "Secret":
            Binance().connect_to_api(api_key, api_secret)
        else:
            self.api_key = api_key
            self.api_secret = api_secret

    def connect_to_api(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_api_key(self):
        print("Your Api Key: {}".format(self.api_key))

    def get_api_secret(self):
        print("Your Api Secret: {}".format(self.api_secret))


