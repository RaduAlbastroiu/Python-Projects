
# import polynom class and copy
from polinom import polinom
import copy

class matrice():

    # default constructor
    def __init__(self, ordin, listaPol):
        self.ordin = ordin
        empty = []
        self.elementematrice = []
        if ordin:
            count = 0
            alist = []
            alist.append(polinom(empty))
            self.elementematrice.append(alist)
            for i in range(1, ordin+1):
                alist = []
                alist.append(polinom(empty))
                for j in range(1, ordin+1):
                    alist.append(listaPol[count])
                    count += 1
                self.elementematrice.append(alist)

    # incremental method
    def crestere(self):
        print(" Current order of the matrix is " + str(self.ordin) + " add in order elements:")
        empty = []
        for linie in range(1, self.ordin+1):
            print(" Polynomial on the position [" + str(linie) + "][" + str(self.ordin+1) + "] :")
            aPolinom = polinom(empty)
            aPolinom.constructor()
            self.elementematrice[linie].append(aPolinom)

        alist = []
        alist.append(polinom(empty))
        for coloana in range(1, self.ordin+2):
            print(" Polynomial on the position [" + str(self.ordin+1) + "][" + str(coloana) + "] :")
            aPolinom = polinom(empty)
            aPolinom.constructor()
            alist.append(aPolinom)

        if self.ordin == 0:
            self.elementematrice.append(alist)
        self.elementematrice.append(alist)
        self.ordin += 1

    # overloading add operation
    def __add__(self, other):
        alist = []
        for i in range(1, self.ordin + 1):
            for j in range(1, self.ordin + 1):
                alist.append(self.elementematrice[i][j] + other.elementematrice[i][j])
        return matrice(self.ordin, alist)

    # overloading multiply operation
    def __mul__(self, other):
        alist = []
        empty = []
        for i in range(1, self.ordin + 1):
            for j in range(1, self.ordin + 1):
                sum = polinom(empty)
                for it in range(1, self.ordin + 1):
                    sum += self.elementematrice[it][j] * other.elementematrice[i][it]
                alist.append(copy.copy(sum))
        return matrice(self.ordin, alist)

    # computing matrix for a given X
    def evalinX(self, X):
        for i in range(1, self.ordin + 1):
            for j in range(1, self.ordin + 1):
                self.elementematrice[i][j] = self.elementematrice[i][j].calculareX(X)
        self.afisareMatrice()

    # print method
    def afisareMatrice(self):
        print()
        print(" Matrix of order " + str(self.ordin) + ": ")
        for i in range(1, self.ordin+1):
            for j in range(1, self.ordin+1):
                x = self.elementematrice[i][j].afisareStringTrimiteInapoi()
                print( " Element from position [" + str(i) + "][" + str(j) + "] = " + x)
        print()

    # computing matrix determinant for order 1 2 and 3
    def determinant(self):
        if self.ordin == 1:
            self.elementematrice[1][1].afis_polinom()

        if self.ordin == 2:
            pol  = self.elementematrice[1][1] * self.elementematrice[2][2]
            pol -= self.elementematrice[1][2] * self.elementematrice[2][1]
            pol.afis_polinom()

        if self.ordin == 3:
            pol  = self.elementematrice[1][1] * self.elementematrice[2][2] * self.elementematrice[3][3]
            pol += self.elementematrice[1][2] * self.elementematrice[2][3] * self.elementematrice[3][1]
            pol += self.elementematrice[1][3] * self.elementematrice[2][1] * self.elementematrice[3][2]
            pol -= self.elementematrice[1][3] * self.elementematrice[2][2] * self.elementematrice[3][1]
            pol -= self.elementematrice[1][2] * self.elementematrice[2][1] * self.elementematrice[3][3]
            pol -= self.elementematrice[1][1] * self.elementematrice[2][3] * self.elementematrice[3][1]
            pol.afis_polinom()
