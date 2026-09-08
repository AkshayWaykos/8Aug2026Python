from pydoc import classname

print("========Student Details===========")

class Student:

    collageName="XYZ"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def Info(self):
        print("Student Name =",self.name)
        print("Student ROllno=",self.roll)
        print("Class Name =", Student.collageName)

s1=Student("Akshay",101)
s1.Info()

print("========Employee Details===========")
#Use Of static and Non-static Variable
class CompanyDetails:

    companyName="ABCD PVT LIM"

    def __init__(self,EmpName,EmpId):
        self.EmpName=EmpName
        self.EmpId=EmpId

    def EmpInfo(self):
        print("Employee Name =",self.EmpName)
        print("Employee ID =",self.EmpId)
        print("Comapny Name=",CompanyDetails.companyName)

c1=CompanyDetails("Akshay",1234)
c1.EmpInfo()
print("---------")
c2=CompanyDetails("Amol",4567)
c2.EmpInfo()
print("---------")
c2=CompanyDetails("Rahul",8901)
c2.EmpInfo()
print("---------")







