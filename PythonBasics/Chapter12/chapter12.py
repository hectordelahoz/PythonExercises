def copyFile(orgPath, destPath):
    orgF = open(orgPath,'rt')
    destF = open(destPath,'wt')
    for line in orgF:
        print(line.rstrip(), file=destF)
        print('.', end='', flush=True)
    else:
        print('\ncopy Done!')
    orgF.close()
    destF.close()

def printFile(path):
    f = open(path,'rt')
    for line in f:
        print(line.rstrip())

def writeFile(path, text):
    f = open(path, 'wt')
    f.write(text)
    f.close()
    return f

def appendFile(path, text):    
    f = open(path,'at')
    f.writelines(text)
    f.close()
    return f

def main():
    filePathPrint = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\myPrograms\\Chapter12\\test1.txt'
    filePathWrite = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\myPrograms\\Chapter12\\testw.txt'
    filePathCopy = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\myPrograms\\Chapter12\\testc.txt'
    printFile(filePathPrint)
    writeFile(filePathWrite,'This is my text')
    copyFile(filePathPrint, filePathCopy)
    appendFile(filePathCopy,'This FILE is a copy!')
    printFile(filePathCopy)


if __name__ == "__main__":
    main()