from .ingredientFactory import IngredientFactory
from .Ingredients.cheeseMusarella import CheeseMusarella
from .Ingredients.doughNatural import DoughNatural
from .Ingredients.jamEnglish import JamEnglish
from .Ingredients.pepperoniItalian import PepperoniItalian
from .Ingredients.sauceTomato import SouceTomato

class IngredientFactoryCH(IngredientFactory):
    def __init__(self):
        super().__init__()
        self._city = 'Chicago'
        
    def createCheese(self):
        return str(CheeseMusarella())
    
    def createDough(self):
        return str(DoughNatural())
    
    def createJam(self):
        return str(JamEnglish())
    
    def createPepperoni(self):
        return str(PepperoniItalian())
    
    def createSouce(self):
        return str(SouceTomato())