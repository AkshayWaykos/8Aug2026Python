print("===Method Overriding with using super()-non static-without Param=======")
#Declaring same method name with same parameters in different class with inheritance is called Method Overriding.
class A:
    def method(self):
        print("method from parent class")

class B(A):
    def method(self):
        print("method from child class")
        super().method()

b=B()
b.method()
print("===Method Overriding with -Static-With Param=======")

class Student:
    @staticmethod
    def info1(name,age):
        print("Student Info=",name,info)

class Parent(Student):
    @staticmethod
    def info1(name,age):
        print("Parent Info=",name,age)


Parent.info1("Akshay",31)
Parent.info1("Sagar",29)
