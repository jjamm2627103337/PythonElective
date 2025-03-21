class Arith:
    def read(self):
        self.a = int(input("Enter first number"))
        self.b = int(input("Enter second number"))

    def sum(self):
        s = self.a+self.b
        print(s)

a1 = Arith()
a1.read()
a1.sum()