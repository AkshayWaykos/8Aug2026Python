print("=====lamda Function======")

add=lambda x,y: x * y
print(add(10,10))
print(type(add))

print('================================')

class Demo:
    mul1=lambda self,a,b:a+b
    mul2=lambda self,a,b:a+b

d=Demo()
print("Addition 1 =",d.mul1(10,20))
print("Addition 2 =",d.mul2(30,30))

print('================================')

class Demo1:
    add1=lambda self,x,y: x+y   #lamda function
    mul1=lambda self,p,q: p*q
    div1=lambda self,s,t: s/t

d1=Demo1()
print("Addition 1       =",d1.add1(20,20))
print("Multiplication 1 =",d1.mul1(20,30))
print("Division 1       =",d1.div1(20,5))
