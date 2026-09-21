print("=============Function with multiple return type===============")

def fun1(num1,num2):
    add=num1+num2
    mul=num1*num2
    return add,mul

A,M=fun1(10,20)
print("Addition =", A)
print("Multiplication=", M)

print("==============function with single return type================")

def fun2(num2,num3):
    sub=num2-num3
    return sub

s=fun2(30,20)
print("Subtraction =",s)

print("==============function with multiple return type================")

def f1(name,age):
    return name,age

N,A=f1("Sagar",29)

print("Student name =",N)
print("Student age=",A)

print(f1("shiva",33))
print(f1("Akshay",31))

print("=====Function with single/multiple return type===========")

class Demo:
    def studentinfo(self,name,age):
        return name,age

D=Demo()
n,a=D.studentinfo("Akki",21)
print("Student Name & age =",n,a)

print("=====Function with single/multiple return type===========")

class Demo1:
    def m1(self,n1,n2):
        add=n1+n2
        mul=n1*n2
        return add,mul
d1=Demo1()
a1,m=d1.m1(20,20)

print("Addition =",a)
print("Multiplication=",m)
print("===================================================")

class math:
    def add(self,num1,num2):
        total=num1+num2
        return total

m=math()
t=m.add(20,30)
print("Addition=",t)
print("===================================================")
class Sample:
    def method(self,name,age):
        return name,age

S=Sample()
n,a=S.method("Sagar",21)
print("Student Name & age =",n,a)
print(S.method("akki",21))
print(S.method("shiva",33))

print("===================================================")

class Company:
    def emp1(self,name,age):
        return name,age

c=Company()
N,A=c.emp1("Kiaynsh",31)
print(c.emp1("Akki",21))
print(c.emp1("Trutpi",20))
























































