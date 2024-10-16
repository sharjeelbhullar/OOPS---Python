class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        average = sum/3
        print("hi", self.name , "your avg score is:", average)  

s1 = Student("Sharjeel", [65, 72, 70])
s1.average()