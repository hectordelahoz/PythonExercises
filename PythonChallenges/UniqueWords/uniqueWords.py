import re
def printwords(dictionary):
    position, word, maximum = 0, '', 0
    print('Printing Top 20 must used words')
    for element in dictionary.items():
        position += 1
        if element[1] > maximum:
            word, maximum = element[0] , element[1]
        print(f'{position} - {element[0]} = {element[1]}')
        if position >= 20:
            break

    print(f'Most repeted word is {word} and Appears {maximum} times')

def countWords(path):
    dictionary = dict()
    file = open(path, encoding='utf-8')
    totalWords = 0

    for line in file:
        words = re.findall(r"[0-9a-zA-Z-1']+",line.rstrip())
        totalWords += len(words)
        for word in words:            
            key = word.upper()
            if key not in dictionary:
                dictionary[key] = 0
            dictionary[key] = dictionary[key]+1
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)), totalWords

def main():
    path = 'C:\\Dev\\CursosTreinamentos\\LinkedInLearning\\Python\\PythonChallenges\\UniqueWords\\test.txt'
    counts, total = countWords(path)
    printwords(counts)
    print(f'Total Number of Words: {total}')

if __name__ == "__main__":
    main()