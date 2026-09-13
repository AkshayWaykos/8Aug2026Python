print("===Single Level Inheritance with parameter===========")

class Sample1:
    def add(self,num1,num2):
        print("Addition = ",num1+num2)

class Sample2(Sample1):
    def mul(self,num3,num4):
        print("Multiplication=",num3*num4)

s1=Sample2()
s1.add(10,10)
s1.mul(20,20)

print("===Multilevel Inheritance with parameter===========")

class Father:
    def info1(self,name,age):
        print("Father Details =",name,age)
class Mother(Father):
    def info2(self,name,age):
        print("Mother details=",name,age)
class son(Mother):
    def info3(self,name,age):
        print("Son Details=",name,age)

s1=son()
s1.info1("Akshay",31)
s1.info2("Sagar",31)
s1.info3("Shiva",33)


print("===Hierarchical Inheritance with parameter===========")

class BigBro:
    def fun1(self,car):
        print("BigBrother = ",car)

class brother2(BigBro):
    def fun2(self,bike):
        print("brother2 bike =",bike)

class brother3(BigBro):
    def fun3(self,laptop):
        print("brother3 laptop=",laptop)

b2=brother2()
b2.fun1("BMW")
b2.fun2("KTM")

b3=brother3()
b3.fun1("BMW")
b3.fun3("ASUS")


print("===Multiple Inheritance with parameter===========")

class Demo1:
    def addition(self,num1,num2):
        print("Addition =",num1+num2)

class Demo2:
    def multiplication(self,num3,num4):
        print("Multiplication=",num3*num4)

class Demo3(Demo1,Demo2):
    def Divination(self,num5,num6):
        print("Divination =",num5 / num6)

d3=Demo3()
d3.addition(20,20)
d3.multiplication(30,30)
d3.Divination(30,3)

print("==================================================")




















