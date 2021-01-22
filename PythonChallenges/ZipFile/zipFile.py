import os
from zipfile import ZipFile

def compressFolder(inputPath, targetEx, outputPath):
    zippedFile = ZipFile(outputPath,'w')
    for root, dirs, files in os.walk(inputPath):
        relativePath = os.path.relpath(root, inputPath)
        for file in files:
            name, ext = os.path.splitext(file)
            if ext.lower() in targetEx:
                zippedFile.write(os.path.join(root, file), arcname=os.path.join(relativePath,file))

def main():
    sourcePath = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\ZipFile\\src'
    fileExtention = ['.txt','jpg']
    outputPath = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\ZipFile\\test.zip'
    compressFolder(sourcePath, fileExtention, outputPath)

if __name__ == "__main__":
    main()