print("======Constructor with Parameter=============")

class Demo:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition =",self.num1+self.num2)
    @staticmethod
    def mul(num1,num2):
        print("Multiplication =",num1* num2)

d=Demo(20,20)
d.add()

Demo.mul(30,30)

print("======Constructor without Parameter=============")

class Demo1:
    def __init__(self):
        self.num1=10
        self.num2=20
    def add1(self):
        print("Addition =",self.num1+self.num2)
    def mul1(self):
        print("Multiplication =",self.num1* self.num2)

d1=Demo1()
d1.add1()
d1.mul1()
print("======Constructor without Parameter=============")























