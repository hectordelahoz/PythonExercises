import simpleFactory

def main():
    myFirstPizza = simpleFactory.createPizza(**{'flavor':'peperoni'})
    myFirstPizza.prepare()
    myFirstPizza.bake()
    print(myFirstPizza.state())

if __name__ == "__main__":
    main()