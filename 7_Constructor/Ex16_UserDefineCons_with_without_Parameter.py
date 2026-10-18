

class Demo1:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Addition = ",self.num1+self.num2)

    def mul(self):
        print("Multiplication =",self.num1*self.num2)

d1=Demo1(10,20)
d1.add()
d1.mul()

print("==============================")
class Demo2:
    def __init__(self):
        self.n1=20
        self.n2=30
    def add1(self):
        print("Addition =",self.n1+self.n2)

    def mul2(self):
        print("Multiplication =",self.n1*self.n2)
d2=Demo2()
d2.add1()
d2.mul2()
