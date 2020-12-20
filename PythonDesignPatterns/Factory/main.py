from nyPizzaStore import NyPizzaStore

def main():
    myFirstPizza = NyPizzaStore().orderPizza(**{'flavor':'peperoni', 'size':'medium'})
    mySencodPizza = NyPizzaStore().orderPizza(**{'flavor':'tuna', 'size':'large'})

if __name__ == "__main__":
    main()