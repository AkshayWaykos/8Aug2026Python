print("====User Define constructor with Parameter===")

class Sample():
    def __init__(self,name,age,roll,x,y,z):
        self.name = name
        self.age = age
        self.roll = roll
        self.x=x
        self.y=y
        self.z=z

    def details(self):

        print("Student Name =",self.name)
        print("Student age  =",self.age)
        print("Student roll =",self.roll)

    def addtion(self):

        print("Addition1=",self.x+self.y)
        print("Addition2=",self.x+self.z)

ss=Sample("Akshay",32,101,20,20,20)
ss.details()
ss.addtion()
