from pizza import Pizza

class NyTuna(Pizza):
    def __init__(self,**kwargs):
        super().__init__()
        super().size(kwargs['size'] if 'size' in kwargs else 'small')
        super().flavor('Tuna')
    
    def prepare(self,**kwargs):
        ingredients = dict(
                            sauce='cicilian tomato',
                            cheese = 'italian muzarella',
                            meat = 'spanish tuna',
                            bakeTime = '80 min',
                            edge = kwargs['edge'] if 'edge' in kwargs else 'No Edge',
                            dough = kwargs['dough'] if 'dough' in kwargs else 'traditional')
        super().prepare(**ingredients)