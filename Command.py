"""Паттерн «команда» очень похож в реальной жизни на кнопки выключателей света в наших квартирах и домах.
Каждый выключатель по своей сути делает одно простое действие — разъединяет или соединяет два провода, однако
что стоит за этими проводами выключателю не известно. Что подключат, то и произойдет. Точно также действует
и паттерн «команда». Он лишь определяет общие правила для объектов (устройств), в виде соединения двух проводов
для выполнения команды, а что именно будет выполнено уже определяет само устройство (объект).
Таким образом мы можем включать одним типом выключателей как свет в комнате, так и пылесос.
"""

from datetime import time
from abc import ABCMeta, abstractmethod


class Timer:
    _start_time = None

    def start(self):
        self._start_time = time.now()

    def stop(self):
        return (time.now() - self._start_time).seconds

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class TimerStartCommand(Command):
    def __init__(self, timer):
        self._timer = timer

    def execute(self):
        self._timer.start()

class TimerStopCommmand(Command):
    def __init__(self, timer):
        self._timer = timer

    def execute(self):
        self._timer.stop()

class Trigger:
    _state = None

    def __init__(self, on_command, off_command):
        self._on = on_command
        self._off = off_command

    def on(self):
        if self._state != 'on':
            try:
                self._state = 'on'
                return self._on.execute()
            except:
                self._state = 'off'

    def off(self):
        if self._state != 'on':
            raise Exception('turn on first')
        try:
            self._state = 'off'
            return self._off.execute()
        except:
            self._state = 'on'

timer = Timer()
start_cmd = TimerStartCommand(timer)
stop_cmd = TimerStopCommmand(timer)
t = Trigger(start_cmd, stop_cmd)
t.start()
t.stop()
t.stop()