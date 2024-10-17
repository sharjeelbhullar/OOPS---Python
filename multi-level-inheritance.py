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

class Prius(ToyotaCar):
    def __init__(self, model, year, brand, colors):
        self.model = model
        self.year = year
        self.brand = brand
        self.colors = colors

user1 = Prius("A3", 2023, "Toyota", ["red", "blue", "green"])
# user1.start()
# print(f"Brand = {user1.brand}")
# print(user1.colors)
# print(user1.model)
# print(user1.year)


