from pizzaStore import PizzaStore
from nyPepperoni import NyPepperoni
from nyTuna import NyTuna

class NyPizzaStore(PizzaStore):
    
    def createPizza(self,**kwargs):
        if 'flavor' not in kwargs:
            raise TypeError(f'At least Flavor must be informed')
        if kwargs['flavor'] == 'peperoni':
            _pizza = NyPepperoni(**kwargs)
        elif kwargs['flavor'] == 'tuna':
            _pizza = NyTuna(**kwargs)
        else:
            print('Sorry, we don\'t have this flavor in NY')
    
        return _pizza