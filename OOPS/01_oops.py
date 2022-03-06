# Python Object-Oriented Programming

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram, "gb")


comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 3', 8)

# Computer.config(comp1)

comp1.config()
comp2.config()
