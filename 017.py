class A:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def sum(self):
        print(self.x + self.y)


class B:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def difference(self):
        print(self.x - self.y)

class C(A, B):
    def __init__(self, x, y, a, b):
       A.__init__(self, x,y) 
       B.__init__(self, a,b) 

c = C(10, 9, 3, 5)
c.sum()
c.difference()


