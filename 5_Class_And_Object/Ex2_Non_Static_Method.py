from Functionsprogram.Exp8_Function_WithSingleReturnType import addition

print("================Ex2:Non static Method =================")

class Demo:
   def addition1(self,num1,num2):
    num3=num1+num2
    print(num3)

   def addition2(self,num4,num5):
    num6=num4+num5
    print(num6)

D1=Demo()
D1.addition1(10,20)
D1.addition2(10,20)
print("=======")
D2=Demo()
D2.addition1(20,20)
D2.addition2(30,30)

