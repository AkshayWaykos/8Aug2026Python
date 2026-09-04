
print("====Import All Module 1 and 2 in Module 3======")
#module 3=Demo 3 Operation
import Demo1
import Demo2
import Demo3

print("------From Demo1 Module 1------------")
Demo1.add()
Demo1.mul(20,20)
print("------Sample1 class from Demo1------------")
S1=Demo1.Sample1()
S1.method1()

print("------From Demo2 Module 2------------")

Demo2.sub()
Demo2.div(10,5)
print("------Sample2 class from Demo2------------")
S2=Demo2.Sample2()
S2.method2()
print("------From Demo3 Module 3------------")

S3=Demo3.Sample3(30,20)
S3.student()

Demo3.Sample3.details("Akshay",31)

print("------------------END-------------------")





