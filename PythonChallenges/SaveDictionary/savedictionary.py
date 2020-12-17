import os

def read(path):
    fd = open(path,'rt')
    fdContent = dict()
    for line in fd:
        myLine = line.rstrip().split(':')
        fdContent[myLine[0]] = myLine[1]
    fd.close()
    return fdContent

def save(path,**kwargs):
    fd = open(path,'wt')
    for data in kwargs:
        print(f'{data}:{kwargs[data]}',file=fd,flush=True)
    fd.close()

def main():
    path = os.getcwd() + '\\SaveDictionary' + '\\dictionary.txt'
    myDict = dict(first=10, second=20, third=30, forth=40)
    save(path, **myDict)
    print(read(path))

if __name__ == "__main__":
    main()