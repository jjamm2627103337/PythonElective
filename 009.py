class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b

    def area(self):
        a = self.l * self.b
        print(f"Area of rectangle is {a}")

r = Rectangle(10, 3)
r.area()