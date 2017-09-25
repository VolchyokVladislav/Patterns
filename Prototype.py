"""Данный паттерн чем-то напоминает «фабрику», он также служит для создания объектов, однако с немного другим подходом.
 Представьте что у вас есть пустой пакет (из под сока), а вам нужен полный с апельсиновым соком. Вы «говорите» пакету
 «Хочу пакет апельсинового сока», он в свою очередь создает свою копию и заполняет ее соком, который вы попросили.
 Немного «сказочный пример», но в программировании часто так и бывает. В данном случае пустой пакет и является
 «прототипом», и в зависимости от того что вам требуется, он создает на своей основе требуемые вами объекты
 (пакеты сока).
Клонирование не обязательно должно производится на самом «пакете», это может быть и какой-то другой «объект»,
главное лишь что данный «прототип» позволяет получать его экземпляры.
"""


from copy import deepcopy

class Box:
    width = 10
    height = 10
    lenght = 10

class Prototype:
    _objects = {}

    def register(self, object):
        self._objects[object.__class__] = object
    def clone(self, object_class, **values):
        if object_class not in self._objects:
            raise Exception('Not found')
        c = deepcopy(self._objects[object_class])
        for name, value in values.items():
            setattr(c, name, value)
        return c

b1 = Box()
p = Prototype()
p.register(b1)
b1 = p.clone(Box, width=12)
