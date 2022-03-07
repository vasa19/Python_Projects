# Types of methods

class Student:

    school = 'Ahlcon'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class method
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static method
    @staticmethod
    def info():
        print("This is Student class")

    '''
    # getters
    def get_m1(self):
        return self.m1

    # setters
    def set_m1(self, value):
        self.m1 = value
    '''


s1 = Student(34, 67, 32)
s2 = Student(89, 62, 22)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
