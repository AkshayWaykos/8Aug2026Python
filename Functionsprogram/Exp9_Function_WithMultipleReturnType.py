print("========Function with Multiple Return Type ============")

def arithmaticoperation(n1,n2):
    add=n1+n2
    mul=n1*n2
    return add,mul
n3,n4=arithmaticoperation(20,30)
print("Addition of to no =",n3)
print("Multiplication of no =",n4)
print("=======================================================")
def twooperation(num1,num2):
    mul=num1*num2
    sub=num1-num2
    return mul,sub

Mul,Sub = twooperation(20,10)
print("Multiplication = ",Mul)
print("Subtraction  = ",Sub)
print("=======================================================")

def studentinfo(name,age):
    details1 = name
    details2 = age
    return name,age

info=studentinfo("Akshay",21)
print(info)
print("=======================================================")

def arithmaticoperation2(no1,no2):
    div=no1/no2
    add=no1/no2
    return div,add
math1,math2=arithmaticoperation(20,10)
print("Division of to no=",math1)
print("Addition of to no=",math2)

print("=======================================================")

def function2(n1,n2):
    add= n1+n2
    mul= n1+n2
    return add,mul

total1,total2=function2(10,20)
print("addition of 2 no =",total1)
print("Multiplication of 2 no =",total2)

print("=======================================================")




























