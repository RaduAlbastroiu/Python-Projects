
# class for complex numbers
class complex():

    # standard constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # read data from input
    def constructor(self):
        real = input(" The real part of the complex number: ")
        imag = input(" The imaginary part of the complex number: ")
        self.real = int(real)
        self.imag = int(imag)

    # overloading add operation
    def __add__(self, other):
        real = int(self.real + other.real)
        imag = int(self.imag + other.imag)
        return complex(real, imag)

    # overloading substraction operation
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return complex(real, imag)

    # overloading multiply operation
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return complex(real, imag)

    # print method for complex class
    def afis(self):
        if self.imag < 0:
            semn = " "
        else:
            semn = " + "

        return str(self.real) + semn + str(self.imag) + "i"
