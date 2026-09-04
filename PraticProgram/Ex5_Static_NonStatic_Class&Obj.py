from Functionsprogram.Exp16_Funciton_WithMultupleReturnType import match
from Functionsprogram.Exp2_Function_WithParameter import addition

print("====Non static method in class without Parameter===")
class Sample:
    def add(self):
        x=10
        y=20
        print("Addition of no =",x+y)
    def student(self):
        name="Akshay"
        age=31
        print("Details of student =",name,age)
s1=Sample()
s1.add()
s1.student()
print("===Non static method in class with Parameter===")

class Sample2:
    def m1(self,num1,num2):
        total=num1+num2
        print("Addition of 2 no =",total)
    def m2(self,num1,num2):
        total=num1*num2
        print("Multiplication = ",total)
s2=Sample2()
s2.m1(20,20)
s2.m2(30,30)

print("====Static method in class without Parameter===")

class Sample3:
    @staticmethod
    def method1():
        A=20
        B=20
        C=A+B
        print("Addition =",C)
    @staticmethod
    def method2():
        name="Akshay"
        age=31
        print("Student Details =",name,age)
Sample3.method1()
Sample3.method2()
print("====Static method in class with Parameter===")

class Sample4:
    @staticmethod
    def sub(num1,num2):
        print("Subtraction =",num1-num2)

    @staticmethod
    def mul(num1,num2):
        print("Multiplication =",num1*num2)
s4=Sample4()
s4.sub(40,20)
s4.mul(40,40)

print("======Positional Parameter======")

def details(name,age):
    print("StudentName =",name ,"Age =",age)

details("Akshay",31)
details(31,"Akshay")

print("======Keywaord Parameter======")

def details2(name,age):
    print("Name =",name," Age =",age)

details2(name="Akshay",age=31)
details2(age=21,name="Sagar")

print("======default Parameter======")

def details3(name,age=31):
    print(name,age)

details3(name="Akshay")
details3(name="Sagar",age=21)

print("======default Parameter======")






















