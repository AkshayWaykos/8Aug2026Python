print("=====Ex 1: Function With Single Value Return =============")

def add():
    x=10
    y=20
    addition=x+y
    print("Addition = ",addition)
    return addition
ad=add()
print("=====Ex2:Function with Multiple value return==========")

def math(num1,num2):
    total1=num1+num2
    total2=num1+num2
    return total1,total2

t1,t2=math(20,30)
print("Addition =",t1)
print("Multiplication=",t2)
print("=====Ex3:Function with multiplication return ==========")

def sample(a,b):
    addition = a+b
    multiplication = a+b
    return addition,multiplication

a,m=sample(30,30)
print("Addition =",a)
print("Multiplication=",m)

print("=====Ex4:Function with multiplication return ==========")

def student():
    name="Akshay"
    age=31
    return name,age

n,a=student()
print("Student=",n)
print("age=",a)

print("=====Ex5:Function with multiplication return ==========")

def details():
    name="Sagar"
    age=31
    roll=101
    clg="DVD clg"

    return name,age,roll,clg
n,a,r,c=details()
print("Student =",n)
print("Age =",a)
print("Roll no=",r)
print("Collage Name=",c)

print("=====================END======================")
























