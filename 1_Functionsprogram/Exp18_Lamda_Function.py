print("========lambda Function===========")

class Demo:
    mul=lambda self,x,y: x * y


d1=Demo()
print("Multiplication = ",d1.mul(10,10))

print("===================================")

div=lambda s,t:s/t
print(div(10,5))

print("===================================")

add1=lambda A,B:A+B
print(add1(20,20))

print("===================================")

# Normal function
def add(a, b):
    return a + b
print("==============================")
# Same thing in Lambda
add11 = lambda a, b: a + b
print(add11(2,3)) # 5


print("===================================")



















