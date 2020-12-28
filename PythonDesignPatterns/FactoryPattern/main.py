from PizzaStore.pizzaStoreCH import PizzaStoreCH

def main():
    store = PizzaStoreCH()
    product = store.orderPizza(**{'flavor':'pepperoni'})
    print(product.flavor())

if __name__ == "__main__":
    main()