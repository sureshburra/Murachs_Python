class Student:
    def __init__(self, phy: int, chem: int, math: int):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    """The below gets automatically called when the percentage property is accessed"""

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


student1 = Student(98, 97, 99)
print(student1.percentage)

student1.phy = 86
student1.chem = 55
student1.math = 50
print(student1.phy)
print(student1.percentage)
