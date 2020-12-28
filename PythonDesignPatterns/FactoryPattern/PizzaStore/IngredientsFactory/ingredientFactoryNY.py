from .ingredientFactory import IngredientFactory
from .Ingredients.cheeseProvolone import CheeseProvolone
from .Ingredients.doughIntegral import DoughIntegral
from .Ingredients.hamSpanish import HamSpanish
from .Ingredients.pepperoniGerman import PepperoniGerman
from .Ingredients.souceAlfredo import SouceAlfredo

class IngredientFactoryNY(IngredientFactory):
    def __init__(self):
        super().__init__()
        self._city = 'New York'
        
    def createCheese(self):
        return str(CheeseProvolone())
    
    def createDough(self):
        return str(DoughIntegral())
    
    def createHam(self):
        return str(HamSpanish())
    
    def createPepperoni(self):
        return str(PepperoniGerman())
    
    def createSouce(self):
        return str(SouceAlfredo())