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
