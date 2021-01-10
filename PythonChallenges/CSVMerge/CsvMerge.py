import csv

def getHeader(*args):
    header = list()
    for fd in range(len(args)):
        inputCSV = open(args[fd],'r')
        fields = csv.DictReader(inputCSV).fieldnames
        for field in fields:
            if field not in header:
                header.append(field)
    return header

def writeContent(fieldNames, outputFile, *args):
    fd = open(outputFile, 'w',newline='')
    handlerW = csv.DictWriter(fd,fieldnames=fieldNames)
    handlerW.writeheader()
    for fd in range(len(args)):
        inputCSV = open(args[fd],'r')
        handlerR = csv.DictReader(inputCSV)
        for line in handlerR:
            handlerW.writerow(line)

def CsvMerge(output,*args):
    header = getHeader(*args)
    writeContent(header, output, *args)

def main():
    outputFile = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\CsvMerge\\output.csv'
    inputFiles = ['C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\CsvMerge\\csv1.csv',
                  'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\CsvMerge\\csv2.csv']
    CsvMerge(outputFile, *inputFiles)

if __name__ == "__main__":
    main()