from mubuilder import ProtectionMuBuilder
from mubuilder import MeteringMuBuilder
from director import Director

def main():
    myBuilder = ProtectionMuBuilder()
    myDirector = Director(myBuilder)
    myDirector.buildProduct()
    product = myDirector.getProduct()
    print(product)

    myBuilder = MeteringMuBuilder()
    myDirector = Director(myBuilder)
    myDirector.buildProduct()
    product = myDirector.getProduct()
    print(product)

if __name__ == "__main__":
    main()