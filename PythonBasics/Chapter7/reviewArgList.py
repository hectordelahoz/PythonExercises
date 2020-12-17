def putNumbers(*family):
    index = 0
    familyWithNumber = {}
    while index < len(family):
        familyWithNumber[str(index)] = family[index]        
        index += 1
    else:
        return familyWithNumber
    

def printNames(*family):
    for person in family:
        print(f'{person}')

def printNamesWithNumbers(**family):
    for person in family.items():
        print(f'{person[0]} - {person[1]}')

def changePerson(index,name,family):
    family[index] = name    

def appendPerson(name,family):
    family.append(name)

def F1(func):
    def F2():
        print('this is F2 Running')
        func()
        print('this is F2 Stopping')
    return F2

@F1
def myFunct():
    print('this is my funct!')

def main():
    names = ['Ernesto', 'Hector', 'Eduardo', 'Camilo']
    printNames(*names)
    namesWithNumbers = putNumbers(*names)
    printNamesWithNumbers(**namesWithNumbers)
    appendPerson('Maria',names)
    printNames(*names)
    myFunct()

if __name__ == "__main__":    
    main()