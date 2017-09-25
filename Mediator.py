"""Вспомним пример из паттерна «одиночка». Так вот телефонная станция в том примере по сути также являлась паттерном
«посредник», то есть обеспечивала взаимодействие группы объектов без необходимости обеспечения связи каждого объекта
друг с другом.
Однако дополнительной ответственность этого «паттерна» является также управление этой группой через «посредника».
 То есть если мы возьмем пример с армейским строем, то медиатором будет командир отделения, то есть нам нет
 необходимости взаимодействовать с каждым солдатом в отдельности, достаточно отдавать приказания лишь командиру
 отделения, а он уже сам решит какие действия должны быть выполнены внутри его отделения.
"""

from abc import ABCMeta, abstractmethod

class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass

class User:
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator

    def send(self, text):
        self._mediator.send(self, text)

    def receive(self, user, text):
        print('%s: %s' % (user.name, text))

class Chat(Mediator):
    _users = []

    def add_user(self, user):
        self._users.append(user)

    def send(self, user, text):
        for u in self._users:
            u.receive(user, text)

c = Chat()
jaf = User('Jaf', c)
bill = User('Bill', c)
jaf.send('Hello')
bill.send('Hi!')