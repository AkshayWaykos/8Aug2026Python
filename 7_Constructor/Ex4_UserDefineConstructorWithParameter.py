print("====Ex1_User Define Constructor(with Parameter)====")

class Sample():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        print("Addition =",self.x+self.y)

s=Sample(20,20)
s.add()

print("====Ex2_User Define Constructor(with Parameter)====")

class Sample2():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition =",self.a+ self.b)

s2=Sample2(10,20)
s2.add()
print("====Ex2_User Define Constructor(with Parameter)====")

class Calculation():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def addition(self):
        print("Addition=",self.x+self.y)

C1=Calculation(20,20)
C1.addition()

print("====Ex3_User Define Constructor(With Parameter)====")

class Math():
    def __init__(self):
        pass
    def mul(self,s,t):
        print("Multiplication =",s*t)

M=Math()
M.mul(20,20)

print("====Ex4_User Define Constructor(With Parameter)====")

class StudentName():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("Student Name =",self.name)
        print("Student Age  =",self.age)

S1=StudentName("Akshay",31)
S1.info()




























