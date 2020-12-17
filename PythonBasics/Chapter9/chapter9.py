class Person:
    def __init__(self, **kwargs):
        self.__myName = kwargs['name'] if 'name' in kwargs else 'John'
        self.__myAge = kwargs['age'] if 'age' in kwargs else '21'
        self.__myNationality = kwargs['nationality'] if 'nationality' in kwargs else 'American'

    def name(self,myName = None):
        if myName:
            self.__myName = myName
        return self.__myName
    
    def age(self, myAge = None):
        if myAge:
            self.__myAge = myAge
        return self.__myAge
    
    def nationality(self, myNationaltiy = None):
        if myNationaltiy:
            self.__myNationality = myNationaltiy
        return self.__myNationality
    
    def __str__(self):
        return f'My Name is {self.name()}, I am {self.nationality()}, I am {str(self.age())} years old!'

class GeEmployee(Person):
    def __init__(self, **kwargs):
        self.__myCompany = 'GE'
        self.__mySSO = kwargs['sso'] if 'sso' in kwargs else 'TBD'
        super().__init__(**kwargs)
    
    def sso(self, mySSO = None):
        if mySSO:
            self.__mySSO = mySSO
        return self.__mySSO
    
    def __str__(self):
        return f'{super().__str__()} and I am a GE Employee {self.sso()}'


def addPerson(p,reg):
    if not isinstance(p,Person):
        print('it is not a Person')
        return False    
    reg.append(p)
    return True

def generateRegister(reg):
    allData = []
    for person in reg:
        allData.append({'Name':person.name(),'Age':person.age(),'Nationality':person.nationality()})
    else:
        return allData

def printRegister(reg):
    for entry in reg:
        for key in entry.keys():
            print(f'{key}: {entry[key]}', end=' ; ', flush=True)
        else:
            print()

def main():
    hector = Person(name='Hector', age=35, nationality='Colombian')
    john = Person()
    luis = GeEmployee(name = 'Luis', age = '32', nationality='Brazilian', sso='212518053')

    register = []
    addPerson(hector,register)
    addPerson(john,register)
    addPerson(luis,register)
    entries = generateRegister(register)
    printRegister(entries)
    print(luis)
    
if __name__ == '__main__':
    main() 