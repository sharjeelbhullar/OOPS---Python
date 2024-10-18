class Student():
    name = "anonymous"
    
    def __init__(self, name):
        self.name = name
        # Student.name = name
        # self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

s1 = Student("sherry")
s1.changeName("Sherry")
print(s1.name)
print(Student.name)