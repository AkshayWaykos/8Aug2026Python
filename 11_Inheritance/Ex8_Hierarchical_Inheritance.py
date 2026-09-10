print("======Hierarchical Inheritance=======")

class Father:
    def money(self):
        print("Money = 5L")

    def home(self):
        print("Home = 2 BHK")

class son1(Father):
    def bike(self):
        print("bike = KTM")

class son2(Father):
    def car(self):
        print("Car = BMW")

s1=son1()
s1.money()
s1.home()
s1.bike()

print("--------------")

s2=son2()
s2.money()
s2.home()
s2.car()
print("======Hierarchical Inheritance(with Param)=======")

class Boss:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition of Boss Class = ",self.num1+self.num2)

class Emp1(Boss):
    def mul(self,num1,num2):
        print("Multiplication of Emp Class=",num1*num2)

class Emp2(Boss):
    def div(self,num1,num2):
        print("Division of Emp 2 Class =",num1/num2)

e1=Emp1(30,30)
e1.add()
e1.mul(10,10)
print("----------------------")
e2=Emp2(20,20)
e2.div(20,5)










































