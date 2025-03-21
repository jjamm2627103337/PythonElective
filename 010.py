class Student:
    def readData(self):
        self.name = input("Enter your name")
        self.mark1 = int(input("Enter mark 1"))
        self.mark2 = int(input("Enter mark 2"))

    def compute(self):
        self.total = self.mark1+ self.mark2

    def printData(self):
        print(f"Name: {self.name} Total: {self.total}") 

s = Student()
s.readData()
s.compute()
s.printData()