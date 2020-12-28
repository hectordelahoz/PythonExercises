from .pizza import Pizza

class HawaianPizza(Pizza):
    def __init__(self,ingredientFactory):
        _pizza = super().__init__()
        self._ingredientFactory = ingredientFactory
        return self
    
    def prepare(self, **kwargs):
        self.bakeTime(40)
        self.cheese(self._ingredientFactory.createCheese())
        self.dough(self._ingredientFactory.createDough())
        self.meat(self._ingredientFactory.createHam())
        self.flavor('Hawaian')
        self.size(kwargs['size'] if 'size' in kwargs else 'medium')
        self.souce(self._ingredientFactory.createSouce())
        self.vegies(['olives','oregano','Pineapple'])
        super().prepare(**kwargs)
        return self