"""Самым лучшим примером (который я смог найти в реальной жизни) для метафорического сравнения паттерна
 «приспособленец» является театральная постановка. Представьте что нам требуется поставить пьесу. Однако по
 сценарию в этой пьесе задействованы несколько десятков людей, которые по своей сути выполняют одинаковые действия,
 например участвуют в массовках различных сцен в разные промежутки времени, но между ними всё же есть какие-то
  различия (например костюмы). Нам бы стоило огромных денег нанимать для каждой роли отдельного актера, поэтому
  мы используем паттерн «приспособленец». Мы создадим все нужные нам костюмы, но для каждой массовки будем переодевать
   небольшую группу актеров в требуемые для этой сцены костюмы. В результате мы имеем возможность ценой малых
   ресурсов создавать видимость управления большим количеством казалось бы разных объектов."""

from abc import ABCMeta, abstractmethod

class Character(metaclass=ABCMeta):
    has_cap = None
    hair_color = None

    def dress_up(self, actor):
        pass

class Character1(Character):
    has_cap = True
    hair_color = 'black'

class Character2(Character):
    has_cap = False
    hair_color = 'red'

class AbstractScene(metaclass=ABCMeta):
    _characters_list = []
    _characters = {}

    def __init__(self, *actors):
        for number, character in enumerate(self._characters):
            c = character()
            c.dress_up(actors[number])
            self._characters[character] = c

    @abstractmethod
    def action(self):
        pass


class Scene1(AbstractScene):
    _characters_list = [Character1, Character2]

    def action(self):
        pass

scene = Scene1('Sam', 'John')
scene.action()