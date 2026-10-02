
print("==Function without Parameter ==")

def fun11():
    print("Function without Parameter")

def fun22():
    print("Function2 without parameter")

# fun11()
# fun22()
print("=======With Parameter==========")

def fun1(num1,num2):
    print("Addition=",num1+num2)

def fun2(num1,num2):
    print("Multiplication=",num1*num2)

fun1(10,10)
fun2(20,20)

print("===========With Single/Multiple , Return type=====================")

def f1(num1,num2):
    add=num1 + num2
    mul=num1 * num2
    return add,mul

# A,M=f1(30,30)
#
# print("Addition=",A)
# print("Multiplication=",M)

print("======Lambda Function without class=======")

add = lambda A,B : A+B
print("Addition=",add(10,10))

mul = lambda A=10,B=20:A+B
print("Multiplication =",mul())

print("======Lambda Function with class=======")
class sample1:
    #withParameter-Lambda Function.
    mul=lambda self,X=10,Y=20: X*Y
    # WithoutParameter-Lambda Function.
    add=lambda self,A,B : A+B

# s=sample1()
# print("Multiplication =",s.mul())
# print("Addition       =",s.add(10,20))


print("======================================")












