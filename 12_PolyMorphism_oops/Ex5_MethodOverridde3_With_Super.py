
print("===Method Override_With_Super(with same MethodName)=====")

class Sample1:
    def m1(self):
        print("M1 method executed from Sample1 Class")

class Sample2(Sample1):
    def m2(self):
        super().m1()
        print("M2 Method executed from Sample2 class")

S2=Sample2()
S2.m2()

print("====Method Override_With_Super(With Diff Name)=======")

class Father:
    def home(self):
        print("Father 1 BHK")
    def car(self):
        print("Father car")

class Son(Father):
    def bike(self):
        print("Son Bike")

    def home(self):
        super().home()
        super().car()
        print("Father 1 BHK")
S=Son()
S.bike()
S.home()

print("====Method Override_With_Super(With Diff Name)=====")

class Demo1:
    def add(self,a,b):
        print("Addition = ",a+b)

    def mul(self,x,y):
        print("Multiplication = ",x*y)
class Demo2(Demo1):
    def div(self,s,t):
        print("Division = ",s/t)

    def sub(self,p,q):
        print("Subtraction =",p-q)

D2=Demo2()
D2.add(30,30)
D2.mul(20,20)
D2.div(20,10)
D2.sub(50,40)

print("====Method Override_With_Super(With Diff Name)====")

class Sample1:
    def home(self):
        print("home 1 executed from Sample 1")
    def car(self):
        print("car 2 executed from Sample 1")
class Sample2(Sample1):
    def bike(self):
        print("bike 1 executed from Sample 2 ")
    def home(self):
        print("home 2 executed from sample 2")

        super().home()
        super().car()

S2=Sample2()
S2.bike()
S2.home()

print("=================================================")