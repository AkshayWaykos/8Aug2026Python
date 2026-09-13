print("==Method Overloading in Python(with Parameter)Non static Method====")

class Demo1:
    def add(self,num1=0,num2=0,num3=0,num4=0):
        print("Addition = ",num1+num2+num3+num4)

# d1=Demo1()
# d1.add(10)
# d1.add(10,10)
# d1.add(20,20,20)
# d1.add(10,20,30,40)

print("==Method Overloading in Python(with Parameter)Static====")

class Demo2:
    @staticmethod
    def mul(num1=20,num2=30):
        print("Multiplication =",num1*num2)

# Demo2.mul(20,30)
# Demo2.mul(20,20)

print("==Method Overloading in Python(without Parameter)Non static Method====")
#Declaring same method name with different parameters in same class is called Method Overloading.
class Demo3:
    def div(self):
        a=10
        b=5
        print("Division =",a/b)
# d3=Demo3()
# d3.div()
print("==Method Overloading in Python(without Parameter)static Method====")

class Demo4:
    @staticmethod
    def sub():
        s=50
        t=20
        print("Subtraction =",s-t)

# Demo4.sub()
print("==Method Overloading in Python(without Parameter)static Method====")
















