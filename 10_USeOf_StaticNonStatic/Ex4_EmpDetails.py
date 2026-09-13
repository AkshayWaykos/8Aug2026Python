print("=======Use static non static ========")

class Demo1:

    collage="SB Collage"
    team="GangZero"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("Student Name =",self.name)
        print("Student Age = ",self.age)
        print("Collage Name =",Demo1.collage)
        print("Student Team =",Demo1.team)

    @staticmethod
    def info2():
        print("Static Method")
d1=Demo1("Akshay",31)
d1.info()
print("--------------")
Demo1.info2()
