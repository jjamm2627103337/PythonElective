class Hello:
    def displayHello(self):
        print("hello")

class Hi(Hello):
    def displayHi(self):
        print("Hi")

ob = Hi()
ob.displayHello()
ob.displayHi()