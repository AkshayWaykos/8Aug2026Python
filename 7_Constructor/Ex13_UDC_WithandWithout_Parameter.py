print("=====UDConstructor with parameter====")

class Demo1:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    @staticmethod
    def mul(num1,num2):
        print("Multiplication=",num1 * num2)

Demo1.mul(20,20)

print("===================================")

class Demo2:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        print("Addition=",self.n1+self.n2)

d1=Demo2(20,20)
d1.add()
print("=========Without Parameter ===============")

class Demo3:
    def __init__(self):
        self.a=20
        self.b=10

    def sub(self):
        print("Subtraction=",self.a-self.b)

    @staticmethod
    def add1(a,b):
        print("Addition=",a+b)

d3=Demo3()
d3.sub()

Demo3.add1(30,30)






























