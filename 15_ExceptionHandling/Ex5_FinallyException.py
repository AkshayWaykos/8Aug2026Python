
print("finally – (Optional) Executes code regardless of whether an exception occurs")

try:
    n1=10
    n2=0
    print(n1/n2)
except Exception:
    print("Generic Exception Handled")
finally:
    print("Finally Block Executed")

print("======================================")

age=2
if age<18:
    raise Exception("Age is less than 18")
else:
    print("age is grater than 18")
print("======================================")
try:
    p=10
    q=0
    print("division=",p/q)
except ZeroDivisionError:
    print("Division =",p/2)
finally:
    t=10
    s=20
    print("Finally Block code executed")
    print("Addition =",t+s)