#It is an example of single level inheritance
class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car stopped...")

    
class ToyataCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # print(self.name, self.color)
    
user1 = ToyataCar("Fortuner", "black")
user1.start()

user2 = ToyataCar("Prius", "White")
user2.stop()