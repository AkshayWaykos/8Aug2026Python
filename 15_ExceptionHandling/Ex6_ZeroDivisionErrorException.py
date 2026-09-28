from pip._internal.models import index

print("===================================")

try:
    n1=10
    n2=0
    print("Division=",n1/n2)
except ZeroDivisionError:
    print("ZeroDivision Exception Error")

print("===================================")
try:
    a=10
    b=0
    print("Division =",a/b)
except ZeroDivisionError:
    print("Zero Division Exception Handled")

print("===================================")

try:
    num1=20
    num2=0
    print("Division=",num1/num2)
except Exception as s1:
    print(s1)
print("===================================")

try:
    p=10
    q=0
    print("division=",p/q)
except ZeroDivisionError:
    print("Division =",p/2)
    print("Zero division Exception not Handled here bcoz operation perform")


