from builder import Builder

class Director:
    def __init__(self, builder):
        self._builder = builder
    
    def buildProduct(self):
        self._builder.createProduct()
        self._builder.addModel()
        self._builder.addChassis()
        self._builder.addAnalogBoard()
        self._builder.addBinaryBoard()
    
    def getProduct(self):
        return self._builder._product