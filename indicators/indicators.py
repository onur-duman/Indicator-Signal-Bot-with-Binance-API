import talib as ta
import numpy as np

class Indicators:
    @staticmethod
    def RSI(crypto_currency):
        close_array = np.asarray(crypto_currency.close_values)
        close_finished = close_array[:-1]
        rsi = ta.RSI(close_finished)
        return rsi

    @staticmethod
    def MACD(crypto_currency):
        close_array = np.asarray(crypto_currency.close_values)
        close_finished = close_array[:-1]
        macd, macdsignal, macdhist = ta.MACD(close_finished)
        return macd, macdsignal, macdhist
