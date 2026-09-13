print("==========User Define Constructor ==================")

class Demo1:
    def __init__(self):
        a,b=20,20
        print("Addition =",a,b)

class Demo2:
    def __init__(self,num1,num2):
        print("Multiplication =",num1+num2)

D1=Demo1()
D2=Demo2(30,30)

print("==========User Define Constructor ==================")

class Sample1:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("Addition =",self.n1+self.n2)
class Sample2:
    def __init__(self,n3,n4):
        self.n3=n3
        self.n4=n4
    def mul(self):
        print("Multiplication=",self.n3*self.n4)
class Sample3:
    def __init__(self,n5,n6):
        self.n5=n5
        self.n6=n6
    @staticmethod
    def div(n5,n6):
        print("Addition =",n5/n6)

s1=Sample1(10,10)
s1.add()
s2=Sample2(20,20)
s2.mul()
Sample3.div(30,3)


























