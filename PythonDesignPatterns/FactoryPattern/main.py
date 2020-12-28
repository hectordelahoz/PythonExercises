from PizzaStore.pizzaStoreCH import PizzaStoreCH
from PizzaStore.pizzaStoreNY import PizzaStoreNY

def main():
    store = PizzaStoreCH()
    product = store.orderPizza(**{'flavor':'pepperoni'})
    print(product)

    store2 = PizzaStoreNY()
    product2 = store2.orderPizza(**{'flavor':'pepperoni', 'size':'large'})
    print(product2)

if __name__ == "__main__":
    main()