#
# mainFile.py
#
# Created by Radu Gabriel Albastroiu
#

# file open
fInput = open('date.in', 'r')

def lineParser(lineInput):
    # this function takes a string, split the string and then it makes conversion from string to int
    aList = [int(char) for char in lineInput.split() if char.isdigit()]
    return aList

def inputParser():
    # this function reads the input file line by line
    listOfLists = []
    for lineInput in fInput:
        aList = lineParser(lineInput)
        listOfLists.append(aList)
    return listOfLists

def inputListToMatrix(listInput):
    # this function creates a operation matrix
    max = 0
    for line in listInput:
        if line[0] > max:
            max = line[0]
        if line[1] > max:
            max = line[1]
    
    # this is matrix creation
    opMatrix = []
    for i in range(max+1):
        alist = []
        for j in range(max+1):
            alist.append(0)
        opMatrix.append(alist)
    
    # operation matrix si filled with data from input
    for op in listInput:
        opMatrix[op[0]][op[1]] = op[2]
    
    return opMatrix

# function for testing the associative property
def isAssociative(opMatrix):
    if len(opMatrix) < 3:
        return False
    else:
        # taking every i, j, k, and testing if (i * j) * k = i * (j * k)
        for i in range(len(opMatrix)):
            for j in range(len(opMatrix)):
                for k in range(len(opMatrix)):
                    if i != j and j != k and i != k:
                        partialResult1 = opMatrix[i][j]
                        partialResult2 = opMatrix[j][k]

                        # it is guaranteed that partial results are part of the operation table
                        finalResult1 = opMatrix[partialResult1][k]
                        finalResult2 = opMatrix[partialResult2][i]

                        if finalResult1 != finalResult2:
                            return False
    return True

# function for testing the commutative property
def isCommutative(opMatrix):
    if len(opMatrix) < 2:
        return False
    else:
        # taking every i, j, and testing if i * j = j * i
        for i in range(len(opMatrix)):
            for j in range(len(opMatrix)):
                if opMatrix[i][j] != opMatrix[j][i]:
                    return False
    return True

# function for finding the neutral element
def neutralElement(opMatrix):
    if len(opMatrix) < 2:
        return -1
    else:
        for ele in range(len(opMatrix)):
            isNeutralElement = True
            for j in range(len(opMatrix)):
                if not(opMatrix[ele][j] == opMatrix[j][ele] and opMatrix[ele][j] == j):
                    isNeutralElement = False
                    break
            if isNeutralElement == True:
                return ele
    return -1

# simetrical element
def simetricalElement(opMatrix, neutralElement):
    # taking every i and testing if there is an simetrical element for it
    for i in range(len(opMatrix)):
        hasSimetrical = False
        for j in range(len(opMatrix)):
            if opMatrix[i][j] == neutralElement:
                hasSimetrical = True
        if hasSimetrical == False:  
            return False
    return True

       
# parsing input
alist = inputParser()
opMatrix = inputListToMatrix(alist)

# computation for associative, commutative, neutral element and simetrical element
boolAssociative = isAssociative(opMatrix)
boolCommutative = isCommutative(opMatrix)

neutralElement = neutralElement(opMatrix)
if neutralElement != -1:
    boolSimetrical = simetricalElement(opMatrix, neutralElement)
else:
    boolSimetrical = False

# printing
print("Operatia:")
if boolAssociative == True:
    firstString = "este"
else:
    firstString = "nu este"

if boolCommutative == True:
    secondString = "este"
else:
    secondString = "nu este"

if neutralElement != -1:
    neutralElementString = "- are pe " + str(neutralElement) + " ca element neutru"
else:
    neutralElementString = "- nu are element neutru"

if boolSimetrical == True:
    simetricalString = "- fiecare element are un invers"
else:
    simetricalString = "- operatia nu este simetrica"


print("- " + firstString + " asociativa si " + secondString + " comutativa")
print(neutralElementString)
print(simetricalString)

if boolAssociative == True and boolCommutative == True and boolSimetrical == True:
    print(" Operatia este un grup comutativ")
elif boolAssociative == True and boolSimetrical == True:
    print(" Operatia este un grup")
else:
    print(" Operatia nu este un grup")