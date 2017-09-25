from abc import ABCMeta, abstractmethod

class ConfigInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_login(self):
        pass

    @abstractmethod
    def get_passw(self):
        pass

class Config(ConfigInterface):
    def __init__(self,login, passw):
        self.login = login
        self.passw = passw
    def get_passw(self):
        return self.passw
    def get_login(self):
        return self.login

class UserSession:
    def __init__(self, config):
        self.config = config
    def auth(self):
        print('%s, %s' % (self.config.get_login(), self.config.get_passw()))

c = Config('1', '2')
sss = UserSession(c)
sss.auth()