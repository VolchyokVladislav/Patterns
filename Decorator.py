"""Как понятно из названия, данный паттерн чаще всего используется для расширения исходного объекта до требуемого вида.
 Например мы условно можем считать «декоратором» человека с кистью и красной краской. Таким образом, какой бы объект
 (или определенный тип объектов) мы не передали в руки «декоратору», на выходе мы будем получать красные объекты.
"""

from abc import ABCMeta, abstractmethod

class Box(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self):
        pass

class WoodenBox(Box):
    def get_weight(self):
        pass

class NailedBox(Box):
    def __init__(self, box):
        self.__box = box

    def get_weight(self):
        return self.__box.get_weight() + 10

box = NailedBox(WoodenBox())