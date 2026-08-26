#Function without parameters       --->def function()
#Function with Parameters          --->def function(name,age)
#Function with Single and multiple return value   ---> def function(name,age)     return

print("===============")
#Function without parameters       --->def function()
def function():
    num1=20
    num2=30
    total=num1+num2
    print("Addition =",total)
function()
print("===============")
#Function with Parameters          --->def function(name,age)
def function(num1,num2):
    addition=num1+num2
    print("Addition = ",addition)
function(20,20)

print("===============")
#Function with Single return value   ---> def function(name,age)     return
def function(num1,num2):
    add=num1+num2
    return add
S1=function(20,20)
print(S1)
print("===============")
#Function with multiple return value
def function(num1,num2):
    add=num1+num2
    mul=num1*num2
    return add,mul
S1,S2=function(20,20)
print(S1)
print(S2)
print("===============")
# positional Parameter

def studentInfo(name,age):
    print("Student Name =",name ,"|", "Student Age=", age)

studentInfo("Akshay",21)
studentInfo(21 ,"sagar")
print("===============")
# Keyword Parameter

def StudentInfo(name,age):
    print(name,age)
StudentInfo(name="Akshay",age=21)
StudentInfo(age=23, name="Sagar")

print("===============")
# Optional Parameter
def info(name,age=21):
    print(name,age)

info(name="Akshay")
info(name="Akshay",age=23)
print("===============")





