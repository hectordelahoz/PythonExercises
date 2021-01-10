import random

def getWord(number):
    path = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\Diceware\\wordlist.txt'
    fd = open(path)
    for line in fd:
        code, word = line.rstrip().split('\t')
        if code == number:
            return word
    else:
        return 'None'

def generateNumber():
    result = ''
    for x in range(5):
        result += str(random.randint(1,6))
    return result

def getPassword(numberOfWords):
    passPhrase = ''
    for x in range(numberOfWords):
        passPhrase += getWord(generateNumber())
        if x < numberOfWords:
            passPhrase += ' '
            
    return passPhrase

def main():
    password = getPassword(5)
    print(password)

if __name__ == "__main__":
    main()