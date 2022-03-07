# Inner Class

# Outer Class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # Accesssing inner class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    # Inner Class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Vasu', 1)
s2 = Student('Kartik', 2)

s1.show()
s2.show()
