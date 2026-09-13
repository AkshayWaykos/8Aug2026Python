print("=====Company Details=====")

class Demo1:

    CompanyName="TCS industry"

    def __init__(self,EmpName,EmpID):
        self.EmpName=EmpName
        self.EmpID=EmpID

    def method(self):
        print("Employee Name =",self.EmpName)
        print("Employee ID=",self.EmpID)
        print("Company Name =",Demo1.CompanyName)

d1=Demo1("Akshay",30)
d1.method()
print("-------------------")
d1=Demo1("Sagar",28)
d1.method()