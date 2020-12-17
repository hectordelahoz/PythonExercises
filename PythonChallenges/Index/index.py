def getIndex(array,value):
    current_index = 0
    indexlist = list()
    for number in array:
        if isinstance(number, int) and (value == number):
            indexlist.append(current_index)
        elif isinstance(number,list):
            internalList = getIndex(number,value)
            if(len(internalList)):
                for x in internalList:
                    indexlist.append([current_index, x])
        current_index += 1
    return indexlist

def main():
    print(getIndex([[[1,2,3],2,[1,3]],[1,2,3]] , 2))
    
if __name__ == "__main__":
    main()