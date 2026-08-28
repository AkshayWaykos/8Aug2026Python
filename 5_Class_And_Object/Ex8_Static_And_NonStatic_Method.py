
print("=======Non-Static Method(without Parameter)==========")

class StudentInfo():
    def Method1(self):
        print("Method 1 ")

    def Method2(self):
        print("Method 2")
S1=StudentInfo()
S1.Method1()
S1.Method2()

print("=======Non Static Method(with Parameter)==========")

class addition():
    def Method3(self):
        print("Method 3")
    def Method4(self):
        print("Method 4")
A=addition()
A.Method3()
A.Method4()
print("=======Static Method(with Parameter)==========")

class ArithmaticOpe():
    @staticmethod
    def Addition(num1,num2):
        num3=num1+num2
        print("Addition of =", num3)
    @staticmethod
    def Substraction(num1,num2):
        num3=num1*num2
        print("Substraction =", num3)

ArithmaticOpe.Addition(10,10)
ArithmaticOpe.Substraction(20,20)

print("=======Static Method(with Parameter)==========")
class Velocity():
    @staticmethod
    def StdentInfo(name,age):
        print("Student Name =",name,"|","Student Age =",age)

    @staticmethod
    def StudentSubject(sub1,sub2):
        print("Subject 1= ",sub1, "|","Subject 2=",sub2)

Velocity.StdentInfo("Akshay",31)
Velocity.StudentSubject("English","Math")

print("=======Static Method(without Parameter)==========")

class College():
    @staticmethod
    def Method1():
        print("Method1 Executed")
    @staticmethod
    def Method2():
        print("Method2 Executed")
College.Method1()
College.Method2()

print("=======Non-Static/Static Method(Without Parameter)==========")

class Company1():
    def Sample1(self):
        print("Sample1 Method from Non Static method")
    @staticmethod
    def Sample2():
        print("Sample2 Method from Static method")

C1=Company1()
C1.Sample1()
Company1.Sample2()

print("=======Non-Static/Static Method(With Parameter)==========")

class StudInfo():
    @staticmethod
    def DemoMethod1(name,age):
        print("Name = ",name ,"Age =" ,age)

    @staticmethod
    def DemoMethod2(num1,num2):
        num3=num1+num2
        print("Addition of no =",num3)
StudInfo.DemoMethod1("Akshay",31)
StudInfo.DemoMethod2(10,20)





























