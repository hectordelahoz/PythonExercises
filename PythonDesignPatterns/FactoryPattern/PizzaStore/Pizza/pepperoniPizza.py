from .pizza import Pizza

class PepperoniPizza(Pizza):
    def __init__(self,ingredientFactory):
        self._pizza = super().__init__()
        self._ingredientFactory = ingredientFactory
    
    def prepare(self, **kwargs):
        self.bakeTime(20)
        self.cheese(self._ingredientFactory.createCheese())
        self.dough(self._ingredientFactory.createDough())
        self.flavor('Pepperoni')
        self.meat(self._ingredientFactory.createPepperoni())
        self.size(kwargs['size'] if 'size' in kwargs else 'medium')
        self.souce(self._ingredientFactory.createSouce())
        self.vegies(['olives','oregano'])
        super().prepare(**kwargs)
        return self