from pizza import Pizza

class Peperoni(Pizza):
    def __init__(self,**kwargs):
        super().__init__()
        super().size(kwargs['size'] if 'size' in kwargs else 'small')
        super().flavor('Peperoni')
    
    def prepare(self,**kwargs):
        ingredients = dict(
                            sauce='tomato',
                            cheese = 'muzarella',
                            meat = 'pepperoni',
                            bakeTime = '30 min',
                            edge = kwargs['edge'] if 'edge' in kwargs else 'No Edge',
                            dough = kwargs['dough'] if 'dough' in kwargs else 'traditional')
        super().prepare(**ingredients)