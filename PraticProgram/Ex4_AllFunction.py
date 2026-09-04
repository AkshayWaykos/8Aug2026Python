from Functionsprogram.Exp8_Function_WithSingleReturnType import addition

print("===Function without Parameter===")

def info1():
    print("student Name = Akshay")
def add():
    a=10
    b=20
    total=a+b
    print("Addition =",total)
info1()
add()
print("===Function with Parameter===")

def details(name,age):
    print("Student Name =",name)
    print("Student Age =", age)
def mul(num1,num2):
    total1=num1*num2
    print("Multiplication =",total1)
details("Akshay",31)
mul(20,20)

print("===Function with Single return type without parameter===")

def add():
    addition=num1+num2
    print("Addition =",addition)
    return addition

ad1=addition(20,20)
ad2=addition(10,10)

print("Addition=",ad1)
print("Addition=",ad2)

print("===Function with Multiple return type with parameter===")

def operation(num1,num2):
    add1=num1+num2
    mul1=num1*num2
    return add1,mul1

ad,mu=operation(20,20)

print("Addition =",ad)
print("Multiplication=",mu)
print("===Function with Multiple return type with parameter===")


def demo(name,age):
    info1 = name
    info2 =age
    return info1,info2
in1,in2=demo("Akshay",31)
print("Student Name =",in1)
print("Student Age =",in2)
print("====================================================")






