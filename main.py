from views.api import API
from indicators.indicators import Indicators

if __name__ == "__main__":
    # Connect to API
    api = API()
    api.connect_to_api("Key",
                       "Secret")

    # Get Api Keys and Secret to See
    api.get_api_key()
    api.get_api_secret()

    # Taking Crypto Currency Values
    crypto_currency = api.get_crypto_currency('BTCUSDT', "1d", 100)

    # To check some information about the crypto currency which we got its values
    print("Symbol: {}\nInterval: {}\nLimit: {}".format(crypto_currency.symbol,
                                                       crypto_currency.interval,
                                                       crypto_currency.limit))

    # Its Open Values
    print(crypto_currency.open_values)

    # RSI Scores
    rsi = Indicators.RSI(crypto_currency)

    # MACD Scores
    macd, macdsignal, macdhist = Indicators.MACD(crypto_currency)




