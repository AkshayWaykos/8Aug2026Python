print("======Ex1-User Define Constructor=======")

class StudentDetails:
    def __init__(self):
        self.name ="Akshay"
        self.age  =31
        self.roll=101
        self.x=30
        self.y=30

    def info(self):
        print("Student Name =",self.name)
        print("Student Age =",self.age)
        print("Roll no = ",self.roll)

    def addition(self):
        print("Addition =",self.x+self.y)

S=StudentDetails()
S.info()
S.addition()
