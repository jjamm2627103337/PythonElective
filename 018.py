class A:
    def area(self, a, b=None):
        if(b==None):
            print(a*a)
        else:
            print(a*b)

obj = A()
obj.area(5)
obj.area(10, 6)
obj.area(10,20,5)