from abc import abstractmethod

class IngredientFactory():

    def __init__(self):
        _city = None

    @abstractmethod
    def createCheese(self):
        return 'Cheese'

    @abstractmethod
    def createDough(self):
        return 'Dough'

    @abstractmethod
    def createJam(self):
        return 'Jam'

    @abstractmethod
    def createPepperoni(self):
        return 'pepperoni'

    @abstractmethod
    def createSouce(self):
        return 'souce'

    @abstractmethod
    def createVegies(self):
        return ['vegies1','vegies2']