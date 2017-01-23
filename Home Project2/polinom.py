
# import complex numbers
from complex import complex

# polynomial class
class polinom():

    # default cosntructor
    def __init__(self, listaCoef):
        self.coeficienti = []
        self.grad = 0
        if len(listaCoef) and type(listaCoef[0]) is complex:
            self.coeficienti = listaCoef
            self.grad = len(listaCoef) - 1

    # read input for polynomial class with complex coefficients
    def constructor(self):
        self.coeficienti = []

        grad = int(input(" Polynomial order(minimum order 0): "))
        self.grad = grad
        count = int(0)

        # read coefficients one by one
        while count <= grad:
            print(" Coefficient for x^" + str(count))
            coef = complex(0, 0)
            coef.constructor()
            self.coeficienti.append(coef)
            count += 1

    # computing polynomial function for a given X
    def calculareX(self, x):
        val = 1
        real = 0
        imag = 0
        for it in range(self.grad + 1):
            real += self.coeficienti[it].real * val
            imag += self.coeficienti[it].imag * val
            val *= x

        alist = []
        alist.append(complex(real, imag))
        return polinom(alist)

    # overloading add operation for two polynomials
    # this method is based on complex class overload for addition
    def __add__(self, other):
        if len(self.coeficienti) > len(other.coeficienti):
            coeficientiMici = other.coeficienti
            coeficientiMari = self.coeficienti
            for it in range(len(coeficientiMari)):
                if it >= len(coeficientiMici):
                    coeficientiMici.append(complex(0,0))

            grad = len(coeficientiMari)
            count = 0
            coeficienti = []
            while count < grad:
                coeficienti.append(coeficientiMari[count] + coeficientiMici[count])
                count += 1

            return polinom(coeficienti)
        else:
            coeficientiMici = self.coeficienti
            coeficientiMari = other.coeficienti

            for it in range(len(coeficientiMari)):
                if it >= len(coeficientiMici):
                    coeficientiMici.append(complex(0,0))

            grad = len(coeficientiMari)
            count = 0
            coeficienti = []
            while count < grad:
                coeficienti.append(coeficientiMici[count] + coeficientiMari[count])
                count += 1

            return polinom(coeficienti)

    # overloading substraction for polynomials
    # this method is based on complex class overload for substraction
    def __sub__(self, other):
        if len(self.coeficienti) > len(other.coeficienti):
            coeficientiMici = other.coeficienti
            coeficientiMari = self.coeficienti
            for it in range(len(coeficientiMari)):
                if it >= len(coeficientiMici):
                    coeficientiMici.append(complex(0,0))

            grad = len(coeficientiMari)
            count = 0
            coeficienti = []
            while count < grad:
                coeficienti.append(coeficientiMari[count] - coeficientiMici[count])
                count += 1

            return polinom(coeficienti)
        else:
            coeficientiMici = self.coeficienti
            coeficientiMari = other.coeficienti

            for it in range(len(coeficientiMari)):
                if it >= len(coeficientiMici):
                    coeficientiMici.append(complex(0,0))

            grad = len(coeficientiMari)
            count = 0
            coeficienti = []
            while count < grad:
                coeficienti.append(coeficientiMici[count] - coeficientiMari[count])
                count += 1

            return polinom(coeficienti)

    # overloading multiply operation for polynomials
    def __mul__(self, other):
        coeficienti = []
        gradFinal = len(self.coeficienti) + len(other.coeficienti)
        for it in range(gradFinal - 1):
            coeficienti.append(complex(0,0))

        for i in range(len(self.coeficienti)):
            for j in range(len(other.coeficienti)):
                coeficienti[i+j] += self.coeficienti[i] * other.coeficienti[j]

        return polinom(coeficienti)


    # print method for polynomial class
    def afis_polinom(self):
        mesaj = ""
        count = 0
        for coef in reversed(self.coeficienti):
            if self.grad == count:
                mesaj +=  "(" + coef.afis() + ")" + " + "
            else:
                mesaj += "(" + coef.afis() + ")x^" + str(self.grad - count) + " + "
            count += 1

        # deleting the last " + "
        mesaj = mesaj[:-3]
        print(mesaj)


    # this method returns the string for output
    def afisareStringTrimiteInapoi(self):
        mesaj = ""
        count = 0
        for coef in reversed(self.coeficienti):
            if self.grad == count:
                mesaj +=  "(" + coef.afis() + ")" + " + "
            else:
                mesaj += "(" + coef.afis() + ")x^" + str(self.grad - count) + " + "
            count += 1

        # deleting the last " + "
        mesaj = mesaj[:-3]
        return mesaj
