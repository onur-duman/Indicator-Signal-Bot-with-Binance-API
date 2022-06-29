from abc import ABCMeta, abstractmethod

class SignalBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self): pass
    @abstractmethod
    def create_signal(self): pass