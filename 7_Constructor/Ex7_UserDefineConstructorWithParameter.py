print("===================================================")

class Sample:
    def __init__(self,x,y,z,a,b):
        self.name=x
        self.age=y
        self.roll=z
        self.num1=a
        self.num2=b

    def details(self):
        print("Student Name=",self.name)
        print("Student age =",self.age)
        print("Student roll =",self.roll)

    def add(self):
        print("Addition = ",self.num1+self.num2)
    def mul(self):
        print("Multiplication = ",self.num1*self.num2)
    def sub(self):
        print("Subtraction = ",self.num1-self.num2)

S=Sample("Akshay",31,101,20,20)
S.details()
S.add()
S.mul()

print("===================================================")