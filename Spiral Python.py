#Print given array in clockwise spiral

def spiralArray(endRow,endColumn,a) :
    startRow = 0; startColumn = 0

    while (startRow < endRow and startColumn < endColumn) :
        
        for i in range (startColumn, endColumn) : 
            print(a[startRow][i], end = " ")
            
        startRow += 1

        for i in range (startRow, endRow) :
            print(a[i][endColumn - 1], end = " ")

        endColumn -= 1

        if (startRow < endRow) : 
            for i in range(endColumn - 1, (startColumn - 1), -1) :
                print(a[endRow - 1][i], end = " ")

        endRow -= 1

        if (startColumn < endColumn) :
            for i in range(endRow - 1, startRow - 1, -1) : 
                print(a[i][startColumn], end = " ")

        startColumn += 1

a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

R = 3; C = 6
spiralArray(R, C, a)
    