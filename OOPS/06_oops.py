# Inheritance

# Parent class
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


# Child class / Single-level Inheritance
class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


# Multi-level Inheritance
class C(B):
    def feature5(self):
        print("Feature 5 working")


# Parent class
class D():
    def feature6(self):
        print("Feature 6 working")


# Multiple Inheritance
class E(A, D):
    def feature7(self):
        print("Feature 7 working")


a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

a1.feature1()
a1.feature2()
b1.feature3()
b1.feature1()
c1.feature1()
c1.feature5()
e1.feature1()
e1.feature7()
