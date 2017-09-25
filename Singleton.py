def singleton(cls):
    global instance
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return getinstance()

@singleton
class AnyClass:
    pass




