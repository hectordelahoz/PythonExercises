import random

def printDataByFace(kwarg):
    kwarg = sorted(kwarg.items())
    print('CASE - Probability')
    for x in range(len(kwarg)):
        print(f'{kwarg[x][0]} = {kwarg[x][1]*0.0001:.6}') 

def getEssayByFace(*args):
    data = {}

    for essay in range(1000000):
        essayResult = ''
        for number in range(len(args)):
            essayResult += str(random.randint(1,args[number]))
        else:
            if essayResult not in data:
                data[essayResult] = 1
            else:
                data[essayResult] += 1
    printDataByFace(data)
    return data

def printDataByResult(args, dices):
    for x in range(len(args)):
        print(f'{x + dices} - {args[x]*0.0001:.6}')

def getEssayByResult(*args):
    data = [0 for x in range(len(args),sum(args)+1)]

    for essay in range(1000000):
        essayResult = 0
        for number in range(len(args)):
            essayResult += random.randint(1,args[number])
        else:
            data[essayResult-len(args)] += 1
    printDataByResult(data,len(args))
    return data

def main():
    print('-------------------')
    getEssayByFace(6,6,4)
    print('-------------------')
    getEssayByResult(6,6,4)
    
if __name__ == "__main__":
    main()