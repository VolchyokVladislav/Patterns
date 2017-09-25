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


class BottleBeerAdaper(BeerAdapter, BottleBeer):
    def open(self):

        return self.open_bottle()

class Opener:
    def __init__(self, adaper):
        self.__adaper = adaper


def get_beer(self):
    return self.__adaper.open()


a1 = BankBeerAdapter()
o = Opener(a1)
o.get_beer()