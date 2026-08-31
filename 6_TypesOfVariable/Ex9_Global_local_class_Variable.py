print("========Ex9_Global_local_class_Variable================")

num1=10                   #Global Variable

class Test1():
    num2=20                  #class Variable
    def fun1(self):
        num3=30              #local variable

        print("Global Variable=",num1)         #Calling Global Variable
        print("Local variable=",num3)          #calling local variable
        print("Class Variable=",self.num2)       #Calling Class Variable

    @staticmethod
    def fun2():
        num4=40
        print("Global Variable=",num1)         #Calling Global Variable
        print("Local variable=", num4)         #Calling local variable
        print("Class Variable=", Test1.num2)    #Calling Class Variable

T1=Test1()
T1.fun1()
print("-----------------")
Test1.fun2()

print("========Global Variable================")

no1=10
no2=20

def add():
    total=no1+no2
    print("Addition of global variable =",total)
add()

print("========Global_local_class_Variable================")

a=10

def sample1():
    b=20
    print("Global =",a)
    print("local variable=",a)

class Test2():
    c=30
    def sample2(self):
        d=40
        print("Global =",a)
        print("local variable=",d)
        print("class variable=",self.c)

sample1()

t2=Test2()
t2.sample2()

























