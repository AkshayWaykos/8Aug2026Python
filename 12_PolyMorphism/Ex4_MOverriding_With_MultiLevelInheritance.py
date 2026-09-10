from tokenize import Single3

print("===Method Overriding with MultiLevel Inheritance=========")

class Sample1:
    def total(self):
        a,b=10,10
        print("Addition =",a+b)
class Sample2(Sample1):
     def total(self):
         x, y = 20, 20
         print("multiplication=",x*y)
class Sample3(Sample2):
    def total(self):
        p, q = 30, 30
        print("Division=",p+q)

S3=Sample3()
S3.total()
print("===Method Overriding with MultiLevel Inheritance=========")

class GrandFather:
    def money(self):
        print("GrandFather Money = 5L")
class Father(GrandFather):
    def money(self):
        print("Father Money = 7L")
class son(Father):
    def money(self):
        print("Son Money = 10L")

s=son()
s.money()
print("===Method Overriding with MultiLevel Inheritance(with Param)=========")

class Student1:
    def total(self,num1,num2):
        print("Addition=",num1+num2)
class Student2(Student1):
    def total(self,num1,num2):
        print("Subtraction=",num1-num2)
class Student3(Student2):
    def total(self,num1,num2):
        print("Multiplication =",num1*num2)

S3=Student3()
S3.total(20,20)

print("=================================================================")





















