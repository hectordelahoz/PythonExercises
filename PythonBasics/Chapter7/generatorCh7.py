#---Generator Example---
print('---Generator Example---')

def generator():
    for number in range(1,10,2):
        password = (number * 5) - 3
        yield password

if __name__ == "__main__":
    allPasswords = generator()
    for eachPassword in allPasswords:
        print(eachPassword)