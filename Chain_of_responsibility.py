"""Самым простым примером цепочки обязанностей можно считать получение какого-либо официального документа.
Например вам требуется получить справку со счета из банка. Так или иначе, вы должны эту справку получить, однако
кто именно ее должен вам дать — пока не ясно. Вы приходите в местное отделение банка, вам говорят что «мы сейчас
заняты, идите в другое отделение», дальше вы идете в другое, там вам отвечают «мы этим не занимаемся», вы идете в
региональное отделение и там получаете нужную справку. Таким образом паттерн реализует «цепочку обязанностей»
отдельные объекты которой (отделения банка) должны обработать ваш запрос. Соответственно ваш запрос может быть
обработан в первом же отделении, или же в нескольких, в зависимости от самого запроса и обрабатывающих объектов."""

from abc import ABCMeta, abstractmethod

class AbstractVehicle(metaclass=ABCMeta):
    pass

class Vehicle(AbstractVehicle):
    min_fuel_level = 20
    min_oil_level = 5

    def __init__(self, fuel, oil):
        self.fuel_level = fuel
        self.oil_level = oil
        self.check()

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, vehicle):
        pass

class HandleFuel(Handler):
    def handle(self, vehicle):
        if vehicle.fuel_level <= vehicle.min_fuel_level:
            raise Exception('Low fuel level')

class HandleOil(Handler):
    def handle(self, vehicle):
        if vehicle.oil_level <= vehicle.min_oil_level:
            raise Exception('Low oil level')

class Garage:
    __handlers = []

    def add_handler(self, handler):
        self.__handlers.append(handler)

    def check_vehicle(self, vehicle):
        errors = []
        for h in self.__handlers:
            try:
                h.check(vehicle)
            except Exception as exc:
                errors.append(str(exc))

g = Garage()
g.add_handler(HandleFuel())
g.add_handler(HandleOil())
g.check_vehicle(Vehicle(15, 6))