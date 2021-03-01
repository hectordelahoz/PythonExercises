from product import Product

class Builder():
    def __init__(self):
        self._product = None
    
    def createProduct(self):
        self._product = Product()