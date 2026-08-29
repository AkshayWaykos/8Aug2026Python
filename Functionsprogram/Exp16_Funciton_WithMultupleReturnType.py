print("=====Function with Multiple return(without Parameter)=====")
#Function with Multiple return without parameter
def function11():
    num1=20
    num2=30
    add=num1+num2
    mul=num1+num2
    return add,mul

add,mul=function11()
print("Addition = ",add)
print("Multiplication =",mul)
print("=====Function with Multiple return(without Parameter)=====")
#Function with Multiple return without parameter

def match(num1,num2):
    sub=num1-num2
    div=num1/num2
    return sub,div

sub,div=match(20,10)
print("Subtraction =",sub)
print("Division =", div)

print("=====Function with Multiple return(with Parameter)=====")
#Function with Multiple return with parameter

def addition(num1,num2):
    num3=num1+num2
    num4=num1*num2
    return num3,num4

add,mul=addition(20,10)
print("Addition = ",add)
print("Multiplication =",mul)

add,mul=addition(30,30)

print("Addition = ",add)
print("Multiplication =",mul)

print("=====End=====")


















