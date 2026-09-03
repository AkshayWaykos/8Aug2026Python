print("=======Ex8_User Define Constructor With Parameter=========")

class Sample:
    def __init__(self,a,b):
        self.name=a
        self.age=b

    def info(self):
        print("Student Name =",self.name)
        print("Student Age =",self.age)

S=Sample("Akshay",31)
S.info()


print("=========================")
class Sample:
    def __init__(self,x,y):
        self.num1=x
        self.num2=y

    def multiplication(self):
        print("multiplication =",self.num1*self.num2)

S1=Sample(20,20)
S1.multiplication()
S2=Sample(30,30)
S2.multiplication()

