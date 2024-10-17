class Student:
    def __init__(self, name):
        self.name = name
        # print(f"Your name is {self.name}")

    def __id(self):
        self.id = id

    def get_id(self):
        print(self.id)

s1 = Student("Sherry")
# print(f"Object = {s1}")
# print(f"name = {s1.name}")
# del s1.name
# print(f"id = {s1.id}")
# print(f"name = {s1.name}")

s1.get_id()

