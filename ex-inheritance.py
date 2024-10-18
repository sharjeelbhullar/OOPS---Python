#example program of inheritance
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print(f"Role = {self.role}")
        print(f"Department = {self.department}")
        print(f"Salary = {self.salary}")
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
engr1 = Engineer("Sherry", 24)
engr1.showDetails(  )
