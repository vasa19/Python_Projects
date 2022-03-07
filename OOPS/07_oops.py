# Constructor in Inheritance


class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B():
    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        print("In C init")
        super().__init__()

    def feat(self):
        super().feature2()


c1 = C()
c1.feature1()
c1.feat()
