class CryptoCurrency:
    open_values = list()
    close_values = list()
    high_values = list()
    low_values = list()
    def __init__(self, symbol, interval, limit):
        self.symbol = symbol
        self.interval = interval
        self.limit = limit

