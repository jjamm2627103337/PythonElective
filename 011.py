class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll

    def display(self):
        print(f"{self.name} {self.roll} {self.age} {self.mark}")

    def setAge(self, age):
        self.age=age

    def setMark(self, mark):
        self.mark=mark

s = Student("Jesa", 26)
s.setAge(20)
s.setMark(100)
s.display()