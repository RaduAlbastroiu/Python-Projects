
# importing things
from polinom import polinom
from complex import complex
from matrice import matrice

# this is an example

# creating a matrix and upgrading it to order 2 then printing it
empty = []
a = matrice(0, empty)
a.crestere()
a.crestere()
a.afisareMatrice()

# creating a matrix and upgrading it to order 2 then printing it
b = matrice(0, empty)
b.crestere()
b.crestere()
b.afisareMatrice()

# add two matrices and print the resulting one
c = a + b
print("\n Matrix resulted after adding the first 2 matrices: ")
c.afisareMatrice()

# multiply two matrices and print the resulting one
c = a * b
print("\n Matrix resulted after multiplying the first 2 matrices: ")
c.afisareMatrice()

# computing matrix resulted from adding the first two matrices for a given X
c = a + b
x = int(input(" X = "))
print("\n Matrix resulted after adding first two matrices and computing them for the given X: ")
c.evalinX(x)

# computing matrix determinant
c = a + b
print("\n Polynomial function resulted after computing the determinant of the matrix resulted after adding the first two :")
c.determinant()
