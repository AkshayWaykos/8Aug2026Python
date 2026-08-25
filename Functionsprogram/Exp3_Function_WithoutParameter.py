print("======Function without Param============")
def function1():
    num1=20
    num2=30
    sum=num1+num2
    print("Addition of 2no =" ,sum)
function1()
print("============Multiplication of 2 no===================")

def mul():
    mul1=3
    mul2=2
    total=mul1*mul2
    print("Multiplication of 2 no =",total)
mul()
print("=======No print from 1 to 10(withoutparamFunction)=========")
def numprint():
    for i in range(1,11):
        print(i)
        i+=1
numprint()
print("============5 ka table print ho aaisa code likho=========")

def table():
    i=5
    while i<=50:
        print(i)
        i+=5
table()
print("=================print msg in out=====================")
def greet():
    print("Hello")
    print("Welcome to Python")
greet()
print("===================5 table in diff way===================================")

def table():
    i = 1
    while i <= 10:
        print(f"5 x {i} = {5*i}")
        i += 1
table()
print("======================8 table ================================")

def Eight_table():
    i=1
    while i<=10:
        print(f"8 * {i} = {8*i}")
        i+=1
Eight_table()

print("======================2 table ================================")

def two_table():
    i=2
    while i<=10:
        print(f"2 *{i} ={ 2 * i }")
        i+=1
two_table()

print("======================Pattern Program ================================")

def Pattern():
    s=1
    while s<=10:
        print("# "*s)
        s+=1
Pattern()
print("====================== 65 table ================================")
def table65():
    s=1
    while s<=10:
        print(f"65 * {s} = {65 * s}")
        s+=1
table65()
print("====================== function using if_else========================")

def Conditionalstatements():
    mark=84
    if mark>=85:
        print("CLass A ")
    elif mark>=80 and mark<85:
        print("Class B")
    elif mark>=70 and mark<80:
        print("Class C")
    else:
        print("Only Pass")
Conditionalstatements()
print("==============================================")













