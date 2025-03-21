class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        r = self.real + other.real
        i = self.img + other.img
        return Complex(r,i)

    def printValues(self):
        print(f"{self.real} + {self.img}i")


c1 = Complex(7, 2)
c2 = Complex(3, 5)
c3 = c1+c2
c1.printValues()
c2.printValues()
c3.printValues()
        