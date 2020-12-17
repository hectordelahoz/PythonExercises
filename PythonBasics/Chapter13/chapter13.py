def getComplex(real, imaginary):
    return complex(real,imaginary)

def getModule1(div, dvsr):
    return (int(div/dvsr) , div%dvsr)

def getModule(div, dvsr):
    return divmod(div,dvsr)

def getAbs(value):
    return abs(value)

def getFloat(strNum):
    v = float(strNum)
    return v, type(v)

def getInt(strNum):
    v = int(strNum)    
    return v, type(v)

def main():
    value, typeVal = getInt('15')
    print (f'value = {value}, type = {typeVal}')
    value, typeVal = getFloat('15')
    print (f'value = {value}, type = {typeVal}')
    print(getAbs(-16.57))
    print(getModule(15,8))
    print(getModule1(15,8))
    print(getComplex(15,8))
    myList = (0,0,0,0,0)
    print(any(myList))
    print(all(myList))
    myList = (0,0,1,0,0)
    print(any(myList))
    print(all(myList))
    myList = (10,20,1,50,60)
    print(list(reversed(myList)))    
    print(myList[::-1])
    print(sum(myList))
    print(max(myList))
    print(min(myList))
    print([(x,y) for x, y in enumerate(myList)])
    

if __name__ == "__main__":
    main()