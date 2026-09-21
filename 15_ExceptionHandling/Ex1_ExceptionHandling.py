print("======Zero DivisionError Exception Handling=============")
#Example 1
try:
    n1=10
    n2=0
    total=n1/n2
    print("Division =",total)
except ZeroDivisionError:
    print("ZeroDivisionError Handling")

print("Program Ended")

print("---------Alternate way-----------------")

#Exception 2

try:
    n1=20
    n2=0
    div=n1/n2
    print("Multiplication =",div)
except ZeroDivisionError:
    print(n1/2)
    print("ZeroDivisionError Handling")

print("Program Ended")

print("---------Alternate way-----------------")

#Example to print what exception we are going to handle with Generic Exception
n1=10
n2=0
try:
    n3=n1/n2
    print(n3)
except Exception as s1:
    print(s1)
    print("Generic Exception")
print("Program End")

print("---------Alternate way-----------------")

num1=20
num2=0
try:
    num3=num1/num2
    print("Division =",num3)
except Exception as s1:
    print(s1)
    print(num1/5)
    print("Generic Exception")

print("---------Alternate way-----------------")

num1=20
num2=0
try:
    num4=num1/num2
except ValueError as s1:
    print(s1,"Value Error exception")
except ZeroDivisionError as s2:
    print(s2, "Zero Div Exception")

print("Program End")














