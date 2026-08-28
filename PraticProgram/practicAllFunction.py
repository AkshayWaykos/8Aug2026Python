#Function without parameter
print("=====Function without Parameter======")
def Function1():
    num1=20
    num2=30
    total=num1+num2
    print("Addition = ",total)

Function1()
print("=======Function with Parameter==========")

#Function with Parameter
def Function2(num1,num2):
    mul=num1*num2
    print("Multiplication =" , mul)

Function2(20,10)

print("=======Function with single return type=========")

#Function with single return type

def Function3(num1,num2):
    num3=num1/num2
    print("Division = ",num3)

Function3(20,10)

print("=======Function with Multiple return type=========")

#Function with multiple return type
def Function4(num1,num2):
    add=num1+num2
    mul=num1+num2
    print("Addition = ",add)
    print("Multiplication =", mul)

Function4(20,20)
print("========")
Function4(10,10)

print("======Function with Multiple return type=======")

#Function with Positional Parameter
def StudentInfo(name,age):
    print(name,age)

StudentInfo("Akshay",21)
StudentInfo(21,"Akshay")

print("=====Function with Key Word Parameter=====")

#Function with Key Word Parameter
def EmpInfo(name,age):
    print(name,age)

EmpInfo(name="Akshay",age=21)
EmpInfo(age=32,name="Akshay")

print("=======Default Optional Parameter=======")

def Employee(name,age=21):
    print(name, age)

Employee(name="Sagar")
Employee(name="Akshay",age=31)














