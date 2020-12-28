from .pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self,ingredientFactory):
        _pizza = super().__init__()
        self._ingredientFactory = ingredientFactory
        return self
    
    def prepare(self, **kwargs):
        self.bakeTime(30)
        self.cheese(self._ingredientFactory.createCheese())
        self.dough(self._ingredientFactory.createDough())
        self.flavor('Cheese')
        self.size(kwargs['size'] if 'size' in kwargs else 'medium')
        self.souce(self._ingredientFactory.createSouce())
        self.vegies(['olives','oregano'])
        super().prepare(**kwargs)
        return self