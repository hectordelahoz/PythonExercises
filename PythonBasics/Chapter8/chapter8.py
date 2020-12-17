#---List Examples---
print('---List Examples---')
def printNames(args):
    print(f'this is the number of names: {len(args)}')
    index = 0
    for arg in args:        
        print(f'this is the {index} name: ', arg)
        index += 1

def stringWithToken(literal, args):
    if isinstance(literal,str):
        string = literal.join(args)
        return string

def accessByIndex(index, args):
    if index < len(args) and isinstance(index,int):
        return args[index]
    return None

def getValueIndex(value, args):
    if isinstance(value, str) and args.index(value) != None:
        return args.index(value)
    return None

def insertValue(value, index, args):
    if index < len(args):
        args.insert(index,value)
    else:
        args.append(value)
    return args

def changeValue(value, index, args):
    if index < len(args):
        args[index] = value
    else:
        args.append(value)
    return args

def popValue(index, args):
    if index < len(args):
        return args.pop(index)
    else:
        return args.pop()

def createSet(args):
    args =  set(sorted(args))
    return args

def putFamilyName(args, familyName):    
    args = [name + ' ' +  familyName for name in args]        
    return args

def disp(args):
    if isinstance(args, list):
        printList(args)
    elif isinstance(args, tuple):
        printTuple(args)
    else:
        print(repr(args),end=' ',flush=True)

def printTuple(tp):
    print('( - ', end=' ', flush=True)
    for x in tp:
        disp(x)
    print(' - )', end=' ', flush=True)

def printList(ls):
    print('[ - ', end=' ', flush=True)
    for it in ls:
        disp(it)
    print(' - ]', end=' ', flush=True)

def printMix():
    pet = ['dog', 'bird', 'fish', ('dino','aligator','snake')]
    building = ('house','apartment','farm','camp')
    person = {'Ernesto':(building[0],pet[0]),'Hector':(building[1],pet[1]),'Eduardo':(building[2],pet[2]),'Camilo':(building[3],pet[3])}
    mix = [pet, building, person]
    disp(mix)

def main():
    names = ['Ernesto', 'Eduardo', 'Camilo', 'Hector']
    printNames(names)
    separator = '*'
    print(stringWithToken(separator, names))
    print(accessByIndex(1,names))
    print(accessByIndex(0,names))
    print(accessByIndex(3,names))
    print(accessByIndex(2,names))
    print(accessByIndex(6,names))
    print(getValueIndex('Ernesto',names))
    print(getValueIndex('Hector',names))
    print(getValueIndex('Eduardo',names))
    print(getValueIndex('Camilo',names))
    print(changeValue('Juan',10,names))
    print(changeValue('Maria',10,names))
    print(changeValue('Osvaldo',4,names))
    print(changeValue('Deysy',10,names))
    print(insertValue('Juan',3,names))
    print(insertValue('Juan',4,names))
    print(insertValue('Juan',14,names))
    print(f'this is the popped value: {popValue(12,names)}')
    print(f'this is the popped value: {popValue(10,names)}')    
    print(createSet(names))
    print(putFamilyName(names,'De La Hoz'))
    printMix()
    #printNames(names)

if __name__ == '__main__':
    main()