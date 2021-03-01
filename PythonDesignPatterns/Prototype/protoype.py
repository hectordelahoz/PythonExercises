import copy

class Prototype:
    def __init__(self):
        self._objects = {}
    
    def register(self, name, obj):
        self._objects[name] = obj
    
    def unregister(self,name):
        del self._objects[name]
    
    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj