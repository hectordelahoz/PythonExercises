from pizza import Pizza

class NyPepperoni(Pizza):
    def __init__(self,**kwargs):
        super().__init__()
        super().size(kwargs['size'] if 'size' in kwargs else 'small')
        super().flavor('Peperoni')        
    
    def prepare(self,**kwargs):
        ingredients = dict(
                            sauce='Cicilian Tomato',
                            cheese = 'french muzarella',
                            meat = 'american pepperoni',
                            bakeTime = '40 min',
                            edge = kwargs['edge'] if 'edge' in kwargs else 'No Edge',
                            dough = kwargs['dough'] if 'dough' in kwargs else 'traditional')
        super().prepare(**ingredients)