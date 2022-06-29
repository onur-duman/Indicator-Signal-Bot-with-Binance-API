from signals.signal_base import SignalBase

class RSISignalCreator(SignalBase):
    signal_name = "RSI"
    signal_type = True
    def __init__(self, date_time, c_currency_name, initial_price, time_interval, rsi_score):
        self.date_time = date_time
        self.c_currrency_name = c_currency_name
        self.initial_price = initial_price
        self.time_interval = time_interval
        self.rsi_score = rsi_score

    def create_signal(self):
        if self.rsi_score>=27 and self.rsi_score<=33:
            self.signal_type = False
        elif self.rsi_score>=65 and self.rsi_score<=75:
            self.signal_type = True
        else:
            self.signal_type = "-"

    def create_signal_message(self):
        self.create_signal()
        self.data = {"dateTime": self.date_time,
                     "signalName": self.signal_name,
                     "coinName": self.c_currrency_name,
                     "coinInitialPrice": self.initial_price,
                     "timeInterval": self.time_interval,
                     "signalType": "BUY" if self.signal_type == False else ("SELL" if self.signal_type == True else "-")}




