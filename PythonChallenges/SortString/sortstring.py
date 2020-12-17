def sortString(string):
    string = string.split(" ")
    sortedString = string
    for i in list(range(0,len(string))):
        for j in list(range(i+1,len(string))):
            if  string[i].upper() > string[j].upper():
                temp = sortedString[j]
                sortedString[j] = sortedString[i]
                sortedString[i] = temp
    return ' '.join(sortedString)

def main():
    print(sortString("banana ORANGE apple"))

if __name__ == "__main__":
    main()