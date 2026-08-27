from Functionsprogram.Exp7_Function_WithParameter import studentInfo

print("============Ex 5 Static Method =====================")
#Example 1
class Demo():
    @staticmethod
    def method1():
        print("Static method")

    @staticmethod
    def square(num1):
        print("Square of no = ",num1 * num1)
Demo.method1()
Demo.square(10)

print("============")
#Example 2

class Demo2():
    @staticmethod
    def student(name,age):
        print("Student Name =", name)
        print("Age of student =",age)
    @staticmethod
    def calculation(num1,num2):
        print("Addition of 2 no = ",num1+num2)
Demo2.student("Akshay",21)
Demo2.calculation(20,20)

print("============")
#Example 3

class Demo3():
    @staticmethod
    def EmpDetails():
        print("Emp Details method from Demo3 class")

    @staticmethod
    def EmpFamilyD():
        print("print family details of Emp from Demo 3 class")
Demo3.EmpDetails()
Demo3.EmpFamilyD()
print("============")




