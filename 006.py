class Car:
    def __init__(self, model, year, price):
        self.model=model
        self.year=year
        self.price=price

    def cost(self):
        print(f"Car {self.model} {self.year} costs {self.price}")


cr1 = Car("Maruti", 2000, 100000)
cr2 = Car("XUV", 2010, 800000)

cr1.cost()
cr2.cost()