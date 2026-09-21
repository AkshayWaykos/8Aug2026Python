print("===========================")
class Demo1:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Addition=",self.num1 + self.num2)

    @staticmethod
    def mul(num1,num2):
        print("Multiplication=",num1 * num2)

d1=Demo1(10,10)
d1.add()

Demo1.mul(20,20)

print("===========================")
n1=10
n2=0
try:
    print(n1/n2)
except ValueError:
    print("Value Error Exception")
except ZeroDivisionError:
    print("Zero Division Error")

print("===========================")

class Demo2:
    def m1(self):
        print("Non Static Method m1 Demo2=object required")

    @staticmethod
    def m2():
        print("Static Method m2 Demo2 = object not required")

D2=Demo2()
D2.m1()

Demo2.m2()

print("===========================")


str ="my name is akshay "

print(str.strip())  #remove space

print(str.upper())  #Make it in upper case
print(str.isupper()) #True/False

print(str.lower())  #Make it in lower case
print(str.islower()) #true/False

print(str.title())
print(str.istitle())

print(str.isdecimal())

print(str.count("is"))

print(str.join(["Akshay"]))

print(str.replace("akshay" , "sagar"))

print(str.startswith("my"))
print(str.endswith("akshay"))


l1=["pune","mumbai","pune","buldhana"]

print(l1.count("pune"))

print("===================")

#method Overriding

class Demo1:
    def add(self,num1,num2):
        print("Addition = ", num1+num2)
class Demo2(Demo1):
    def add(self,num1,num2):
        print("Multiplication=",num1 * num2)

D2=Demo2()
D2.add(20,20)


class Father:
    def Home(self):
        print("2BHK")
print("===================")
class Son(Father):
    def Home(self):
        print("3BHK")
s=Son()
s.Home()
print("===================")


#Method Overloading

class Math:
    def add(self,num1=0,num2=0,num3=0):
        print("Addition=", num1+num2+num3)

m1=Math()
m1.add(20,20)
m1.add(30,30)
m1.add(20,30,30)

print("===================")

class Math2:
    def add(self,n1=0,n2=0,n3=0):
        print("Multiplication=",n1*n2*n3)

    def div(self,n1=0,n2=0):
        print("Division =",n1/n2)

m2=Math2()
m2.add(20,20,20)
m2.div(20,5)

print("===================")

























