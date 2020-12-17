#------Chapter Three Examples---------
print('------Chapter Three Examples---------')
#-----------Type Examples-------------
print('-----------Type Examples-------------')
def printType(n = 0):
    print('n = {} and its type is {}'.format(n,type(n)))

printType(7)
printType(7.0)
printType('7.0')
printType(True)
printType(None)
#-----------String Examples-------------
print('-----------String Examples-------------')
def printString(n = 0):
    print('n = {} and its type is {}'.format(n,type(n)))

printString('seven')
printString('seven'.capitalize())
printString('seven'.upper())
precessor = 6 
sucessor = 8
printString('{} seven {}'.format(precessor, sucessor))
printString('{1} seven {0}'.format(precessor, sucessor))
printString(f'{1} seven {0}')
printString(f'{precessor} seven {sucessor}')
precessor = 123
sucessor = 456
printString('{0:>09} seven {1:<09}'.format(precessor, sucessor))
printString(f'{precessor:<09} seven {sucessor:<09}')

#-----------Number Examples-------------
print('-----------Number Examples-------------')
def printNumber(n=None):
    print(f'n = {n} and its type is {type(n)}')

printNumber(7)
printNumber(7*3)
printNumber(7.0*3)
printNumber(7/3)
printNumber(7//3)
printNumber(7%3)
printNumber(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
dotOne = Decimal('0.1')
dotThree = Decimal('0.3')
printNumber(dotOne + dotOne + dotOne - dotThree)

#-----------Sequence Examples-------------
print('-----------Sequence Examples-------------')
def printSeq(n = None):
    if n == None:
        print('There is no sequence')
        return False
    print('Sequence is: ', end=" ",flush=True)
    for index in n:
        print(f'{index}',end=' ',flush=True)
    else:
        print('')
        return True
printSeq()
x = [ 3 , 4 , 5 , 6 , 7 , 8 ]
printSeq(x)
x[2] = 55
x[3] = 66
x[4] = 77
printSeq(x)
y = ( 3 , 4 , 5 , 6 , 7 , 8 )
printSeq(y)
#y[2] = 55 #This is an Error
#y[3] = 66 #This is an Error
#y[4] = 77 #This is an Error
#printSeq(x)
y = range(10)
printSeq(y)
y = range(2,10)
printSeq(y)
y = range(2,10,3)
printSeq(y)
y = list(range(10))
y[2] = 55 #This is not an Error
y[3] = 66 #This is not an Error
y[4] = 77 #This is not an Error
printSeq(y)
#-----------Dictionary Examples-------------
print('-----------Dictionary Examples-------------')
def printDic(n = None):
    if n == None:
        print('There is no dictionary')
        return False    
    for key, value in n.items():
        print(f'key is {key} and value is {value}')
    else:
        return True

dictionary = { 'First': 1 , 'Second':2, 'Third':3, 'Forth':4, 'Fith':5 }
printDic(dictionary)
dictionary['Second'] = 22
dictionary['Third'] = 33
dictionary['Seventh'] = 7 # A new value pair was created
printDic(dictionary)
#-----------ID and Type Examples-------------
print('-----------ID and Type Examples-------------')
def printObjType (n=None):
    if n == None:
        print('Theres no attribute')
        return False
    print(f'n value is {n}', end=' ', flush=True)
    print(f'and its type is {type(n)}')
    return True

def printObjId (n=None):
    if n == None:
        print('Theres no attribute')
        return False
    print(f'n value is {n}', end=' ', flush=True)
    print(f'and its id is {id(n)}')
    return True

def verifyType (n=None):
    if n == None:
        print('Theres no attribute')
        return False
    print (f'n is {n}', end=' ', flush=True)
    if isinstance(n,tuple):
        print ('and its a tuple')
    elif isinstance(n,list):
        print ('and its a list')
    elif isinstance(n,dict):
        print ('and its a dictionary')
    else:
        print ('Other')
    return True

x = (1, 2 , 'Three' , 4.0)
y = [5 , 6, 'Three', 8.0]
z = {'Dey':34, 'Hector':35, 'Juan':13, 'Mafe':5}
printObjType(x)
printObjType(y)
printObjType(z)
printObjId(x)
printObjId(y)
printObjId(z)
printObjType(x[2])
printObjType(y[2])
printObjId(x[2])
printObjId(y[2])
printObjId(y[0])
printObjId(z['Mafe'])
verifyType(x)
verifyType(y)
verifyType(z)
verifyType(x[3])
verifyType(y[2])
verifyType(z['Hector'])