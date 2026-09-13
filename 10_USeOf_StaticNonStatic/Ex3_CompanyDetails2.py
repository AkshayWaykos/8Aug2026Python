
print("==1: Write a code to store 5 employee details =====")

class Company:

    CompnyName="XYZ PVT LIM Company"
    CEOName="Vijay Thalapathy"

    def __init__(self,EmpName,EmpId,EmpCTC):
        self.EmpName=EmpName
        self.EmpId=EmpId
        self.EmpCTC=EmpCTC

    def employeeDetails(self):
        print("Employee Name =",self.EmpName)
        print("Employee ID = ",self.EmpId)
        print("Employee CTC =",self.EmpCTC)
        print("Company Name =",Company.CompnyName)
        print("Company CEO  =",Company.CEOName)

print("Employee= 1")
c1=Company("Akshay",1001,800000)
c1.employeeDetails()
print("Employee= 2")
c2=Company("SAGAR",1002,900000)
c2.employeeDetails()
print("Employee= 3")
c3=Company("SHIVA",1003,700000)
c3.employeeDetails()
print("Employee= 4")
c4=Company("AMOL",1004,500000)
c4.employeeDetails()
print("Employee= 5")
c5=Company("RAHUL",1005,900000)
c5.employeeDetails()

