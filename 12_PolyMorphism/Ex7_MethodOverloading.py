print("===Method Overloading(arithmetic operation)===")

class Overloading:

    def add(self,num1=0,num2=0,num3=0,num4=0):
        print("Addition =",num1 + num2 + num3 + num4)

O1=Overloading()
O1.add()
O1.add(10,20)
O1.add(40,20)
O1.add(10,10,10)
O1.add(20,30,40,40)

print("===Method Overloading(with string value)===")

class School:

    def studetnInfo(self,name="Akshay",roll="101",):
        print("Student Name =",name)
        print("Student roll=",roll)
        print("-----------------------")

S=School()
S.studetnInfo()
S.studetnInfo("Sagar",102)
S.studetnInfo("Shiva",103)
S.studetnInfo("sakshi",104)