from abc import abstractmethod

class Pizza():
    def __init__(self):
        self._bakeTime = None
        self._cheese = None
        self._dough = None
        self._flavor = None
        self._numberOfSlices = None
        self._meat = None
        self._size = None
        self._souce = None
        self._state = None
        self._vegies = []
        self._id = 0
        
    def id(self):
        return self._id    

    def bakeTime(self, BakeTime = None):
        if BakeTime:
            self._bakeTime = BakeTime
        return self._bakeTime
    
    def cheese(self, Cheese = None):
        if Cheese:
            self._cheese = Cheese
        return self._cheese

    def dough(self, Dough = None):
        if Dough:
            self._dough = Dough
        return self._dough

    def flavor(self, Flavor = None):
        if Flavor:
            self._flavor = Flavor
        return self._flavor
    
    def numberOfSlices(self, NumberOfSlices = None):
        return self._numberOfSlices
    
    def meat(self, Meat = None):
        if Meat:
            self._meat = Meat
        return self._meat
    
    def souce(self, Souce = None):
        if Souce:
            self._souce = Souce
        return self._souce
    
    def size(self, size = None):
        if size:
            self._size = size
            if size == 'small':
                self._numberOfSlices = 8
            if size == 'medium':
                self._numberOfSlices = 12
            if size == 'large':
                self._numberOfSlices = 16
        return self._size
        
    def state(self, state=None):
        if state:
            self._state = state
        return self._state
    
    def vegies(self, Vegies = None):
        if Vegies:
            self._vegies = Vegies
        return self._vegies
    
    @abstractmethod
    def prepare(self, **kwargs):
        if (self.state() == None) and (self.flavor() != None):
            self.state('prepared')
            self._id += 1
        else:
            print(f'this pizza can not be prepared')
        return self
    
    def bake(self):
        if self.state() == 'prepared':
            self.state('baked')
        else:
            print('this pizza can not be baked')
        return self
    
    def cut(self):
        if self.state() == 'baked':
            self.state('cut')
        else:
            print('this pizza can not be cut')
        return self
    
    def box(self):
        if self.state() == 'cut':
            self.state('boxed')
        else:
            print('this pizza can not be boxed')
        return self
    
    def ingredinetList(self):
        ingredients = {}
        ingredients['BakeTime'] = self.bakeTime()
        ingredients['Cheese'] = self.cheese()
        ingredients['Dough'] = self.dough()
        ingredients['Meat'] = self.meat()
        ingredients['Souce'] = self.souce()
        ingredients['Vegies'] = self.vegies()
        return str(ingredients)
    
    def __str__(self):
        return f'''pizza {self.id()}:
        Flavor = {self.flavor()}
        Size = {self.size()} - Number Of Slices = {self.numberOfSlices()}
        Ingredients = {self.ingredinetList()}
        State = {self.state()}
        '''