# Cryptocurrency Signal Bot with Indicators

This project is for the purpose of generating signals using technical indicators in cryptocurrencies.
I've used Python language to code and Binance API used for API Service.

**ONGOING**

![1](https://kajeforex.com/img/cry-banner.jpg)

# Requirements

* Python `3.9`

* Numpy `1.20.2`
* TA-Lib `0.4.19`
* Python-Binance `0.7.9`


# What Are Technical Indicators?

Technical indicators are heuristic or pattern-based signals produced by the price, volume, and/or open interest of a security or contract used by traders who follow technical analysis.

By analyzing historical data, technical analysts use indicators to predict future price movements. Examples of common technical indicators include the Relative Strength Index, Money Flow Index, Stochastics, MACD and Bollinger Bands®.

# Indicators Used in This Project

## Relative Strength Index (RSI)

The relative strength index (RSI) is a momentum indicator used in technical analysis that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. The RSI is displayed as an oscillator (a line graph that moves between two extremes) and can have a reading from 0 to 100. The indicator was originally developed by J. Welles Wilder Jr. and introduced in his seminal 1978 book, "New Concepts in Technical Trading Systems."

Traditional interpretation and usage of the RSI are that values of 70 or above indicate that a security is becoming overbought or overvalued and may be primed for a trend reversal or corrective pullback in price. An RSI reading of 30 or below indicates an oversold or undervalued condition.

## Moving Average Convergence Divergence (MACD)

Moving average convergence divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA.

The result of that calculation is the MACD line. A nine-day EMA of the MACD called the "signal line," is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals. Traders may buy the security when the MACD crosses above its signal line and sell—or short—the security when the MACD crosses below the signal line. Moving average convergence divergence (MACD) indicators can be interpreted in several ways, but the more common methods are crossovers, divergences, and rapid rises/falls.

# Files Structure

## Api
* > *api_base.py* - api service base code.
* > *binance_api.py* - binance api service.

## Indicators
* > *indicators.py* - Includes rsi and macd indicators to get signal.

## Models
* > *crypto_currency.py* - to save a cryptocurrency got from binance.

## Main
* > *main.py* - to show the project general use

# References

The description texts on indicators were taken from invostepedia site.

