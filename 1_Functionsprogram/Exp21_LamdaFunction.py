import ast


class Demo:
    add=lambda self, a,b:a+b
    mul=lambda self, a,b:a*b
d=Demo()
print("Addition =",d.add(10,10))
print("Multiplication=",d.mul(20,20))

print("======================================")

add1=lambda a,b:a+b
print("Addition=",add1(20,20))

mul1=lambda a,b:a*b
print("Multiplication=",mul1(10,10))

print("======================================")

sum = lambda m,n:m+n
print("Addition=",sum(10,10))
print("======================================")

info=lambda name,surname : name+surname
print(info("AKshay"," Waykos"))

print("======================================")






















