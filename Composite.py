"""Довольно интересный паттерн суть которого заключается в минимизации различий в управлении как группами
 объектов так и индивидуальными объектами. Для примера можно рассмотреть управление солдатами в строю.
 Существует строевой устав, который определяет как управлять строем и согласно этого устава абсолютно не важно
  кому отдается приказ (например «шагом марш») одному солдату или целому взводу. Соответственно в устав (если его
  в чистом виде считать паттерном «компоновщик») нельзя включить команду, которую может исполнить только один солдат,
   но не может исполнить группа, или наоборот."""


class Solder:
    def run(self):
        pass

class Squard:
    __solders = []

    def run(self):
        for s in self.__solders:
            s.run()

    def add_solder(self, solder):
        if solder not in self.__solders:
            self.__solders.append(solder)

    def remove_solder(self, solder):
        self.__solders.remove(solder)

s1 = Solder()
s2 = Solder()

sq = Squard()
sq.add_solder(s1)
sq.add_solder(s2)
sq.run()