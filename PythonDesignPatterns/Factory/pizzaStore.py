from abc import ABC, abstractmethod

class PizzaStore():

    @abstractmethod
    def createPizza(self, **kwargs):
        pass

    def orderPizza(self, **kwargs):
        pizza = self.createPizza(**kwargs)        
        pizza.prepare()
        print(f'your {pizza.flavor()} pizza is now {pizza.state()}')
        pizza.bake()
        print(f'your {pizza.flavor()} pizza is now {pizza.state()}')
        pizza.cut()
        print(f'your {pizza.flavor()} pizza is now {pizza.state()}')
        pizza.box()
        print(f'your {pizza.flavor()} pizza is now {pizza.state()} and ready')
        return pizza