class Person:
    def __init__(self,name, age, __id):
        self.name = name
        self.age = age
        self.__id = __id

    def __value(self):
        print("Hello person.")
        print(f"Value of id in private function : {self.__id}")

    def getValue(self):
        self.__value()
        print(f"Value of id in public function : {self.__id}")
        

student1 = Person("Sherry", 24, 4952)
print(student1.name, student1.age)
student1.getValue()