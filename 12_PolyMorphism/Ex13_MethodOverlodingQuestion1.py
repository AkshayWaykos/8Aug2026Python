print("===============================")
# Q .Create a class Calculator with a method add.
# It should work like this:
# If you give 2 numbers, it should add them: add(2, 3) -> 5
# If you give 3 numbers, it should add all 3: add(2, 3, 4) -> 9

#First Way --->
class Calculator:
    def add(self,num1=0,num2=0,num3=0):
        print("Addition =",num1+num2+num3)

c=Calculator()
c.add(2,3)
c.add(2,3,4)

print("===============================")

#Second Way --->

class Caculater1:
    def multiplication(self,*args):
        print("Multiplication=",sum(args))

c1=Caculater1()
c1.multiplication(20,20)
c1.multiplication(20,30,30)


