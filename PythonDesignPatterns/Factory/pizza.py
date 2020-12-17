class Pizza():
    def __init__(self):
        self._ingredients = dict(sauce = None,
                                cheese = None, 
                                dough = None,                                
                                meat = None,
                                edge = None,
                                bakeTime = None,
                                numSlices = None
                                )
        self._flavor = None
        self._size = None
        self._state = 'created'
    
    def state(self):
        return self._state
    
    def flavor(self, newFlavor = None):
        if newFlavor == None:
            return self._flavor
        else:
            self._flavor = newFlavor

    def size(self, newSize = None):
        if newSize == None:
            return self._size
        else:
            self._size = newSize

    def ingredients(self,**kwargs):
        self._ingredients.update(kwargs)
        return self._ingredients

    def prepare(self,**kwargs):
        if self._state == 'created':
            self.ingredients(**kwargs)
            self._state = 'prepared'
        else:
            print(f'This pizza can not be prepared! {self._state}')
        return self
    
    def bake(self, **kwargs):
        if self.state() == 'prepared':
            remainingTime = str(0)
            self.ingredients(**dict(bakeTime = remainingTime))
            self._state = 'baked'
        else:
            print(f'This pizza can not be baked!: {self._state}')
        return self
    
    def cut(self):
        if self.state() == 'baked':
            if self.size() == 'small':
                self.numSlices = 4
            elif self.size() == 'medium':
                self.numSlices = 8
            elif self.size() == 'large':
                self.numSlices = 16
            else:
                self.numSlices = 0
        else:
            print(f'This pizza can not be cut!: {self._state}')
        
        return self
            
    
    def __str__(self):
        string = ''
        string += f'I\'m a {self.size()} sized {self.flavor()} pizza\n'
        string += f'My Ingridients are: \n'
        ingredients = self.ingredients()
        for ingredient in ingredients:
            string += f'{ingredient} - {ingredients[ingredient]}\n'
        return string