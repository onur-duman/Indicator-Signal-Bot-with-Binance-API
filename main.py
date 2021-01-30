from api.binance_api import Binance

if __name__ == "__main__":
    api = Binance()
    api.connect_to_api("123", "secrett")
    api.get_api_key()
    api.get_api_secret()