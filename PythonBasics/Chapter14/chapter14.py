import sys
import os
import random
import datetime

def getTimeNow():
    return datetime.datetime.now()

def shuffledList(start, stop, step):
    myList = list(range(start,stop,step))
    random.shuffle(myList)
    return myList
    

def getRandomFromRandom(start, stop):
    return random.randint(start,stop)

def getRandomFromOs(lenght):
    return os.urandom(lenght).hex()

def getCurrentDir():
    return os.getcwd()

def getPath():
    return os.path

def getOS():
    return os.name

def getPlatfor():
    return sys.platform

def getPythonVersion():
    return sys.version_info

def main():
    print('this is my python version: {}.{}.{}'.format(*getPythonVersion()))
    print(f'this is my platform: {getPlatfor()}')
    print(f'this is my os: {getOS()}')
    print(f'this is my PATH: {getPath()}')
    print(f'this is my pwd: {getCurrentDir()}')
    print(f'this is my Random from OS:  {getRandomFromOs(3)}')
    print(f'this is my Random from ramdom:  {getRandomFromRandom(1,100)}')
    print(f'this is my shuffled list:  {shuffledList(1,10,2)}')
    print(f'this is my time: {getTimeNow()}')

if __name__ == "__main__":
    main()