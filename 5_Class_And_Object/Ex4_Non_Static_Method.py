print("============Ex4:Non static Method===========")

class BBB():
    def information(self):
        print("Method Info executed from BBB")


class AAA():
    def addition(self,num1,num2):
        total=num1+num2
        print("Addition = ",total)

    def multiplication(self,num1,num2):
        total=num1*num2
        print("Multiplication =",total)
    def division(self,num1,num2):
        total=num1/num2
        print("Division =",total)
    def subtrication(self,num1,num2):
        total=num1-num2
        print("Subtraction =",total)

A=AAA()
A.addition(20,20)
A.multiplication(20,30)
A.division(50,20)
A.subtrication(30,20)
print("==========")
B=BBB()
B.information()