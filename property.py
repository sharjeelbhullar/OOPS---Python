class Student():
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    def getPercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(78, 96, 84)
print(s1.getPercentage())
print(s1.percentage)
s1.phy = 89
print(s1.getPercentage())
print(s1.percentage)
