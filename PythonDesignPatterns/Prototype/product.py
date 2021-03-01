class Product:
    def __init__(self):
        self._model = None
        self._chasis = None
        self._boards = list()
    
    def createProduct(self,**kwargs):
        if 'model' in kwargs:
            self._model = kwargs['model']
        
        if 'chasis' in kwargs:
            self._chasis = kwargs['chasis']
        
        if 'boards' in kwargs:
            self._boards = list(kwargs['boards'])
    
    def __str__(self):
        return f'''
        Model = {self._model}
        Chasis = {self._chasis}
        Boards = {self._boards}'''