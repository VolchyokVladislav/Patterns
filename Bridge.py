"""Представим ситуацию, когда вам требуется работать на разных автомобилях, однако садясь в новый автомобиль вам
 уже желательно знать как им управлять. Таким образом вы сталкиваетесь с паттерном «мост». С одной стороны вы имеете
 множество различных автомобилей (разные модели и марки), но среди все них есть общая абстракция (интерфейс) ввиде
 руля, педалей, коробки передач и так далее. Таким образом мы задаем как-бы правила изготовления автомобилей по
 которым мы можем создавать любые их виды, но за счет сохранения общих правил взаимодействия с ними, мы можем
 одинаково управлять каждым из них. «Мостом» в данном случае является пара двух «объектов»: конкретного автомобиля
 и правил взаимодействия с этим (и любым другим) автомобилем.
"""

from abc import ABCMeta, abstractmethod

class Kitchen(metaclass=ABCMeta):
    @abstractmethod
    def cook_eggs(self):
        pass

class FrenchKitchen(Kitchen):
    def cook_eggs(self):
        pass

class ItalianKitchen(Kitchen):
    def cook_eggs(self):
        pass

class Restourant(metaclass=ABCMeta):
    @abstractmethod
    def get_eggs_dish(self, kitchen):
        pass

class Restourant1(Restourant):
    def get_eggs_dish(self, kitchen):
        return kitchen.cook_eggs()

res = Restourant1()
res.get_eggs_dish(FrenchKitchen())