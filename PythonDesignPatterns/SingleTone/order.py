from orderNumber import OrderNumber

class Order(OrderNumber):
    
    def __init__(self, **kwargs):
        OrderNumber.__init__(self)

        if 'table' not in kwargs:
            raise ValueError('At least table number shall be given')
        else:
            self._table = kwargs['table']
        
        if 'products' not in kwargs:
            self._products = None
        else:
            self._products = kwargs['products']
        
        self._id = self._orderNumber['order']
        self._orderNumber['order'] += 1
        self._pendingOrders[self._id] = kwargs

    def __str__(self):
        return f'''
        ID - {self._id}
        table - {self._table}
        products - {self._products}
        next order - {self._orderNumber}
        Peding Orders - {self._pendingOrders}'''

myOrder = Order(table='5',products=('Pizza','Coke','Ice Cream'))
print(myOrder)
otherOrder = Order(table='3',products=('Hot-Dog','Pepsi','fries'))
print(otherOrder)
print(myOrder)