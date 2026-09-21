
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
