from abc import abstractmethod
from .Pizza.pizza import Pizza

class PizzaStore():
    def __init__(self):
        self._factory = None
        self._pizza = None
        
    @abstractmethod
    def create(self, **kwargs):
        pass    

    def orderPizza(self, **kwargs):
        self._pizza = self.create(**kwargs)
        self._pizza.prepare(**kwargs)
        self._pizza.bake()
        self._pizza.cut()
        self._pizza.box()
        return self._pizza

if __name__ == "__main__":
    pass