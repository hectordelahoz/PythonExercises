from itertools import product

def solveSoduku(inMatrix):
    for(row, col) in product(range(0,9), repeat=2):
        if inMatrix[row][col] == 0:
            for number in range(1,10):
                candidate = True

                for index in range(0,9):
                    if (inMatrix[row][index] == number) or (inMatrix[index][col] == number):
                        candidate = False
                        break

                for (i, j) in product(range(0,3), repeat=2):
                    if inMatrix[row - row%3 + i][col - col%3 + j] == number:
                        candidate = False
                        break

                if candidate:
                    inMatrix[row][col] = number

                    if trial := solveSoduku(inMatrix):
                        return trial
                    else:
                        inMatrix[row][col] = 0
            return False
    return True

def printSudoku(inMatrix):
    inMatrix = [['*' if number == 0 else number for number in row] for row in inMatrix]
    print()
    for row in range(0,9):
        if(row%3 == 0) and (row != 0):
            print('-'*33)
        for col in range (0,9):
            if(col%3 ==0) and (col != 0):
                print('|',end='')
            print('',inMatrix[row][col],'',end='')
        print()
    print()



def main():
    challenge = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

    printSudoku(challenge)
    solveSoduku(challenge)
    printSudoku(challenge)

    challenge2 = [
        [3,0,0,8,0,1,0,0,2],
        [2,0,1,0,3,0,6,0,4],
        [0,0,0,2,0,4,0,0,0],
        [8,0,9,0,0,0,1,0,6],
        [0,6,0,0,0,0,0,5,0],
        [7,0,2,0,0,0,4,0,9],
        [0,0,0,5,0,9,0,0,0],
        [9,0,4,0,8,0,7,0,5],
        [6,0,0,1,0,7,0,0,3]]

    printSudoku(challenge2)
    solveSoduku(challenge2)
    printSudoku(challenge2)

if __name__ == "__main__":
    main()