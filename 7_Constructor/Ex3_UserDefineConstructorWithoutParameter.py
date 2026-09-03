print("======Ex1 - User Define Constructor(without Parameter)===============")

class Demo:

    def __init__(self):
        self.a=10
        self.b=20

    def add(self):
        addition=self.a+self.b
        print("Addition of no = ",addition)

    def mul(self):
        multiplication=self.a*self.b
        print("Multiplication of no =",multiplication)

d=Demo()
d.add()
d.mul()

print("======Ex2 - User Define Constructor(without Parameter)===========")

class Demo1:
    def __init__(self):
        self.a=10
        self.b=20
    def mul(self):
        multiplication=self.a * self.b
        print("Multiplication = ",multiplication)

d1=Demo1()
d.mul()

print("======Ex3-User Define Constructor(Without Parameter)===========")

class Demo3:

    def __init__(self):
        self.x=5
        self.y=5
    def add1(self):
        addition1=self.x + self.y
        print("Addition =",addition1)

d3=Demo3()
d3.add1()

print("===============================================================")



