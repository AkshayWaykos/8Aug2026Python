
print("=============Function with Single Return Type====================")

def addition(num1,num2):
    num3=num1+num2
    return num3

num4=addition(10,20)
print(num4)
num4=addition(20,20)
print(num4)
num4=addition(30,20)
print(num4)
print("=============Subtraction====================")

def sub(num1,num2):
    num3=num1-num2
    return num3

print("FunctionWithReturnType=",sub(20,10))
print("FunctionWithReturnType=",sub(20,5))

print("=============Multiplication====================")

def mul(mul1,mul2):
    mul3=mul1*mul2
    return mul3
mul4=mul(20,20)
print(mul4)
print("============")
print(mul(20,5))
print("=============Name wala Program====================")

def studentinfo(name):
    return name

info=studentinfo("Akshay")
print(info)

print(studentinfo("Sagar"))
print(studentinfo("Sagar"))
print("=============Name wala Program====================")

def function1(name,age):
    return "Name=", name,"Age =", age

info=function1("Akshay",31)
print(info)
print("------------")
print(function1("Sagar",29))

print("=============Addition wala Program====================")

def addition(num1,num2):
    total=num1+num2
    return total

add=addition(10,20)
print(add)
print("-------------")
print("Addition of 2 no =",addition(20,20))

print("=============Substraction wala Program====================")

def substraction(sub1,sub2):
    answer=sub1-sub2
    return answer

sub=substraction(30,20)
print(sub)
print("-------------")
print("substraction of 2 no =",substraction(40,10))

print("=====================================================")
