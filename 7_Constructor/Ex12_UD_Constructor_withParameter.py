print("====================")

class Demo:
    def __init__(self,num1,num2):
        self.num1=num2
        self.num2=num2

    def add(self):
        print("Addition =",self.num1+self.num2)

d=Demo(20,20)
d.add()

print("===================================")

class Demo1:
    def __init__(self):
        self.a=10
        self.b=20

    def add(self):
        print("Addition =",self.a+self.b)

D1=Demo1()
D1.add()

print("===================================")