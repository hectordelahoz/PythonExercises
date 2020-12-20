from pepperoni import Peperoni
from tuna import Tuna

def createPizza(**kwargs):
    if 'flavor' not in kwargs:
        raise TypeError(f'At least Flavor must be informed')
    if kwargs['flavor'] == 'peperoni':
        _pizza = Peperoni()
    elif kwargs['flavor'] == 'tuna':
        _pizza = Tuna()
    else:
        print('Sorry, we don\'t have this flavor')
    
    return _pizza