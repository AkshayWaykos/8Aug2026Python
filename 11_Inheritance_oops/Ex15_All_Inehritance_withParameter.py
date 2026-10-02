print("===========Single Level Inheritance==============")
class Sample1:
    @staticmethod
    def add(num1,num2):
        print("Addition =", num1+num2)

class Sample2(Sample1):
    @staticmethod
    def mul(num1,num2):
        print("Multiplication=",num1*num2)


Sample2.mul(20,20)

print("===========Multilevel Level Inheritance==============")

class Demo1:
    @staticmethod
    def m1():
        print("M1 method executed from Demo1 class ")

class Demo2(Demo1):
    @staticmethod
    def m2():
        print("M2 method executed from Demo2 class")
class Demo3(Demo2):
    @staticmethod
    def m3():
        print("M3 method executed from Demo3 class")


Demo3.m1()
Demo3.m2()
Demo3.m3()
print("===========Hierarchical Level Inheritance==============")

class Demo11:
    def method11(self):
        print("Method 11 from Demo11")

class Demo22(Demo11):
    def method22(self):
        print("Method22 from Demo22 class")
class Demo33(Demo11):
    def method33(self):
        print("Method33 from Demo33 class")
D2=Demo22()
D2.method11()
D2.method22()

D3=Demo33()
D3.method11()
D3.method33()
print("===========Multiple Level Inheritance==============")

class Sample11:
    @staticmethod
    def add1(num1,num2):
        print("Addition=",num1+num2)
class Sample22:
    @staticmethod
    def mul(num1,num2):
        print("Multiplication=",num1*num2)
class Sample33(Sample11,Sample22):
    @staticmethod
    def sub(num1,num2):
        print("Subtraction=",num1-num2)

S33=Sample33()
S33.add1(30,30)
S33.mul(20,20)
S33.sub(10,10)
print("===========End==============")








