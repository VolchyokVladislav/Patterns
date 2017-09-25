from abc import ABCMeta, abstractmethod

class Juice:
    pass

class OrangeJuice(Juice):
    pass

class TomatoJuice(Juice):
    pass

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def build_juice(self):
        pass

class Factory1(Factory):
    def build_juice(self):
        return OrangeJuice()

f = Factory1()
juice = f.build_juice()

