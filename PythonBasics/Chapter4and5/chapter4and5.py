#---------Example IF-------------
print('-----Example IF---------')
def detect_true(x=None):
    if x == True:
        print('This is an if')
        return True
    elif x == False:
        print('This is an elif')
        return False
    else:
        print('This is an else')
        return True

detect_true(True)
detect_true(10)
detect_true(0)

#------Example Logic Op-----------
print('-----Example Logic Op------')
def logic_or(x=None,y=None):
    if x==True or y==True:
        print(f'someone is true: {x}, {y}', end=' ', flush=True)
        return True
    else:
        print(f'Both are false: {x}, {y}', end=' ', flush=True)
        return False

def logic_and(x=None, y=None):
    if x==True and y==True:
        print(f'Both are True: {x}, {y}', end=' ', flush=True)
        return True
    else:
        print(f'Someone is False: {x}, {y}', end=' ', flush=True)
        return False

print(f'return = {logic_or(True, True)}')
print(f'return = {logic_or(True, False)}')
print(f'return = {logic_or(False, True)}')
print(f'return = {logic_or(False, False)}')

print(f'return = {logic_and(True, True)}')
print(f'return = {logic_and(True, False)}')
print(f'return = {logic_and(False, True)}')
print(f'return = {logic_and(False, False)}')

#------Example Membership-----------
print('-----Example Membership------')
def membership(x=None, y=None):
    if x in y:
        print(f'{x} is in {y}')
        return True
    else:
        print(f'{x} is NOT in {y}')
        return False

even_numbers = list(range(0,10,2))
my_number = 5
membership(my_number, even_numbers)
my_number = 4
membership(my_number, even_numbers)

odd_numbers = {1,3,5,7,9}
for i in odd_numbers:
    print(f'is {i} in odd_numbers? = {i in odd_numbers}')

#------Example Binary Op-----------
print('-----Example Binary Op------')
def set_bit(number=None, index=None):
    if number == None or index ==None:
        print(f'No parameters are passed')
        return False
    
    new_number = number | (1 << index)
    print(f'this is the old number: {number:08b}', end=' ', flush=True)
    print(f'this is the new number with {index} bit set: {new_number:08b}')
    return True

def clear_bit(number=None, index=None):
    if number == None or index ==None:
        print(f'No parameters are passed')
        return False
    
    new_number = number & (0xff^(1 << index))
    print(f'this is the old number: {number:08b}', end=' ', flush=True)
    print(f'this is the new number with bit {index} clear: {new_number:08b}')
    return True

set_bit(122,0)
set_bit(180,0)
clear_bit(135,2)

#------Example Terciary Op-----------
print('-----Example Terciary Op------')

condition = True
print(f'x = {3 if condition else 10}')
condition = False
print(f'x = {3 if condition else 10}')

#------Example Arithm Op-----------
print('-----Example Arithm Op------')
print (f'x = 2 * 5 = {2*5}')
print (f'x = 2 ** 5 = {2**5}')
print (f'x = 10 / 10 = {10/3}')
print (f'x = 10 // 3 = {10//3}')
print (f'x = 10 % 3 = {10%3}')