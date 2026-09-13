print("======Method Overloading==========")

class Demo1:

    def add(self,n1=0,n2=0,n3=0,n4=0,n5=0):
        print("Addition =",n1+n2+n3+n4+n5)

D=Demo1()
D.add(50)
D.add(40,40)
D.add(30,30,30,)
D.add(20,20,20,20)
D.add(10,10,10,10,10)
print("==========================================")
class Demo2:
    def info(self,EmpName="Akshay",EmpId=3218,EmpCTC=800000):
        print("Student Info =",EmpName ,"+", EmpId ,"+" ,EmpCTC)

D2=Demo2()
D2.info("Sagar")

D2.info("Sagar",3219,900000)
