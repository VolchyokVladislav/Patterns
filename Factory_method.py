"""Данный паттерн довольно сложно объяснить в метафорах, но всё же попробую.
Ключевой сложностью объяснения данного паттерна является то, что это «метод», поэтому метафора метода будет использовано
 как действие, то есть например слово «Хочу!». Соответственно, паттерн описывает то, как должно выполнятся это «Хочу!».
Допустим ваша фабрика производит пакеты с разными соками. Теоретически мы можем на каждый вид сока делать свою
производственную линию, но это не эффективно. Удобнее сделать одну линию по производству пакетов-основ, а разделение
ввести только на этапе заливки сока, который мы можем определять просто по названию сока. Однако откуда взять название?
Для этого мы создаем основной отдел по производству пакетов-основ и предупреждаем все под-отделы, что они должны
производить нужный пакет с соком про простому «Хочу!» (т.е. каждый под-отдел должен реализовать паттерн
«фабричный метод»). Поэтому каждый под-отдел заведует только своим типом сока и реагирует на слово «Хочу!».
Таким образом если нам потребуется пакет апельсинового сока, то мы просто скажем отделу по производству
 апельсинового
 сока «Хочу!», а он в свою очередь скажет основному отделу по созданию пакетов сока, «Сделай ка свой обычный
 пакет и вот сок, который туда нужно залить».
"""

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

