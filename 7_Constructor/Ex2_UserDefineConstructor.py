print("===Ex1 - User Define Constructor(withoutParameter)===")

#user defined constructor
#use1: copy all the members of class into object
class Sample1:

    def __init__(self):
        print("Executing User Define Constructor")

    def m1(self):
        print("Method m1 has been executed")
    def m2(self):
        print("Method m2 has been executed")

s1=Sample1()
s1.m1()
s1.m2()

print("===Ex2 - User Define Constructor(withParameter)===")

class studentInfo:

    def __init__(self,name):
        print("Running user defined constructor=",name)

si=studentInfo("Akshay")

print("===Ex3 - User Define Constructor(without Parameter)===")

class Sample2:

    def __init__(self):
        self.a=10
        self.b=20
    def add(self):
        total1 = self.a+self.b
        print("Addition of two no =",total1)

    def mul(self):
        total2 = self.a * self.b
        print("Multiplication of two no =",total2)

s2=Sample2()
s2.add()
s2.mul()















