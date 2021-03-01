from product import Product
from protoype import Prototype

def main():
    myProduct = Product()
    myProduct.createProduct(model='ProtectionSAMU',chasis='80TE',boards=({'TMU321':2},{'BIU211S':1},{'CPUMZ5':1},{'DIU211':1},{'DOU211':1}))
    print(myProduct)
    myPrototype = Prototype()
    myPrototype.register('SAMU1',myProduct)

    myClone = myPrototype.clone('SAMU1')
    print(myClone)

if __name__ == "__main__":
    main()