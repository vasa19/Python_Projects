# Class and Objects

'''
Attributes => Variables
Behaviour => Methods(Function)
'''


class Computer:

    # Special method / Also known as constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    # config is a method
    def config(self):
        print("Config is ", self.cpu, self.ram, "gb")


# comp1 and comp2 are objects of class Computer
# They are calling constructor
comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 3', 8)

# Computer.config(comp1)

comp1.config()
comp2.config()
