#----While Loop Examples----
print('----While Loop Examples----')
def enter_password():
    password = 'mypassword'
    tries = 0
    pw = None
    while (pw != password):
        tries += 1
        if tries > 3:
            break
        print(f'you have {4-tries} try left')
        pw = input('Enter the passord: ')

    if tries > 3:
        print('You are not allowed to enter! ALARM!')
        return False
    else:
        print('Welcome sir!')
        return True

def password_recovery(name=None):
    db = {'Hector':'Lakers', 'Juan':'Junior', 'Maria':'Frozen', 'Deysy':'Banofee'}

    if name not in db.keys():
        print(f'User {name} is not registered')
        return False

    for it in db.items():
        if name == it[0]:
            print(f'{name}, your password is: {it[1]}')
            return True        

enter_password()
password_recovery()
password_recovery('Catalina')
password_recovery('Hector')