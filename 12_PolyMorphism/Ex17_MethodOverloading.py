print("=============Method Overloading==")

class Math:
    def add(self,num1=0,num2=0,num3=0):
        print("Addition=",num1+num2+num3)

m1=Math()
m1.add(10,10,10)
m1.add(20,20)
m1.add(10)

print("============Method Overloading==")

def fun(n1=0,n2=0):
    print("Multiplication=",n1*n2)

fun(20,20)

print("==============Method Overloading==")
class Sample:

    def info(self,Fname,Lname,roll):
        print("Student F&LName =",Fname,Lname)
        print("Student roll = ",roll)

S1=Sample()
S1.info("Akshay","Waykos",101)

print("===========Method Overloading==")

class Sample1:
    def add(self,a=10,b=20):
        print("Addition=",a+b)
        print("Mutliplication=",a*b)

s1=Sample1()
s1.add()
print("===========Method Overloading==")























