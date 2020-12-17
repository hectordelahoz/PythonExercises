#------Hello World Example-----------
print('------Hello World Example-----------')
name='Hector'
print('hello world: My name is {}'.format(name))
#------IF Statement Example----------
print('------IF Statement Example----------')
x = 5
y = 4
print('compare X={} with Y={}'.format(x,y))
if x>y :
    print('X is greater than Y')
elif x<y:
    print('X is less than Y')
else:
    print('X and Y are equals')
#----WHILE Statement Example---------
print('----WHILE Statement Example---------')
familyNames = ['Deysy', 'Hector', 'Juan', 'Mafe']
index=0
while index < 4:
    print("{} is part of my family".format(familyNames[index]))
    index+=1
#------FOR Statement Example---------
print('------FOR Statement Example---------')
HomeNames = ['Maria', 'Osvaldo', 'Ernesto', 'Hector', 'Eduardo', 'Camilo']
for name in HomeNames:
    print('{} is part of my Home Family'.format(name))
#--FUNCTION Statement Example---------
print('--FUNCTION Statement Example---------')
def MyPrint(n='NONE'):
    print('This is a function receiving {} as parameter'.format(n))

def IsPrime(n = 1):
    if (n <= 2):
        return True

    for t in range(2,n):
        if n % t == 0 :
            return False    
    
    return True

MyPrint()
MyPrint('Thanks')
print('Testing if X = {} and Y = {} are Prime'.format(x,y))
if IsPrime(x) == True:
    print('X = {} is Prime'.format(x))
else:
    print('X = {} is not Prime'.format(x))

if IsPrime(y) == True:
    print('Y = {} is Prime'.format(y))
else:
    print('Y = {} is not Prime'.format(y))

print('Printing List of primes up to 50')
index = 1
count = 0

for index in range(50):
    if IsPrime(index) == True:
        print(index, end=' ', flush=True)
        count+=1

print('\nThere are {} primes between 1 and 50'.format(count))
#--Class Statement Example---------
print('--Class Statement Example---------')
class Person ():
    name = 'Hector'
    surName = 'De La Hoz'
    def sayYourName(self):
        print('My Name is {} {}'.format(self.name, self.surName))

me = Person()
me.sayYourName()