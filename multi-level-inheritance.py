class Car:
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

    def __coloravailable(self, colors):
        self.colors = colors

    def getcolors(self):
        print(self.colors)

class Prius(ToyotaCar):
    def __init__(self, model, year, brand, colors):
        self.model = model
        self.year = year
        super().__init__(brand)
        self._ToyotaCar__coloravailable(colors)  

user1 = Prius("A3", 2023, "Toyota", ["white", "black", "silver"])
user1.start()
user1.stop()
print(user1.brand)
print(user1.model)
print(user1.year)
user1.getcolors()



