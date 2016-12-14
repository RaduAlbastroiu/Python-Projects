#
# mainFile.py
#
# Created by Radu Gabriel Albastroiu
#

def matrixRead():
    # input reading
    print(" Add another matrix, after the last row of the matrix enter an empty row")
    matrix = []
    while True:
        aline = input()
        if not len(aline):
            break
        matrix.append(aline.split())
    
    # print matrix
    print("\n Matrix is: ")
    for i in matrix:
        print(i)
    
    n = len(matrix)
    m = len(matrix[0])
    # print dimensions
    print("\n Matrix dimensions are : ")
    print(" - Lines : " + str(n))
    print(" - Columns : " + str(m))

    return matrix

# add two matrices
def addmatrix(matrixA, matrixB):
    #nA mB nB mB represent matrices dimensions
    nA = len(matrixA)
    mA = len(matrixA[0])

    nB = len(matrixB)
    mB = len(matrixB[0])
    
    #only if the two matrices have the same dimensions
    if nA != nB or mA != mB:
        print("\n Matrix with different dimensions can not be added")
    else:
        #create matrix C
        matrixC = []
        for i in range(nA):
            aline = []
            for j in range(mA):
                #every element of C is the concatenation between two elements, from A and B
                aline.append(matrixA[i][j] + matrixB[i][j])
            matrixC.append(aline)

    # print matrix
    print("\n Matrix resulted is: ")
    for i in matrixC:
        print(i)

# search in matrix the string 
def searchmatrixforstring(matrix, strn):
    listi = []
    listj = []
    i = 0
    
    # i and j represent line and column
    for line in matrix:
        i += 1
        j = 0
        # search every line of the matrix element by element
        for element in line:
            j += 1
            if element == strn:
                listi.append(i)
                listj.append(j)
    
    # if the string wasn't found
    if len(listi) == 0:
        print("\n String not found")
    # if the string was found print all the aparitions
    else:
        print("\n String found in " + str(len(listi)) + " places \n")
        for i in range(len(listi)):
            print(" #" + str(i) + " line: " + str(listi[i]) + " and column: " + str(listj[i]))


# given the line and column matrices and line lenght this function creates the string for position i and j in the result matrix
def multiplylines(matrixA, matrixB, i, j, mA):
    # "b"-"a" is not supported so i couldn't transform from "bb" to 11
    # instead i chosed to implement the next rule "ax" * "bb" = "ax" + "bb" = "axbb"
    # example : a b   +   a b   =   aabc abbd
    #           c d       c d       cadc cbdd
  
    alist = []
    for k in range(mA):
        alist.append(matrixA[i][k] + matrixB[k][j])
    
    final = ""
    for ele in alist:
        final += ele
    return final

# this function multiply the matrices using function multiplylines     
def multiplymatrix(matrixA, matrixB):
    #nA mB nB mB represent matrices dimensions
    nA = len(matrixA)
    mA = len(matrixA[0])

    nB = len(matrixB)
    mB = len(matrixB[0])
    
    if nA != mB or mA != nB:
        print("\n Matrix with different dimensions can not be multiplied")
    else:
        #for every position in final matrix we call multiplylines()
        matrixC = []
        for i in range(nA):
            alist = []
            for j in range(mA):
                alist.append(multiplylines(matrixA, matrixB, i, j, mA))
            matrixC.append(alist)
        
    # print matrix
    print("\n Matrix resulted is: ")
    for i in matrixC:
        print(i)

# compares two matrices
def comparematrix(matrixA, matrixB):
    #nA mB nB mB represent matrices dimensions
    nA = len(matrixA)
    mA = len(matrixA[0])

    nB = len(matrixB)
    mB = len(matrixB[0])
    
    if mA != mB:
        print("\n Matrix with different dimensions can not be compared")
    else:
        semn = 0
        # compares element by elemnt
        # break at first difference
        for i in range(nA):
            for j in range(mA):
                if matrixA[i][j] < matrixB[i][j]:
                    semn = 1
                    break
                elif matrixA[i][j] > matrixB[i][j]:
                    semn = 2
                    break    
                elif matrixA[i][j] == matrixB[i][j]:
                    semn = 3
        
        # semn represents the result after comparison
        if semn == 1:
            print("\n Second matrix is in lexicographical order after the First one ")
        elif semn == 2:
            print("\n First matrix is in lexicographical order after the Second one ")
        else:
            print("\n The matrices are identical")
                      
# main
listofmatrices = []

# while for the options menu
while True:
    op = int(input("\n Chose your option: \n 1. Add new matrix \n 2. Add two matrices \n 3. Search string in a matrix \n 4. Multiply matrices \n 5. Compare matrices \n 6. Stop \n Your option : "))
    
    # add new matrix option
    if op == 1:
        matrix = matrixRead()
        listofmatrices.append(matrix)
        print(" There are " + str(len(listofmatrices)) + " matrices in the program")

    # add two matrices option
    elif op == 2:
        if len(listofmatrices) < 2:
            print(" Add another matrix in the program")
        else:
            print("\n Which matrices you want to add? ")
            first = int(input(" Index of the first matrix : "))
            second = int(input(" Index of the second matrix : "))
            if first >= len(listofmatrices) or second >= len(listofmatrices):
                print(" The index is not found in the list of matrices! ")
            else:
                addmatrix(listofmatrices[first], listofmatrices[second])

    # search string in a matrix option
    elif op == 3:
        strng = input(" String to be searched: ")
        nr = int(input(" Index of the matrix in which it will be seached: "))
        if nr >= len(listofmatrices):
            print(" The index is not found in the list of matrices! ")
        else:
            searchmatrixforstring(listofmatrices[nr], strng)
    
    # multiply matrices option
    elif op == 4:
        if len(listofmatrices) < 2:
            print(" Add another matrix in the program")
        else:
            print("\n Which matrices you want to multiply? ")
            first = int(input(" Index of the FIRST matrix : "))
            second = int(input(" Index of the SECOND matrix : "))
            if first >= len(listofmatrices) or second >= len(listofmatrices):
                print(" The index is not found in the list of matrices! ")
            else:
                multiplymatrix(listofmatrices[first], listofmatrices[second])
    
    # compare matrices option
    elif op == 5:
        if len(listofmatrices) < 2:
            print(" Add another matrix in the program")
        else:
            print("\n Which matrices you want to compare? ")
            first = int(input(" Index of the FIRST matrix : "))
            second = int(input(" Index of the SECOND matrix : "))
            if first >= len(listofmatrices) or second >= len(listofmatrices):
                print(" The index is not found in the list of matrices! ")
            else:
                comparematrix(listofmatrices[first], listofmatrices[second])

    # break while loop
    else:
        break

            
        
