"""Паттерн «фасад» используется для того, чтобы делать сложные вещи простыми. Возьмем для примера автомобиль.
Представьте, если бы управление автомобилем происходило немного по-другому: нажать одну кнопку чтобы подать питание с
 аккумулятора, другую чтобы подать питание на инжектор, третью чтобы включить генератор, четвертую чтобы зажечь
 ламочку на панели и так далее. Всё это было бы очень сложно. Для этого такие сложные наборы действий заменяются более
 простыми и комплексные как «повернуть ключ зажигания». В данном случае поворот ключа зажигания и будет тем самым
 «фасадом» для всего обилия внутренних действий автомобиля.
"""

from abc import ABCMeta, abstractmethod

class AbstractBullet(metaclass=ABCMeta):
    @abstractmethod
    def bang(self):
        pass

class AbstractMagazine(metaclass=ABCMeta):
    _bullets = []
    _size = None

    def insert_bullet(self, bullet):
        if len(self._bullets) > self._size:
            raise Exception('full magazine')
        self._bullets.append(bullet)

    def is_empty(self):
        return len(self._bullets) > 0

    def pop_bullet(self):
        if self.is_empty():
            raise Exception('magazine is empty')
        return self._bullets.pop()

class AbstractGun:
    @abstractmethod
    def shot(self):
        pass

class Bullet(AbstractBullet):
    def bang(self):
        pass

class Magazine(AbstractMagazine):
    _size = 10

class Gun(AbstractGun):
    def __init__(self):
        self._magazine = Magazine()
        self._loaded = False

    def shot(self):
        check_magazine()
        if not self._loaded:
            self.insert_magazine()
        return self._magazine.pop_bullet().bang()

    def insert_magazine(self):
        self._loaded = True

    def remove_magazine(self):
        self._loaded = False

    def check_magazine(self):
        was_loaded = False
        if self._loaded:
            self.remove_magazine()
        was_loaded = True
        if self._magazine.is_empty():
            try:
                while True:
                    self._magazine.insert_bullet(Bullet())
            except:
                pass
        if was_loaded:
            self.insert_magazine()

gun = Gun()
gun.shot()