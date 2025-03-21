class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

    def __gt__(self, other):
        if(self.area()>other.area()):
            print("yahooo")
        else:
            print("woohoo")

r1 = Rectangle(12, 5)
r2 = Rectangle(5, 7)
r3 = r1>r2