
print("=================Default or Optional Parameter===================")

def studentInfo(name,age=21):
    print("Student Name=",name)
    print("Student Age=",age)

studentInfo("Akshay")
print("------------------")
studentInfo("Akshay",25)

print("===============================================================")

def EmpInfo(EmpName,EmpID=3218):
    print("Employee Name =",EmpName)
    print("Employee ID =",EmpID)

EmpInfo(EmpName="Akshay")
print("------------------")
EmpInfo(EmpName="Sagar",EmpID=3219)
print("===============================================================")

def StudentDetails(name,roll=12):
    print("Student Name =",name,"-->" ,"Student roll=",roll)

StudentDetails(name="Akshay")
StudentDetails(name="Sagar",roll=29)