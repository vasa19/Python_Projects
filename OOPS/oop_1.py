# Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Vasu', 'Saxena', 50000)
emp_2 = Employee('Kartik', 'Saxena', 30000)

'''
emp_1.first = 'Vasu'
emp_1.last = 'Saxena'
emp_1.email = 'vasusaxena19@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Kartik'
emp_2.last = 'Saxena'
emp_2.email = 'kartiksaxena2003@gmail.com'
emp_2.pay = 30000
'''

print(emp_1.Fullname())
print(emp_1.email)

print(emp_2.Fullname())
print(emp_2.email)
