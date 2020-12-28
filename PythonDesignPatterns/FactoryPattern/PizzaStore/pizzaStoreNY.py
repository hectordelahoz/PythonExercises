from .pizzaStore import PizzaStore 
from .Pizza.pepperoniPizza import PepperoniPizza
from .Pizza.hawaianPizza import HawaianPizza
from .Pizza.cheesePizza import CheesePizza
from .IngredientsFactory.ingredientFactoryNY import IngredientFactoryNY

class PizzaStoreNY(PizzaStore):
    def __init__(self):
        super().__init__()
        self._factory = IngredientFactoryNY()
    
    def create(self, **kwargs):
        if 'flavor' not in kwargs:
            raise TypeError(f'At least flavor shall be informed')
        elif kwargs['flavor'] == 'pepperoni':
            self._pizza = PepperoniPizza(self._factory)
        elif kwargs['flavor'] == 'hawaian':
            self._pizza = HawaianPizza(self._factory)
        elif kwargs['flavor'] == 'cheese':
            self._pizza = CheesePizza(self._factory)
        return self._pizza

if __name__ == "__main__":
    pass