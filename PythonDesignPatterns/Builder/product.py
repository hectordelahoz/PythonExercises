class Product:
    def __init__(self):
        self._model = None
        self._chasis = None
        self._analogboard = None
        self._binaryboard = None
    
    def __str__(self):
        return f'''
        Model = {self._model}
        Chasis = {self._chasis}
        Analog Board = {self._analogboard}
        Binary Board = {self._binaryboard}
        '''