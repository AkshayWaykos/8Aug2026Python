print("=====Ex1 -Default Constructor(withoutParameter)=======")


class Sample1():
    #use 1 - copy all the member of class into object.
    #Default Constructor
    #def __init__(self):
    #    constructor body

    def addition(self):
        a=10
        b=20
        print("Addition =",a+b)

S1=Sample1()
S1.addition()

print("=====Ex2 -Default Constructor(withoutParameter)=======")


class Sample2():

    def multiplication(self):
        x,y=20,20
        print("Multiplication=",x*y)
S2=Sample2()
S2.multiplication()

print("=====Ex3 -Default Constructor(With Parameter)=======")


class Sample3():
    def substraction(self,num1,num2):
        print("substraction = ",num1-num2)

s3=Sample3()
s3.substraction(20,10)

print("=====Ex4 -Default Constructor(With Parameter)=======")

class Sample4():
    def div(self,num1,num2):
        print("Division =",num1/num2)
s4=Sample4()
s4.div(20,10)



