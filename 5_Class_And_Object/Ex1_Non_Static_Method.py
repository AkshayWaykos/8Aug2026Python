print("=====-Ex1: Example of non- static methods-======")

class Sample1:                          #class declaration
    def method1(self):                  #method declaration / #non-static
        print("Method1 executed")
    def addition(self,num1,num2): #method declaration / #non-static
        total=num1+num2
        print("Addition of no =",total)

S1=Sample1()
S1.method1()
S1.addition(20,10)
print("================================")

class Sample2:
    def add1(self,num1,num2):
        add1=num1+num2
        print("Addition of no =",add1)

    def mul1(self,num3,num4):
        mul1=num3*num4
        print("Mulktiplication of no =",mul1)
S2=Sample2()
S2.add1(20,20)
S2.mul1(20,20)
print("================================")

class ArithmaticOp():
    def add(self,num1,num2):
        num3=num1+num2
        print("Addition=",num3 )
    def sub(self,num1,num2):
        num3=num1-num2
        print("Substraction=",num3)
    def div(self,num1,num2):
        num3=num1/num2
        print("Division =",num3)
    def mul(self,num1,num2):
        num3=num1*num2
        print("Multiplication =",num3)
A1=ArithmaticOp()
A1.add(10,20)
A1.sub(20,10)
A1.div(20,10)
A1.mul(20,10)
print("======")
A2=ArithmaticOp()
A2.add(20,30)

print("================================")



















