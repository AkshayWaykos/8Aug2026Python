print("======User Define Constructor with Static Method=======")

class Demo1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod
    def info1(Name,age):
        print("Student Name * Age =",Name , age)

class Demo2:
    def __init__(self,EmpName,EmpID):
        self.EmpName=EmpName
        self.EmpID=EmpID
    @staticmethod
    def info2(EmpName,EmpID):
        print("Employee Name & ID =",EmpName , EmpID)

Demo1.info1("Akki",31)
Demo2.info2("Sagar",101)

print("====User Define Constructor with non-static method======")

class Sample1:
    def __init__(self):
        a,b=20,20
        print("Addition=",a+b)

class Sample2:
    def __init__(self):
        x,y=20,20
        print("Multiplication=",x+y)

Sample1()
Sample2()
print("=========================================")