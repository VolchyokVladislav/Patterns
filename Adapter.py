"""Данный паттерн полностью соответствует своему названию. Чтобы заставить работать «советскую» вилку через
евро-розетку требуется переходник. Именно это и делает «адаптер», служит промежуточным объектом между двумя другими,
которые не могут работать напрямую друг с другом.
"""

from abc import ABCMeta, abstractmethod

class BankBeer:
    def open_bank(self):
        pass

class BottleBeer:
    def open_bottle(self):
        pass

class BeerAdapter(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

class BankBeerAdapter(BeerAdapter, BankBeer):
    def open(self):
        return self.open_bank()

class BottleBeerAdapter(BeerAdapter, BottleBeer):
    def open(self):
        return self.open_bottle()

class Opener:
    def __init__(self, adapter):
        self.__adapter = adapter

    def get_beer(self):
        return self.__adapter.open()

a1 = BankBeerAdapter()
o = Opener(a1)
o.get_beer()
