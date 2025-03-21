class Area:
    def __init__(self, l, b):
        self.l=l
        self.b=b

    def area(self):
        print(self.l * self.b)

class PrintDetails(Area):
    def __init__(self, greeting, l, b):
        self.greeting=greeting
        super().__init__(l,b)

    def printGreeting(self):
        print(self.greeting)


ob = PrintDetails("good morning", 5, 9)
ob.area()
ob.printGreeting()